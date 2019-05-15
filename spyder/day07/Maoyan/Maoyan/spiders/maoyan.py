# -*- coding: utf-8 -*-
import scrapy
from Maoyan.items import MaoyanItem

class MaoyanSpider(scrapy.Spider):
    #爬虫名
    name = 'maoyan'
    #允许爬虫的域名
    allowed_domains = ['maoyan.com']
    offset=0
    #起始URL地址
    start_urls = ['http://maoyan.com/board/4?offset=0']

    def parse(self, response):
        dd_list = response.xpath('//dl[@class="board-wrapper"]/dd')

        for dd in dd_list:
            # item={}
            item = MaoyanItem()
            item['name'] = dd.xpath('./a/@title').extract()[0]
            item['star'] = dd.xpath('.//p[@class="star"]/text()').extract()[0].strip()
            item['time'] = dd.xpath('.//p[@class="releasetime"]/text()').extract()[0]
            yield item
        for offset in range(10,91,10):
            url='http://maoyan.com/board/4?offset={}'.format(str(offset))
            #把地址交给调度器入队列
            yield scrapy.Request(url=url,callback=self.parse)
