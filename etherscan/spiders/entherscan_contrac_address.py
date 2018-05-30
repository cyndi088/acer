# -*- coding: utf-8 -*-
import scrapy
import json
from etherscan.items import EtherscanItem
from db import db
from scrapy import Request
import requests

class EntherscanContracAddressSpider(scrapy.Spider):
    name = 'entherscan_contrac_address'
    allowed_domains = ['etherscan.io']
    start_urls = ['https://etherscan.io/']

    def parse(self, response):
        state_code = response
        parse_urls = 'http://api.etherscan.io/api?module=account&action=tokentx&contractaddress=%s&startblock=5690000&endblock=5700000&sort=desc&apikey=18RC3HD9A4Z7E21DA4DWTFX8TZ6VNWYI7M'
        details = db['etherscan_contract_address'].find()
        for address in details:
            request = Request(parse_urls % address['contract_address'], callback=self.parse_list)
            yield request

    def parse_list(self, response):
        # print(response.url)
        resp = json.loads(response.text)
        # print(resp)
        data = resp['result']
        # print(data)
        for dt in data:
            item = {}
            item['block_height'] = dt['blockNumber']
            item['token_name'] = dt['tokenName']
            item['token_symbol'] = dt['tokenSymbol']
            item['time_stamp'] = dt['timeStamp']
            item['token_transfer'] = dt['value']
            item['hash'] = dt['hash']
            item['block_hash'] = dt['blockHash']
            item['from_where'] = dt['from']
            item['to_where'] = dt['to']
            yield item
