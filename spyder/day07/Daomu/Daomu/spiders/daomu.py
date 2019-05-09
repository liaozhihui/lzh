# -*- coding: utf-8 -*-
import scrapy
from ..items import DaomuItem


class DaomuSpider(scrapy.Spider):
    name = 'daomu'
    allowed_domains = ['www.daomubiji.com']
    start_urls = ['http://www.daomubiji.com/']

    #解析一级页面，提取盗墓笔记1 2 3

    def parse(self, response):
        one_link_list = response.xpath('//ul[@class="sub-menu"]/li/a/@href').extract()
        #把连接交给调度器入队列
        for one_link in one_link_list:
            yield scrapy.Request(url=one_link,callback=self.parse_to_link)
        pass
    def parse_to_link(self,response):
        # item = {}
        #基准xpath,匹配所有章节对象列表
        article_list = response.xpath('//article')
        #依次获取每个章节信息
        for article in article_list:
            item = DaomuItem()
            info=article.xpath("./a/text()").extract_first().split()
            item["juan_name"] = info[0]
            item["zh_num"] = info[1]
            item["zh_name"]=info[2]
            item['zh_link'] = article.xpath('./a/@href').extract_first()
            # yield item
            yield scrapy.Request(url=item['zh_link'],meta={"item":item},callback=self.parse_three_link)
    def parse_three_link(self,response):
        #获取小说内容
        item = response.meta['item']
        item['zh_content']="\n".join(response.xpath('//article[@class = "article-content"]//p/text()').extract())
        yield item