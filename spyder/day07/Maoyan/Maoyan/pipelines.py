# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from Maoyan.settings import *
class MaoyanPipeline(object):
    def process_item(self, item, spider):
        print("*"*50)
        print(dict(item))
        return item

#新建管道类，存入mysql
class MaoyanMysqlPipeline(object):
    #开启爬虫时执行，只执行一次
    def open_spider(self,spider):
        #一般用于开启数据库
        print("oepn函数")
        # self.db = pymysql.connect(MYSQL_HOST,MYSQL_USER,MYSQL_PWD,MYSQL_DB,charset="utf8")
        # self.cursor = self.db.cursor()
    
    #爬虫结束时，只执行一次
    def close_spider(self,spider):
        #一般用于断开数据库
        print("close函数")
        # self.cursor.close()
        # self.db.close()
        pass

    def process_item(self,item,spider): 
        # ins = "insert into film(name,star,time) values (%s,%s,%s)"
        # L = [item['name'].strip(),item['star'].strip(),item['time'].strip()]
        # self.cursor.excute(ins,L)
        # self.db.commit()
        print("="*50)
        print(dict(item))
        return item      
        
