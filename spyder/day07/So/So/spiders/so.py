# -*- coding: utf-8 -*-
import scrapy,json
from ..items import SoItem

class SoSpider(scrapy.Spider):
    name = 'so'
    allowed_domains = ['image.so.com']
    
    #爬虫程序不去找start_urls，而是到这里
    def start_requests(self):
        for page in range(5):
            url = "http://image.so.com/zj?ch=beauty&sn={}&listtype=new&temp=1".format(str(page*30))
            #把url地址入队列
            yield scrapy.Request(url=url,callback=self.parse_img)

    def parse_img(self, response):
        html = json.loads(response.text)
        for img in html['list']:
            item = SoItem()
            item['img_link']=img["qhimg_url"]

            yield item
        pass
