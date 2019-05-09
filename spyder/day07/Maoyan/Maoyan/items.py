# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #电影名称
    name=scrapy.Field()
    #主演
    star=scrapy.Field()
    #上映时间
    time = scrapy.Field()

    pass
