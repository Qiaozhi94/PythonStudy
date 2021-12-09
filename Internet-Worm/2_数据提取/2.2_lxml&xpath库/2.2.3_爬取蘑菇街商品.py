import requests
import csv
import time
from lxml import etree


original_url = "https://list.mogu.com/search/goods?q=连衣裙"
# search = input("请输入要搜索的商品名称")
# url = original_url + search

hd = {
     'authority': 'list.mogu.com',
     'method': 'GET',
     'scheme': 'https',
     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
     'accept-language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
     'cache-control': 'max-age=0',
     'cookie': '__mgjuuid=134d89fe-0e1c-4a54-bbb9-a3d9e94ff12b; _mwp_h5_token_enc=abcfb779c57e3fc9e5d9278b3bb7f58c; _mwp_h5_token=b2f5a469963490c1032b6a23a8b869ab_1589777368638',
     'sec-fetch-dest': 'document',
     'sec-fetch-mode': 'avigaten',
     'sec-fetch-site': 'none',
     'sec-fetch-user': '?1',
     'upgrade-insecure-requests': '1',
     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
     }

r = requests.get(original_url,headers=hd, timeout=30)
r.raise_for_status()
print(r.status_code)
r.encoding=r.apparent_encoding
# print(r.text)
html = etree.HTML(r.text)
# goods= html.xpath("//div[@class='goods_list_mod']//div[@class='pin-item-wrap']")
goods= html.xpath("//div[@id='wall_goods_box']//div")
for good in goods:
    good_name = good.xpath(".//div[@class='pin-info-title']/text()")[0]
    print(good_name)
    print(type(good_name))
    # good_price =good.xpath("")
    # good_link = good.xpath("")
    # good_org_price = good.xpath("")
    # good_star = good.xpath("")



