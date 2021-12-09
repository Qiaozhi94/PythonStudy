import requests
import csv
import time
from lxml import etree
import random

# hd = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
#     'Cache-Control': 'max-age=0',
#     'Connection': 'keep-alive',
#     'Host': 's.weibo.com',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-User': '?1',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
#     }

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'SINAGLOBAL=7856788391588.121.1573966402006; UM_distinctid=1701b69e628a1a-0a9b67537deda7-39617b0f-13c680-1701b69e629aa9; _s_tentry=-; Apache=2850399379467.896.1590030520551; ULV=1590030520579:12:3:2:2850399379467.896.1590030520551:1589990702648; login_sid_t=804722beb5201f13d75216740f9bee9f; cross_origin_proto=SSL; WBtopGlobal_register_version=fd6b3a12bb72ffed; appkey=; un=georgel.supertramp@gmail.com; SSOLoginState=1590053006; un=georgel.supertramp@gmail.com; wvr=6; UOR=www.goturkey.cn,widget.weibo.com,www.google.com; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWeBEXxoXcdhLurH.vWUHTR5JpX5K2hUgL.FoMXSKnpS0eXe022dJLoIpD7wPxQdcRLxKBLBonL1KeLxKML1KBLBKn4S5tt; ALF=1621827876; SCF=AkUjm1YB8UiNoAbNkuim_FcdjdNBmlFhOv5dti1DEpiWA7u0RU4UQbpkBZllv3vGEQ2atlp_nKBW8bDMSJdjYNE.; SUB=_2A25zzZ31DeRhGeFK7loQ9y3IyD2IHXVQuog9rDV8PUNbmtAKLWrlkW9NQy1HU2IHkLG-E-SxDWMXcktYK1hTeTPY; SUHB=0A0ZOFEfx9XPEa; webim_unReadCount=%7B%22time%22%3A1590291899817%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A14%2C%22msgbox%22%3A0%7D; WBStorage=42212210b087ca50|undefined',
    'Host': 's.weibo.com',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }




url = "https://s.weibo.com/top/summary"

weibo_rankings = []
# session_url = "https://s.weibo.com/top/summary"
# session = requests.Session()
# session.get(session_url,headers=hd)

# r = session.get(url,headers=hd,timeout=30)
# r.raise_for_status()
# r.encoding=r.apparent_encoding
# print(r.status_code)
# tree = etree.HTML(r.text)
# hots = tree.xpath("//div[@id='pl_top_realtimehot']//tbody/tr")


r = requests.get(url,headers=headers,timeout=30)
r.raise_for_status()
r.encoding=r.apparent_encoding
print(r.status_code)
print(r.text)
tree = etree.HTML(r.text)
hots = tree.xpath("//div[@id='pl_top_realtimehot']//tbody/tr")



for hot in hots:
    try:
        ranktop = hot.xpath(".//td[2]/span/text()")[0]
    except IndexError:
        ranktop =""
    try:
        type = hot.xpath(".//td[3]/i/text()")[0]
    except IndexError:
        type =""
    try:
        num = hot.xpath(".//td[@class='td-01 ranktop']//text()")[0]
    except IndexError:
        num ="0"
    keywords = hot.xpath(".//td[@class='td-02']/a/text()")
    time.sleep(random.randint(0, 5))
    for keyword in keywords:
        hd_each = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
                }

        url_each = "https://s.weibo.com/weibo/%23" + keyword + "%23"
        print(url_each)
        # session_each = requests.Session()
        # session.get(url_each,headers=hd_each,timeout=30)
        r_each = requests.get(url_each,headers=headers,timeout=30)
        r_each.raise_for_status()
        r_each.encoding='utf-8'
        # print(r_each.status_code)
        tree_each = etree.HTML(r_each.text)
        try:
            read = tree_each.xpath("//div[@id='pl_topic_header']//div[@class='total']/span[1]/text()")[0]
        except IndexError:
            read = ""
        try:
            discuss = tree_each.xpath("//div[@id='pl_topic_header']/div[1]/div/div[2]/span[2]/text()")[0]
        except IndexError:
            discuss = ""
        try:
            avator = tree_each.xpath("//div[@class='info']/div[1]/a[1]/text()")[0]
        except IndexError:
            avator = ""
        try:
            tag = tree_each.xpath("//div[@id='pl_feed_main']//a[@class='tag']/text()")[0]
        except IndexError:
            tag = ""
        try:
            area = tree_each.xpath("//div[@id='pl_feed_main']//a[@class='tag']/text()")[1]
        except IndexError:
            area = ""

        weibo_rankings.append([num, keyword,type,ranktop,read,discuss,avator,tag,area])
        time.sleep(random.randint(0, 10))
        print(weibo_rankings)

timestr = time.strftime("%Y.%m.%d.%H.%M.%S",time.localtime())
weibo_csv = 'weibo_rank'+ timestr + '.csv'
try:

    with open(weibo_csv,"w",encoding='utf-8-sig',newline='') as fp:
        writer = csv.writer(fp)
        header = ['排名', '名称', '类型', '热度','阅读量','讨论量','主持人',"标签","地区"]
        writer.writerow(header)
        for line in weibo_rankings:
            writer.writerow(line)
    print("爬取成功！")
except:
    print("爬取失败！")