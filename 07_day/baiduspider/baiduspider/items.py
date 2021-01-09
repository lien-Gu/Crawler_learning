# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaiduspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    python_infoitem=scrapy.Field()
    python_chineseName_item=scrapy.Field()
    python_timeitem=scrapy.Field()
