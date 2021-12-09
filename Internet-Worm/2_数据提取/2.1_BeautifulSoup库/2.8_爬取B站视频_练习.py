import requests
from bs4 import BeautifulSoup
import bs4
import re

url = "https://search.bilibili.com/all?keyword="
url_new = url +"美女"
hd = {
            'authority': 'api.bilibili.com',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
            'accept': 'application/json, text/plain, */*',
            'sec-fetch-site': 'same-site',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://message.bilibili.com/pages/nav/index_new_pc_sync',
            'accept-language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
            'cookie': "_uuid=7880DA02-5DDC-5D7B-AEB4-1466AE7EDF4A88834infoc; buvid3=D5B65A83-B426-40A8-8097-7CDF6558EADC155822infoc; LIVE_BUVID=AUTO1215737144894295; sid=j6u1jmaw; CURRENT_FNVAL=16; stardustvideo=1; rpdid=|(umJJYRRm||0J'ul~J~uRlJ~; laboratory=1-1; DedeUserID=16184361; DedeUserID__ckMd5=0e54ac8ee7948c85; SESSDATA=bb29bdce%2C1599883169%2C12d58*31; bili_jct=8d73ddaf7b42debe2e927b5b6179ae51; CURRENT_QUALITY=80; PVID=1; bp_video_offset_16184361=387784020114110285; bp_t_offset_16184361=387994761267665568; bfe_id=1bad38f44e358ca77469025e0405c4a6",
        }

def get_html_text(url):
    try:
        r = requests.get(url_new, headers =hd, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "False"

def fill_list(list,html):
    soup = BeautifulSoup(html, "html.parser")
    for li in soup.find("ul").children:
        print(li)
        #if isinstance(li, bs4.element.Tag):
            #lis = li("a")  #tr("td")与tr.find_all("td")等价
            #list.append([lis[0].string, lis[1].string, lis[2].string])



#def print_list(list,num):
    #tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    #print(tplt.format("排名", "学校名称", "地区", chr(12288)))
    #for i in range(num):
        #u = list[i]
        #print(tplt.format(u[0], u[1], u[2], chr(12288)))




def main():
    info = []
    html = get_html_text(url)
    fill_list(info,html)
    #print_list(info,5)

main()

