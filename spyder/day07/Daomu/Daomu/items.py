# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DaomuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    juan_name = scrapy.Field()
    zh_num = scrapy.Field()
    zh_name = scrapy.Field()
    zh_link=scrapy.Field()
    zh_content = scrapy.Field()
    
    pass
