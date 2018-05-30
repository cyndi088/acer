import scrapy
import requests
from lxml import etree
from pymongo import MongoClient
from scrapy.utils.project import get_project_settings
from pymongo import MongoClient
import json

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
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
#     'cookie': '__cfduid=de6e94b9990ecaf510c5e81ba4f18206e1527129086; _ga=GA1.2.799864744.1527129086; etherscan_autologin=True; etherscan_userid=cyndi088; etherscan_cookieconsent=True; showfavourite0x3136ef851592acf49ca4c825131e364170fa32b3=0; etherscan_pwd=4792:Qdxb:gWdslDXDqgylK/l0r3N8WpQzp9WmmAkS4NKmhfEcZg4=; _gid=GA1.2.705220662.1527472614; __cflb=2482413123; ASP.NET_SessionId=3d2c00vzkyyvxm4c5ipjkkjd',
#     'referer': url,
# }
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
details = db['etherscan_contract_address'].find()
for address in details:
    # request = Request(parse_urls % address['contract_address'], callback=self.parse)
    # yield request
    parse_urls = 'http://api.etherscan.io/api?module=account&action=tokentx&contractaddress=%s&startblock=5690000&endblock=5700000                      &sort=desc&apikey=18RC3HD9A4Z7E21DA4DWTFX8TZ6VNWYI7M'
    msg = requests.get(parse_urls % address['contract_address']).text
    data = json.loads(msg)
    print(data)
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