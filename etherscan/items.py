# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EtherscanItem(scrapy.Item):
    block_number = scrapy.Field()
    token_name = scrapy.Field()
    token_symbol = scrapy.Field()
    time_stamp = scrapy.Field()
    hash = scrapy.Field()
    block_hash = scrapy.Field()
    from_where = scrapy.Field()
    to_where = scrapy.Field()
    value = scrapy.Field()
