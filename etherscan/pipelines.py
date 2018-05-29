# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.utils.project import get_project_settings
from pymongo import MongoClient
import json

class EtherscanPipeline(object):
    def process_item(self, item, spider):
        return item

class MongoPipeline(object):
    def __init__(self):
        settings = get_project_settings()
        self.client = MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'])
        self.db = self.client[settings['MONGO_DB']]
        self.coll = self.db[settings['MONGO_COLL']]

    def process_item(self, item, spider):
        self.coll.insert(dict(item))
        # print(type(item))
        return item