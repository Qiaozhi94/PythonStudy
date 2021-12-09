import requests
import time
import random
from lxml import etree

# 反爬机制十分高明，采用的是css反爬系统，学习成本很高，所以打算先放着之后在慢慢掌握

def getHTMLtext(url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Cookie': 'fspop=test; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; _lxsdk_cuid=17273ed4339c8-0d4440db2ad1b4-1b396257-1fa400-17273ed4339c8; _lxsdk=17273ed4339c8-0d4440db2ad1b4-1b396257-1fa400-17273ed4339c8; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1591082829; _hc.v=eade2558-cf86-0346-b98c-528e4fadf9b5.1591082829; dplet=5340628da1334932dd20b580ce38a743; dper=63105ed9f53f1b2c0fe376d1be7da4f2c9904f455065b5c992a6810313d081f5cdcb9269bd657c2b739bd697b99ff33f366b58da13763e6f10dfe0a6f6030b9a98f25ece62cad7503ba59595117a22542f25770ec4f461b9625ce4eae8578b8c; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_5794144511; ctu=bb10bf4f9c796fb762a0c2a25848de165a62e45427b13a6d6deffe6e1331b956; cy=1; cye=shanghai; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1591085690; _lxsdk_s=1727418b8c8-2cb-c7-60b%7C%7C64',
        'Host': 'www.dianping.com',
        'Referer': 'http://www.dianping.com/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
    }

    r = requests.get(url, headers=headers, timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.status_code)
    # print(r.text)
    return r.text

def getDetail():

    tree = etree.HTML(HTML)
    hotpots = tree.xpath("//div[@id='shop-all-list']/ul/li")
    for hotpot in hotpots:
        name = hotpot.xpath(".//div[2]/div[1]/a/h4/text()")[0]
        ranking = hotpot.xpath(".//div[@class='comment']/div[1]/div[2]/text()")[0]
        comment = hotpot.xpath(".//div[2]/div[2]/a[1]/b/text()")[0]
        print(name)
        print(ranking)
        print(comment)

        time.sleep(random.randint(0, 2))



if __name__ == '__main__':

    for i in range(1,2):
        original_url = "http://www.dianping.com/shanghai/ch10/g110"
        url = original_url + "p" + str(i)
        time.sleep(random.randint(3, 6))
        HTML = getHTMLtext(url)

