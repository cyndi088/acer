# -*- coding: utf-8 -*-
import scrapy
from db import db
from scrapy import Request


class EntherscanContracAddressSpider(scrapy.Spider):
    name = 'entherscan_contrac_address'
    allowed_domains = ['etherscan.io']
    start_urls = ['http://api.etherscan.io/']

    def parse(self, response):
        state_code = response
        parse_urls = 'http://api.etherscan.io/api?module=account&action=tokentx&contractaddress=%s&startblock=%d&endblock=%d&sort=desc&apikey=18RC3HD9A4Z7E21DA4DWTFX8TZ6VNWYI7M'
        addresses = db['etherscan_contract_address'].find()
        for address in addresses:
            contract_address = address['contract_address']
            symbol = address['symbol']
            if symbol in db['etherscan_token'].distinct("token_symbol"):
                start_block_list = db['etherscan_token'].find({"token_symbol": symbol}).sort([("time_stamp", -1)]).limit(1)
                start_block = int([start_block_list[0]][0]['block_height'])
                end_block = start_block + 10000
                request = Request(parse_urls % (contract_address, start_block, end_block), callback=self.parse_list)
            # request = Request(parse_urls % contract_address, callback=self.parse_list)
                yield request
            else:
                pass

    def parse_list(self, response):
        resp = json.loads(response.text)
        data = resp['result']
        # parse_transfer_urls = 'https://etherscan.io/tx/%s'
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
            # request = Request(parse_transfer_urls % dt['hash'], callback=self.transfer_parse, meta=item)
            # yield request

    # def transfer_parse(self, response):
    #     # pass
    #     res = Selector(response)
    #     token_transfer = res.xpath('//*[@id="ContentPlaceHolder1_maintable"]/div[14]/span/text()[1]').extract()
    #     item = {}
    #     meta = response.meta
    #     item['block_height'] = meta['block_height']
    #     item['token_name'] = meta['token_name']
    #     item['token_symbol'] = meta['token_symbol']
    #     item['token_transfer'] = token_transfer[0]
    #     item['time_stamp'] = meta['time_stamp']
    #     item['hash'] = meta['hash']
    #     item['block_hash'] = meta['block_hash']
    #     item['from_where'] = meta['from_where']
    #     item['to_where'] = meta['to_where']
    #     yield item