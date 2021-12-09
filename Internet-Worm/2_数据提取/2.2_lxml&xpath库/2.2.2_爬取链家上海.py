import requests
from lxml import etree
import csv
import time
import random

hd = {
    'Cookie': 'lianjia_uuid=01765a98-5297-41f9-b19d-89a7449cf57a; UM_distinctid=170e7a4b5ffb7b-0fe20ca1f284a2-396d7406-13c680-170e7a4b600ab1; _smt_uid=5e708c78.114db2b5; _ga=GA1.2.1647190516.1584434300; Hm_lvt_efa595b768cc9dc7d7f9823368e795f1=1586413493; _jzqc=1; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1588042734,1588666427,1588781312; login_ucid=2000000104475969; lianjia_token=2.0056965abb2a471a16473b738a5da3f650; lianjia_token_secure=2.0056965abb2a471a16473b738a5da3f650; security_ticket=ly2D3K/R3CHcH/rpkTzZWS9GWnVPTplSJLozELc90YS4jI1ZuhAUT6GTMnCrGX91tdjv7Llt3XA7DIFzv3QwmYx9HtQN/j2qxTH9C5nRqHVXA+RGI3dXryIHJWvzjiFVahEA0QqknBH1k6PbtYD2K7Gq1RSNZyIkw/SWHXDaE0c=; select_city=310000; lianjia_ssid=c363f9cb-3fff-4872-9c98-d3fd55dc5146; _jzqa=1.3759888401518846500.1584434297.1589293140.1589551538.16; _jzqx=1.1584434297.1589551538.5.jzqsr=google%2Ecom|jzqct=/.jzqsr=google%2Ecom|jzqct=/; _jzqckmp=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22170e7a4bcdc247-0c752ca4b1a414-396d7406-1296000-170e7a4bcddb75%22%2C%22%24device_id%22%3A%22170e7a4bcdc247-0c752ca4b1a414-396d7406-1296000-170e7a4bcddb75%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24latest_referrer_host%22%3A%22www.google.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; _gid=GA1.2.2015424423.1589551539; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1589551577; _jzqb=1.5.10.1589551538.1',
    'Referer': 'https://sh.lianjia.com/ershoufang/tt9/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}

ershoufang_list = []
count=0
for i in range(1,3):
    original_url = 'https://sh.lianjia.com/ershoufang/pg'
    url = original_url + str(i) + 'tt9'
    r = requests.get(url, headers=hd, timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.status_code)
    html = etree.HTML(r.text)
    listcontents = html.xpath("//div//div//ul[@class='sellListContent']/li")
    # print(listcontents)
    for listcontent in listcontents:
        title = listcontent.xpath(".//div[@class='title']/a/text()")[0]
        address = listcontent.xpath(".//div[@class='positionInfo']/a[1]/text()")[0]
        area = listcontent.xpath(".//div[@class='positionInfo']/a[2]/text()")[0]
        link = listcontent.xpath(".//div[@class='title']/a/@href")
        houseinfo = listcontent.xpath(".//div[@class='houseInfo']/text()")[0]
        house_type = houseinfo.split('|')[0].strip()
        house_square = houseinfo.split('|')[1].strip()
        house_face = houseinfo.split('|')[2].strip()
        house_decoration = houseinfo.split('|')[3].strip()
        house_height = houseinfo.split('|')[4].strip()
        house_built_year = houseinfo.split('|')[5].strip()
        try:
            building_type = houseinfo.split('|')[6].strip()
        except:
            building_type = '暂无数据'
        totalprice = listcontent.xpath(".//div[@class='totalPrice']/span/text()")[0]
        unitprice = listcontent.xpath(".//div[@class='unitPrice']/span/text()")[0]
        followinfo = listcontent.xpath(".//div[@class='followInfo']/text()")[0]
        star = followinfo.split('/')[0].strip()
        publish_date = followinfo.split('/')[1].strip()

        ershoufang_list.append(
            [count + 1, title, address, area, totalprice + "万", unitprice, house_type, house_square, house_face,
             house_height, house_built_year, house_decoration, building_type,link])
        count += 1
        print(ershoufang_list)
    time.sleep(random.randint(0,5))

with open("sh_lianjia2.csv","w",encoding='utf-8') as fp:
    writer = csv.writer(fp)
    header = ['序号',"名字","小区","区域","总价","单价","房屋类型","房屋面积","房屋朝向","房屋楼层","房屋建造年代","房屋装修","楼层类型","房屋链接"]
    writer.writerow(header)
    for line in ershoufang_list:
        writer.writerow(line)
