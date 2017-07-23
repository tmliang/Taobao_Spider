# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request
from taobao_spider.items import TaobaoSpiderItem
import urllib.request
from scrapy_redis.spiders import RedisSpider

class TaobaoSpider(RedisSpider):
    name = 'taobao'
    #allowed_domains = ['taobao.com']
    # start_urls = ['http://taobao.com/']
    redis_key = 'TaobaoSpider:start_urls'

    def parse(self, response):
        key = input("请输入你要爬取的关键词\t")
        pages = input("请输入你要爬取的页数\t")
        # key = "虾饺"
        # pages = '100'
        print("\n")
        print("当前爬取的关键词是",key)
        print("\n")
        for i in range(0, int(pages)):
            url = "https://s.taobao.com/search?q=" + str(key) + "&s=" + str(44*i)
            yield Request(url=url, callback=self.page)
        pass

    def page(self,response):
        body = response.body.decode('utf-8', 'ignore')

        pat_id = '"nid":"(.*?)"'    #匹配id
        pat_now_price = '"view_price":"(.*?)"'      #匹配价格
        pat_address = '"item_loc":"(.*?)"'      #匹配地址

        all_id = re.compile(pat_id).findall(body)
        all_now_price = re.compile(pat_now_price).findall(body)
        all_address = re.compile(pat_address).findall(body)

        for i in range(0, len(all_id)):
            this_id = all_id[i]
            now_price = all_now_price[i]
            address = all_address[i]
            url = "https://item.taobao.com/item.htm?id=" + str(this_id)
            yield Request(url=url, callback=self.next, meta={ 'now_price': now_price, 'address': address})
            pass
        pass

    def next(self, response):
        item = TaobaoSpiderItem()
        url = response.url
        pat_url = "https://(.*?).com"
        web = re.compile(pat_url).findall(url)

        #淘宝和天猫的某些信息采用不同方式的Ajax加载，
        if web[0] != 'item.taobao':     #天猫或天猫超市
            title = response.xpath("//div[@class='tb-detail-hd']/h1/text()").extract()  #获取商品名称
            price = response.xpath("//span[@class = 'tm-price']/text()").extract()  #获取商品原价格
            pat_id = 'id=(.*?)&'
            this_id = re.compile(pat_id).findall(url)[0]
            pass
        else:       #淘宝
            title = response.xpath("//h3[@class='tb-main-title']/@data-title").extract() #获取商品名称
            price = response.xpath("//em[@class = 'tb-rmb-num']/text()").extract()  #获取商品原价格
            pat_id = 'id=(.*?)$'
            this_id = re.compile(pat_id).findall(url)[0]
            pass

        #抓取评论总数
        comment_url = 'https://dsr-rate.tmall.com/list_dsr_info.htm?itemId=' + str(this_id)
        comment_data = urllib.request.urlopen(comment_url).read().decode('utf-8', 'ignore')
        each_comment = '"rateTotal":(.*?),"'
        comment = re.compile(each_comment).findall(comment_data)


        item['title'] = title
        item['link'] = url
        item['price'] = price
        item['now_price'] = response.meta['now_price']
        item['comment'] = comment
        item['address'] = response.meta['address']

        yield item