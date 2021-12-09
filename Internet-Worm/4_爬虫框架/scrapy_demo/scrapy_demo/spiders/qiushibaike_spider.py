# -*- coding: utf-8 -*-
import scrapy


class QiushibaikeSpiderSpider(scrapy.Spider):
    name = 'qiushibaike_spider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['http://www.qiushibaike.com/text/page/1/']

    def parse(self, response):
        divs = response.xpath("//div[@class='col1 old-style-col1']/div")
        for div in divs:
            author_name = div.xpath(".//h2/text()").get()
            print("="*40)
            print(author_name)
            print("=" * 40)
            author_year = div.xpath(".//div[@class='author clearfix']//div/text()")
            article = div.xpath(".//a/div[@class='content']/text()")
            stats = div.xpath(".//div[@class='stats']/text()")
            funny_num = stats.split("·")[0].strip()
            comments_num = stats.split("·")[1].strip()


