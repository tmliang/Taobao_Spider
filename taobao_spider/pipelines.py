# -*- coding: utf-8 -*-
import pymongo
from scrapy.conf import settings
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TaobaoSpiderPipeline(object):
    def __init__(self):
        # 链接数据库
        self.client = pymongo.MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'])
        # self.client.admin.authenticate(settings['MINGO_USER'], settings['MONGO_PSW'])     #如果有账户密码
        self.db = self.client[settings['MONGO_DB']]  # 获得数据库的句柄
        self.coll = self.db[settings['MONGO_COLL']]  # 获得collection的句柄

    def process_item(self, item, spider):
        try:
            title = item['title'][0]
            link = item['link']
            price = item['price'][0]
            now_price = item['now_price']
            comment = item['comment'][0]
            address = item['address']
            print('商品标题\t', title)
            print('商品链接\t', link)
            print('商品原价\t', price)
            print('商品现价\t', now_price)
            print('商家地址\t', address)
            print('评论数量\t', comment)
            print('------------------------------\n')
            postItem = dict(商品标题=title,商品链接=link,商品原价=price,商品现价=now_price,商家地址=address,评论数量=comment)
            self.coll.insert(postItem)
            return item
        except Exception as err:
            pass