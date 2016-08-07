# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class AlexaPipeline(object):
    def process_item(self, item, spider):
            with open("output_hybrid", 'a+') as f:
                 f.write(item['url'] + "\n")
            with open("output_hybrid_time", 'a+') as f:
                 f.write(item['time'] + " : " + item['url'] + "\n")
            return item
