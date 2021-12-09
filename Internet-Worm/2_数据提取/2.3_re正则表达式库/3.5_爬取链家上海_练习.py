import re
import requests
import bs4
from bs4 import BeautifulSoup

start_url = "https://sh.lianjia.com/ershoufang/"

hd = {
         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
         'Accept-Encoding':'gzip, deflate, br',
         'Accept-Language':'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
         'Connection':'keep-alive',
         'Cookie': 'TY_SESSION_ID=a8b49a91-b1cb-441a-9785-8c6224bdf3c6; lianjia_uuid=01765a98-5297-41f9-b19d-89a7449cf57a; UM_distinctid=170e7a4b5ffb7b-0fe20ca1f284a2-396d7406-13c680-170e7a4b600ab1; _smt_uid=5e708c78.114db2b5; _ga=GA1.2.1647190516.1584434300; Hm_lvt_efa595b768cc9dc7d7f9823368e795f1=1586413493; _jzqc=1; _qzjc=1; _gid=GA1.2.1309591494.1589124912; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1588042734,1588666427,1588781312; login_ucid=2000000104475969; lianjia_token=2.0056965abb2a471a16473b738a5da3f650; lianjia_token_secure=2.0056965abb2a471a16473b738a5da3f650; security_ticket=ly2D3K/R3CHcH/rpkTzZWS9GWnVPTplSJLozELc90YS4jI1ZuhAUT6GTMnCrGX91tdjv7Llt3XA7DIFzv3QwmYx9HtQN/j2qxTH9C5nRqHVXA+RGI3dXryIHJWvzjiFVahEA0QqknBH1k6PbtYD2K7Gq1RSNZyIkw/SWHXDaE0c=; select_city=310000; CNZZDATA1253492439=646215105-1588040561-https%253A%252F%252Fwww.google.com%252F%7C1589210502; CNZZDATA1254525948=1479450439-1588037718-https%253A%252F%252Fwww.google.com%252F%7C1589210390; CNZZDATA1255633284=1262782669-1588041365-https%253A%252F%252Fwww.google.com%252F%7C1589208598; CNZZDATA1255604082=1745799172-1588039033-https%253A%252F%252Fwww.google.com%252F%7C1589210640; _jzqa=1.3759888401518846500.1584434297.1589177399.1589212040.13; _jzqx=1.1584434297.1589212040.3.jzqsr=google%2Ecom|jzqct=/.jzqsr=google%2Ecom|jzqct=/; _jzqckmp=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22170e7a4bcdc247-0c752ca4b1a414-396d7406-1296000-170e7a4bcddb75%22%2C%22%24device_id%22%3A%22170e7a4bcdc247-0c752ca4b1a414-396d7406-1296000-170e7a4bcddb75%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1589212365; _qzja=1.1285165120.1588042706441.1589177398954.1589212039553.1589212363382.1589212365269.0.0.0.50.10; _qzjb=1.1589212039553.8.0.0.0; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiM2RmY2Y4YjIyY2Q0Y2VlYWFiYjljMTlhZGI1NTYzYzlhODM1MDlhNWE5MTRlNTllZjgwZmQ2ZDczMjY1ZDlhNDc5NzRmMTE2ZDk2YjM1N2Y2NjA2YTdjZmQ0MWI2YjhmNWEyOTJlMTM4ZTkyNmRkOGZkOTIzMzk4ZmM2MDM1OTFmNzMzOGZiNjAwMjY3ZDU2ODBhZGVkNTI0M2QyYjc3NDhkNzVkOGVmYWY1ODBlMzU1NTAzMWRiZTUxM2RhMTg2NDRhNmY0NzA2MjQ2ZmRlNGZmNmFjYWUzNjVhOTBjYzEwYmNmNTdiNDlmZjBlZTczOGM5NmU3ZmQ3OGQzZGQwYmM3MmJkMWU1MTMzYzEyYWRkMGVjN2E0NTYwZWFjNDRhY2Y1MDQxNDM0NzBkMjllZjM1ZDU3OTRmYmNhNTE4NzZcIixcImtleV9pZFwiOlwiMVwiLFwic2lnblwiOlwiNWU1MDM4NjVcIn0iLCJyIjoiaHR0cHM6Ly9zaC5saWFuamlhLmNvbS9lcnNob3VmYW5nLyIsIm9zIjoid2ViIiwidiI6IjAuMSJ9; _jzqb=1.8.10.1589212040.1',
         'Host': 'sh.lianjia.com',
         'Referer': 'https://sh.lianjia.com/ershoufang/',
         'Sec-Fetch-Dest': 'document',
         'Sec-Fetch-Mode': 'navigate',
         'Sec-Fetch-Site': 'same-origin',
         'Sec-Fetch-User': '?1',
         'Upgrade-Insecure-Requests': '1',
         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
     }





def get_html(start_url):
    try:
        r = requests.get(start_url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
        print(r.status_code)
    except:
        return "抓取失败"


def fill_list(list,html):
    print("")

def print_list(list):
    print("")

def main():
    depth = 3
    info_list = []
    for i in range(depth):
        try:
            url = start_url + "pg" + i
            html = get_html(start_url)
            fill_list(info_list,html)
        except:
            return "爬取失败"
    print_list(info_list)


main()

# xpath爬取：
# 价格：//div[@class="totalPrice"]
# 单价：//div//div[@class='unitPrice']
# 名字：//div//div//a[@class='title']
# 编号：//div/div/div/a[@class='title']/@data-housecode
# 位置：//div//div[@class='positionInfo']
# 属性：//div//div[@class='houseInfo']
# 关注：//div//div[@class='followInfo']
