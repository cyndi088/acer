# -*- coding: utf-8 -*-
import scrapy
import json
from etherscan.items import EtherscanItem

class EntherscanContracAddressSpider(scrapy.Spider):
    name = 'entherscan_contrac_address'
    allowed_domains = ['etherscan.io']
    start_urls = ['http://api.etherscan.io/api?module=account&action=tokentx&contractaddress=0x3136ef851592acf49ca4c825131e364170fa32b3&startblock=5660000&endblock=5700000&sort=desc&apikey=18RC3HD9A4Z7E21DA4DWTFX8TZ6VNWYI7M']

    def parse(self, response):
        resp = json.loads(response.text)
        data = resp['result']
        for dt in data:
            item = {}
            item['block_number'] = dt['blockNumber']
            item['token_name'] = dt['tokenName']
            item['token_symbol'] = dt['tokenSymbol']
            item['time_stamp'] = dt['timeStamp']
            item['hash'] = dt['hash']
            item['block_hash'] = dt['blockHash']
            item['from_where'] = dt['from']
            item['to_where'] = dt['to']
            item['value'] = dt['value']

            yield item
            # print(type(item))
