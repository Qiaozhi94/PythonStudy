# -*- coding: utf-8 -*-
import scrapy


class DemocompleteSpider(scrapy.Spider):
    name = 'demo_complete'
    allowed_domains = ['python123.io']
    def start_requests(self):
        urls = [
                  'http://python123.io/ws/demo.html'

               ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)


    def parse(self, response):
        fname = response.url.split('/')[-1]
        with open (fname,'wb') as f:
            f.write(response.body)
        self.log('saved file %s' %fname)
