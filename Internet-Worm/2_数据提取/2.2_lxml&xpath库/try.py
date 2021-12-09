import requests
from lxml import etree
import time
from bs4 import BeautifulSoup


url = "https://zh.wikipedia.org/wiki/%E6%9D%B1%E4%BA%AC%E5%B7%A5%E6%A5%AD%E5%A4%A7%E5%AD%B8"

# headers = {
#     'Cookie': 'TY_SESSION_ID=ff4ef4be-fc14-46df-b2a1-229c2ebc418e; lianjia_uuid=01765a98-5297-41f9-b19d-89a7449cf57a; UM_distinctid=170e7a4b5ffb7b-0fe20ca1f284a2-396d7406-13c680-170e7a4b600ab1; _smt_uid=5e708c78.114db2b5; _ga=GA1.2.1647190516.1584434300; Hm_lvt_efa595b768cc9dc7d7f9823368e795f1=1586413493; select_city=310000; CNZZDATA1253492439=646215105-1588040561-https%253A%252F%252Fwww.google.com%252F%7C1590289478; CNZZDATA1254525948=1479450439-1588037718-https%253A%252F%252Fwww.google.com%252F%7C1590288473; CNZZDATA1255633284=1262782669-1588041365-https%253A%252F%252Fwww.google.com%252F%7C1590286239; CNZZDATA1255604082=1745799172-1588039033-https%253A%252F%252Fwww.google.com%252F%7C1590286106; _qzjc=1; _jzqa=1.3759888401518846500.1584434297.1589773272.1590290910.19; _jzqc=1; _jzqx=1.1584434297.1590290910.5.jzqsr=google%2Ecom|jzqct=/.jzqsr=google%2Ecom|jzqct=/; _jzqckmp=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22170e7a4bcdc247-0c752ca4b1a414-396d7406-1296000-170e7a4bcddb75%22%2C%22%24device_id%22%3A%22170e7a4bcdc247-0c752ca4b1a414-396d7406-1296000-170e7a4bcddb75%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24latest_referrer_host%22%3A%22www.google.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; _gid=GA1.2.1450725778.1590290912; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1588042734,1588666427,1588781312,1590290914; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1590291199; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiZjUzOTgyNGYyNjZlODAxYTE1NDc5YmQwYjllZWViNWQyMDg2NjMzOTUyYmFiMDU5YTg1NzhjNWJiZGQyNGE4YTM0MWYyOTZlY2I4NDMzOTBkNGY3MzZjODRmNDYxYWVhYjA1MjM2OGM3MzFmOWY4MDJjYzUwMmRiMmQzOThlOThmN2U2MzI3YTg4MDA4MmE1YTcxZjhmYWJhZDUxMjc3NzFjM2FkZjgyY2RkYjE5NjYxMDc5YWFiODM0NWRmOWJiZWFmNWI0ODBiZWU2YWE2NThiOTY4ZGZiZmQ1YjBjODA0NWI1NjlhN2I4ODAwNDkzNTdiNjhjYTYzNjM5YTI0NGM5YTYwYmNmMDNkOTU3NWMyNTVmZmI2ZjEwZWUzNTMwYzEwMTQ0MTBjZmU3MzhiOGFkNzNiYTY0NjZiY2NhNjdcIixcImtleV9pZFwiOlwiMVwiLFwic2lnblwiOlwiYWE5NDNkNjlcIn0iLCJyIjoiaHR0cHM6Ly9zaC5saWFuamlhLmNvbS9lcnNob3VmYW5nLyIsIm9zIjoid2ViIiwidiI6IjAuMSJ9; _qzja=1.1285165120.1588042706441.1589773272440.1590290910079.1590291179771.1590291199826.0.0.0.85.16; _qzjto=7.1.0; lianjia_ssid=fbb54ff5-9ea9-3527-812f-d2dbcf8c4733; login_ucid=2000000104475969; lianjia_token=2.001200d2e16ed1924c03adfbd0557882a3; lianjia_token_secure=2.001200d2e16ed1924c03adfbd0557882a3; security_ticket=SUYSSzhA2iD3m98nylBIdodEgRwFGrTabWsl8OKWnps83TRlDeSTCQN9DzUYSpoKuG64gsNS/6kJu+UQgHd7dfiHXjhp4fYjKRvaFvxzIIKSC1JFwHJ2R8tVU2FQvBHn5opb//i5XaKORgZ14U2Ec3XSG7HWfJ5fz6ox7F8E46w=',
#     'Host': 'sh.lianjia.com',
#     'Referer': 'https://sh.lianjia.com/',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
#     }


r_each = requests.get(url, timeout=30)
            # print(link)
r_each.raise_for_status()
r_each.encoding = r_each.apparent_encoding
print(r_each.status_code)
html_each = etree.HTML(r_each.text)
plan_each = html_each.xpath("//*[@id='mw-content-text']/div//tr[3]/td/a/img/@src")[0]
print(plan_each)

plan_data = requests.get("http:" + plan_each).content

print(plan_data)

with open("1.jpg","wb") as f:
    f.write(plan_data)


