# -*- coding: utf-8 -*-
import scrapy



class ShLianjiaSpiderSpider(scrapy.Spider):
    name = 'sh_lianjia_spider'
    allowed_domains = ['sh.lianjia.com/ershoufang/tt9/']
    start_urls = ['http://sh.lianjia.com/ershoufang/tt9/']

    def parse(self, response):
        listcontents = response.xpath("//div//div//ul[@class='sellListContent']/li")
        # print(listcontents)
        for listcontent in listcontents:
            title = listcontent.xpath(".//div[@class='title']/a/text()").get()
            print(title)

