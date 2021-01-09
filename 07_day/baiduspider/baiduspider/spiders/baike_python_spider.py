# -*- coding: utf-8 -*-
import scrapy
from baiduspider.items import BaiduspiderItem
'''
爬取内容：
 介绍、中文名、发行时间
'''

class BaikePythonSpiderSpider(scrapy.Spider):
    name = 'baike_python_spider'
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/Python/407313']

    def parse(self, response):
        # bitems=BaiduspiderItem()
        # python_info=response.xpath('/html/body/div[4]/div[2]/div/div[2]/div[4]/div/text()').get()
        python_chineseName=response.xpath('/html/body/div[4]/div[2]/div/div[2]/div[7]/dl[1]/dd[1]/text()').get()
        python_time=response.xpath('/html/body/div[4]/div[2]/div/div[2]/div[7]/dl[1]/dd[4]/text()').get()
        print(python_chineseName,python_time)
