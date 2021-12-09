import requests
import csv
import time
from lxml import etree
import random

url = "https://www.zhihu.com/hot"

hd = {
    'authority': 'www.zhihu.com',
    'method': 'GET',
    'path': '/hot',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'cookie': '_zap=1f83c031-59f2-41c3-a841-4417c8fb03dd; d_c0="APAgSFznWBCPTrSJrmk9VpkbQ5NpeKELNo0=|1573624136"; __utmz=51854390.1576464075.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/follow; __utma=51854390.799918535.1576464075.1576464075.1576992956.2; __utmv=51854390.100-1|2=registration_date=20131124=1^3=entry_date=20131124=1; _ga=GA1.2.799918535.1576464075; z_c0="2|1:0|10:1582722434|4:z_c0|92:Mi4xbi04akFBQUFBQUFBOENCSVhPZFlFQ1lBQUFCZ0FsVk5ncnREWHdEdUQ0UDl4MVZ5Vm13MUNBdW9mSFRTXzBSNVpn|3da6c75eb7e96f63926969cc641a9bbd664f896fdf5b699fcb371e4b2b201ecf"; tshl=; _xsrf=c45e6341-4aa3-4352-a21f-827f6df29e05; q_c1=ace8797936ff46c883f033abf68702f3|1589636544000|1573632306000; _gid=GA1.2.1846027721.1589792933; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1589706287,1589792517,1589792963,1589793265; BAIDU_SSP_lcr=https://www.google.com/; SESSIONID=d6V9IluN6vDRqrW6qYsAndpad2kkLnpaFIAFiNaQNN1; JOID=V18QBU0dwOA-nFSqRx7xfnAtgOJWe_S1B9Y63QootKZv7SX_c--QIWOdVKtEaQWNM9ho8EPS6P1hD7jwmosVM_w=; osd=W14RB0wRweE8nVirRhzwcnEsguNaevW3Bto73AgpuKdu7yTzcu6SIG-cValFZQSMMdlk8ULQ6fFgDrrxlooUMf0=; tst=h; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1589793293; KLBRSID=fe0fceb358d671fa6cc33898c8c48b48|1589793293|1589792930',
    'referer': 'https://www.google.com/',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }






zhihu_hotTopics =[]

r = requests.get(url,headers=hd,timeout=30)
r.raise_for_status()
print(r.status_code)
r.encoding=r.apparent_encoding
html = etree.HTML(r.text)
hot_topics = html.xpath("//*[@id='TopstoryContent']/div/div/div[2]//section")

for hot_topic in hot_topics:
    num = hot_topic.xpath(".//div[1]/div/text()")[0]
    title = hot_topic.xpath(".//div[2]/a/h2/text()")[0]
    hot_star = hot_topic.xpath(".//div[2]/div/text()")[0]
    links = hot_topic.xpath(".//div[2]/a/@href")

    for link in links:
        # print(link)
        r_each = requests.get(link,headers=hd,timeout=30)
        r_each.raise_for_status()
        r.encoding=r.apparent_encoding
        html_each = etree.HTML(r_each.text)

        try:
            focus_num = html_each.xpath("//div[@class='NumberBoard-itemInner']/strong/text()")[0].strip()
            new_focus_num = focus_num.replace(",","")
            browse_num = html_each.xpath("//div[@class='NumberBoard-itemInner']/strong/text()")[1].strip()
            new_browse_num = browse_num.replace(",","")
            answers = html_each.xpath('//*[@id="QuestionAnswers-answers"]/div/div/div/div[1]/h4/span/text()')[0]
        except:
            new_focus_num = "/"
            new_browse_num= "/"
            answers = "/"



        tags = html_each.xpath("//div[@id='root']//div[@class='Popover']/div/text()")
        print(type(num))
        zhihu_hotTopics.append([num, title, hot_star, new_focus_num, new_browse_num, tags, link])
        time.sleep(random.randint(0,2))
        print(zhihu_hotTopics)

# localtime = time.asctime(time.localtime(time.time()))
# zhihu_hotTopics.append([localtime])
# print(zhihu_hotTopics)
#
timestr = time.strftime("%Y.%m.%d.%H.%M.%S",time.localtime())
zhihu_csv = 'zhihu hottopics'+ timestr + '.csv'
try:

    with open(zhihu_csv,"w",encoding='utf-8-sig',newline='') as fp:
        writer = csv.writer(fp)
        header = ['排名', '名称', '热度', '关注人数','浏览量','标签','链接']
        writer.writerow(header)
        for line in zhihu_hotTopics:
            writer.writerow(line)
    print("爬取成功！")
except:
    print("爬取失败！")




