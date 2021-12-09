# -*- coding: utf-8 -*-
import scrapy


class MoguSpiderSpider(scrapy.Spider):
    name = 'mogu_spider'
    allowed_domains = ['mogu.com']
    start_urls = ['http://mogu.com/']

    def parse(self, response):
        pass
