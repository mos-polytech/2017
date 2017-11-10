# -*- coding: utf-8 -*-

import scrapy
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

__author__ = 'sobolevn'


class CustomPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, BlogPost):
            item['name'] = 'URL: ' + item['name']
        return item


class BlogPost(scrapy.Item):
    name = scrapy.Field(output_processor=TakeFirst())


class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://blog.scrapinghub.com', ]

    custom_settings = {
        'ITEM_PIPELINES': {
            'spider.CustomPipeline': 1
        }
    }

    def parse(self, response):
        selector = Selector(response)

        for post in selector.css('article.post'):
            print('---------------------------------')

            loader = ItemLoader(BlogPost(), post)
            loader.add_css('name', '.entry-title > a::text')
            yield loader.load_item()