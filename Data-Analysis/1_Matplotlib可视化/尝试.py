

import requests
from lxml import etree
from aip import AipOcr
import os

title = []
money = []
url = "http://58921.com/alltime"
headers = {
    'Cookie': 'DIDA642a4585eb3d6e32fdaa37b44468fb6c = c7rlb1la0qdkfngeghjeh0le35; Hm_lvt_e71d0b417f75981e161a94970becbb1b = 1591596272; Hm_lpvt_e71d0b417f75981e161a94970becbb1b = 1591596281',
    'User-Agent': 'Mozilla / 5.0(Macintosh; Intel Mac OS X 10_15_5) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 83.0.4103.61 Safari / 537.36'
}


r = requests.get(url, headers=headers, timeout=30)
r.raise_for_status()
r.encoding = r.apparent_encoding

tree = etree.HTML(r.text)
lis = tree.xpath("//div[@id='content']/div[3]/table//tr")

i = 1
for li in lis:
    try:
        historical_ranking = li.xpath("./td[2]/text()")[0]
    except IndexError:
        continue


    try:
        movie_name = li.xpath("./td[3]/a/text()")[0]
    except IndexError:
        continue

    try:
        year = li.xpath(".//td[7]/text()")[0]
    except IndexError:
        continue

    try:
        money_url = li.xpath(".//td[4]/img/@src")[0]
    except IndexError:
        continue

    # print(money_url)
    r_image = requests.get(money_url)
    # print(r_image.content)

    folder_path = './pictures'
    path_new = folder_path + '/' + str(i) + ".png"

    if os.path.exists(folder_path) == False:
        os.makedirs(folder_path)

    with open(path_new, "wb") as f:
        f.write(r_image.content)

    i += 1
    print('爬取成功')
