# -*- coding: utf-8 -*-
import scrapy
import json
from etherscan.items import EtherscanItem
from scrapy.utils.project import get_project_settings
from pymongo import MongoClient

class EntherscanContracAddressSpider(scrapy.Spider):
    name = 'entherscan_contrac_address'
    allowed_domains = ['etherscan.io']
    base_url = 'http://api.etherscan.io/api?module=account&action=tokentx&contractaddress='
    start_block = '5660000'
    end_block = '5700000'
    api_key = '18RC3HD9A4Z7E21DA4DWTFX8TZ6VNWYI7M'

    contract_address = '0x3136ef851592acf49ca4c825131e364170fa32b3'
    start_urls = base_url + contract_address + '&startblock=' + start_block + '&endblock=' + end_block + '&sort=desc&apikey=' + api_key

    def parse(self, response):
        resp = json.loads(response.text)
        data = resp['result']
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
