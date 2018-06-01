# -*- coding: utf-8 -*-
from pymongo import MongoClient
import re
import requests
from lxml import etree

mongo_url = "mongodb://1o746k7976.51mypc.cn:31006"
mongo_user = "llps"
mongo_password = "llps&789"
mongo_auth = "admin"
mongo_mechanism = "SCRAM-SHA-1"
client = MongoClient(mongo_url, username=mongo_user, password=mongo_password, authSource=mongo_auth, authMechanism=mongo_mechanism)
db = client['neo_crawl_data']
details = db['currency_projectdetail'].find()
base_url = 'https://etherscan.io/token/'
contract_xpath = '//*[@id="ContentPlaceHolder1_trContract"]/td[@class="tditem"]/a/text()'

# 从neo_crawl_data数据库中currency_projectdetail集合中获取数据
def select_etherscan(data):
    for detail in data:
        # 判断字段'Explorer'是否存在，存在则取出对应的值
        if 'Explorer' in detail.keys():
            # 取出对应的'symbol'的值
            symbol = detail['symbol']
            explorer = detail['Explorer']
            res = re.findall('https://etherscan.io/token/(.*)', explorer)
            if len(res) != 0:
                res = res[0].replace('/', '')
                if len(res) > 42:
                    res = res[:-9]
                    post = {'symbol': symbol, 'contract_address': res}
                    yield post
                    # print(post)
                elif len(res) < 42:
                    url = base_url + res
                    headers = {
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
                        'cookie': '__cfduid=de6e94b9990ecaf510c5e81ba4f18206e1527129086; _ga=GA1.2.799864744.1527129086; etherscan_autologin=True; etherscan_userid=cyndi088; etherscan_cookieconsent=True; showfavourite0x3136ef851592acf49ca4c825131e364170fa32b3=0; etherscan_pwd=4792:Qdxb:gWdslDXDqgylK/l0r3N8WpQzp9WmmAkS4NKmhfEcZg4=; _gid=GA1.2.705220662.1527472614; __cflb=2482413123; ASP.NET_SessionId=3d2c00vzkyyvxm4c5ipjkkjd',
                        'referer': url,
                    }
                    resp = requests.get(url, headers)
                    html_tree = etree.HTML(resp.text)
                    contract_list = html_tree.xpath(contract_xpath)
                    if len(contract_list) != 0:
                        res = contract_list[0]
                        post = {'symbol': symbol, 'contract_address': res}
                        yield post
                        # print(contract_list)
                    else:
                        pass
                else:
                    res = res
                    post = {'symbol': symbol, 'contract_address': res}
                    yield post
                    # print(post)
            else:
                pass
                # print('Not etherscan !')
        else:
            pass
            # print('Explorer not exists !')

# select_etherscan(details)
def write_database(post):
    posts = db.etherscan_contract_address_test
    posts.insert_many(post)

write_database(select_etherscan(details))

