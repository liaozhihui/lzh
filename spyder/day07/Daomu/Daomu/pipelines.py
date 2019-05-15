# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DaomuPipeline(object):
    def process_item(self, item, spider):
        filename = '{}-{}-{}.txt'.format(item['juan_name'],item['zh_num'],item['zh_name'])
        f =open(filename,'w')
        f.write(item['zh_content'])
        f.close()
        return item
