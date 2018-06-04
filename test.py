import scrapy
import requests
from lxml import etree
from pymongo import MongoClient
from scrapy.utils.project import get_project_settings
from pymongo import MongoClient
import json
from scrapy import Request
from scrapy.selector import Selector
import pymongo

# res = requests.get('https://api.etherscan.io/api?module=account&action=txlist&address=0x3136ef851592acf49ca4c825131e364170fa32b3&startblock=5660000&endblock=5690000&sort=desc&apikey=18RC3HD9A4Z7E21DA4DWTFX8TZ6VNWYI7M')
# print(res.json())

# client = MongoClient('mongodb://localhost:27017/')
# db = client.pythondb
# posts = db.posts
#
# post = {"name": "Maxsu",
#          "old": "My first blog post!",
#          "tags": "mongodb"}
# def main(data):
#     posts.insert(data)
#
# main(post)

# base_url = 'https://etherscan.io/token/'
# contract_xpath = '//*[@id="ContentPlaceHolder1_trContract"]/td/a/text()'
# res = 'TIME'
# url = base_url + res
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'referer': 'https://etherscan.io/',
    'cookie': '__cfduid=de6e94b9990ecaf510c5e81ba4f18206e1527129086;_ga=GA1.2.799864744.1527129086;etherscan_autologin=True;etherscan_userid=cyndi088;etherscan_cookieconsent=True;showfavourite0x3136ef851592acf49ca4c825131e364170fa32b3=0;etherscan_pwd=4792:Qdxb:gWdslDXDqgylK/l0r3N8WpQzp9WmmAkS4NKmhfEcZg4=;_gid=GA1.2.705220662.1527472614;ASP.NET_SessionId=3d2c00vzkyyvxm4c5ipjkkjd;__cflb=1309472310;cf_clearance=b61561284fc42c9e8b1cddec2d2db3ac31ef59a6-1527745706-2700;_gat_gtag_UA_46998878_6=1',
}
# resp = requests.get(url, headers)
# html_tree = etree.HTML(resp.text)
# contract_list = html_tree.xpath(contract_xpath)
# print(contract_list[0])

# res = requests.get('https://etherscan.io/token/TenXPay')
# print(res.status_code == 200)

# res = requests.get('http://api.etherscan.io/api?module=account&action=tokentx&contractaddress=0x3136ef851592acf49ca4c825131e364170fa32b3&startblock=5660000&endblock=5680000&sort=desc&apikey=18RC3HD9A4Z7E21DA4DWTFX8TZ6VNWYI7M')
# resp = res.json()
# data = resp['result'] #列表
# for dt in data:
#     item = {}
#     item['block_number'] = dt['blockNumber']
#     item['token_name'] = dt['tokenName']
#     item['token_symbol'] = dt['tokenSymbol']
#     item['time_stamp'] = dt['timeStamp']
#     item['hash'] = dt['hash']
#     item['block_hash'] = dt['blockHash']
#     item['from_where'] = dt['from']
#     item['to_where'] = dt['to']
#     item['value'] = dt['value']
#     print(item)
# http://api.etherscan.io/api?module=account&action=tokentx&contractaddress=0x3136ef851592acf49ca4c825131e364170fa32b3&startblock=5660000&endblock=5690000&sort=desc&apikey=18RC3HD9A4Z7E21DA4DWTFX8TZ6VNWYI7M
# http://api.etherscan.io/api?module=account&action=tokentx&contractaddress=0x3136ef851592acf49ca4c825131e364170fa32b3&startblock=5660000&endblock=5700000&sort=desc&apikey=18RC3HD9A4Z7E21DA4DWTFX8TZ6VNWYI7M
# base_url = 'http://api.etherscan.io/api?module=account&action=tokentx&contractaddress='
# start_block = '5660000'
# end_block = '5700000'
# api_key = '18RC3HD9A4Z7E21DA4DWTFX8TZ6VNWYI7M'
# contract_address = '0x3136ef851592acf49ca4c825131e364170fa32b3'
# start_urls = base_url + contract_address + '&startblock=' + start_block + '&endblock=' + end_block + '&sort=desc&apikey=' + api_key
# print(start_urls)



mongo_url = "mongodb://1o746k7976.51mypc.cn:31006"
mongo_user = "llps"
mongo_password = "llps&789"
mongo_auth = "admin"
mongo_mechanism = "SCRAM-SHA-1"
client = MongoClient(mongo_url, username=mongo_user, password=mongo_password, authSource=mongo_auth, authMechanism=mongo_mechanism)
db = client['neo_crawl_data']
# startaddress = db['etherscan_token'].find()
# 根据token_symbol对应的时间戳，获取最新的block_height
rsp = db['etherscan_token'].find({"token_symbol": "QAU"}).sort([("time_stamp", -1)]).limit(1)
# print([rsp[0]][0]['block_height'])
# 获取某个字段值的种类数
print(len(db['etherscan_token'].distinct("token_symbol")))
# 判断contract_address中的symbol是否存在于etherscan_token中
# print("COFI" in db['etherscan_token'].distinct("token_symbol"))


# details = db['etherscan_contract_address'].find()
# for address in details:
#     # request = Request(parse_urls % address['contract_address'], callback=self.parse)
#     # yield request
#     parse_urls = 'http://api.etherscan.io/api?module=account&action=tokentx&contractaddress=%s&startblock=5690000&endblock=5700000                      &sort=desc&apikey=18RC3HD9A4Z7E21DA4DWTFX8TZ6VNWYI7M'
#     msg = requests.get(parse_urls % address['contract_address']).text
#     data = json.loads(msg)
#     print(data)
    # for dt in data['result']:
    #     item = {}
    #     item['block_number'] = dt['blockNumber']
    #     item['token_name'] = dt['tokenName']
    #     item['token_symbol'] = dt['tokenSymbol']
    #     item['time_stamp'] = dt['timeStamp']
    #     item['hash'] = dt['hash']
    #     item['block_hash'] = dt['blockHash']
    #     item['from_where'] = dt['from']
    #     item['to_where'] = dt['to']
    #     item['value'] = dt['value']
    #     print(item)

# resp = requests.get('https://etherscan.io/tx/0xb080c0cad4aaa773441f3099a8dcfd94a1d3d5804f170c5e60c84da16dec64a7')
# hxs = Selector(resp)
# sites = hxs.xpath('//*[@id="ContentPlaceHolder1_maintable"]/div[14]/span/text()[1]').extract()
# print(sites[0])

# res = requests.get('https://etherscan.io/tx/0x1f5c010b9b7694d3342a803aaa94d4d330b27fc0727d774a9cd94b0b02d5e077', headers)
# print(res)


# def func():
#     for i in range(11):
#         stad = 500
#         stad += 1
#         ead = stad + 1
#         post = json.dumps({'start': stad, 'end': ead})
#         print(type(post))
#         print(type(json.loads(post)))
#         # yield post
#
# def writedb(post):
#     posts = db.etherscan_tests
#     # posts.insert_many(post)
#
# writedb(func())

# def parse():
#     # state_code = response
#     parse_urls = 'http://api.etherscan.io/api?module=account&action=tokentx&contractaddress=%s&startblock=%s&endblock=5710000&sort=desc&apikey=18RC3HD9A4Z7E21DA4DWTFX8TZ6VNWYI7M'
#     details = ['contract_address']
#     for address in details:
#         request = Request(parse_urls % (address, 500))
#         print(request)
#
# parse()












