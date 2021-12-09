

import requests
from lxml import etree
from aip import AipOcr
import os


def gethtmltext(url):
    r = requests.get(url, headers=headers, timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    # print(r.text)
    return r.text


def parsepage(html):
    tree = etree.HTML(html)
    lis = tree.xpath("//div[@id='content']/div[3]/table//tr")
    for li in lis:
        try:
            historical_ranking = li.xpath("./td[2]/text()")[0]
        except IndexError:
            continue

        # print(historical_ranking)
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

        # return r_image.content
        title.append(movie_name)
        print(title)





# def saveimage(img):
#     folder_path = './pictures'
#
#     if os.path.exists(folder_path) == False:
#         os.makedirs(folder_path)
#
#     with open("1.png", "wb") as f:
#         f.write(img)


if __name__ == '__main__':
    title = []
    money = []
    url = "http://58921.com/alltime"
    headers = {
        'Cookie': 'DIDA642a4585eb3d6e32fdaa37b44468fb6c = c7rlb1la0qdkfngeghjeh0le35; Hm_lvt_e71d0b417f75981e161a94970becbb1b = 1591596272; Hm_lpvt_e71d0b417f75981e161a94970becbb1b = 1591596281',
        'User-Agent': 'Mozilla / 5.0(Macintosh; Intel Mac OS X 10_15_5) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 83.0.4103.61 Safari / 537.36'
    }
    html = gethtmltext(url)

    parsepage(html)
