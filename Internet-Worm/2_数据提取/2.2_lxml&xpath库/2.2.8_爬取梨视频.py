import requests
from lxml import etree
import time
import csv

original_url = "https://www.pearvideo.com/"

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '__secdyid=5afb1a77612977cea85451c67befda0b0154134073bfabc1021589979543; PEAR_UUID=cbdac409-2195-4393-a875-8f64a5bcf4aa; _uab_collina=158997954504219805222075; UM_distinctid=172322a82085be-04d3fcb9a1fc9-30667d00-1fa400-172322a8209a0f; JSESSIONID=F6DBB1A821F83FB6C08DA2A1434FCA75; PV_WWW=srv-pv-prod-portal1; CNZZDATA1260553744=1718556958-1589976427-https%253A%252F%252Fwww.google.com%252F%7C1590587108; Hm_lvt_9707bc8d5f6bba210e7218b8496f076a=1589979546,1590030678,1590587513; p_h5_u=E8AA537D-FD1F-4CD4-9961-3CD2371CE344; __ads_session=ldSV/lULewkb/x9YoAA=; Hm_lpvt_9707bc8d5f6bba210e7218b8496f076a=1590587739',
    'Host': 'www.pearvideo.com',
    'Referer': 'https://www.google.com/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }

r = requests.get(original_url,headers=headers,timeout=30)
r.raise_for_status()
r.encoding = r.apparent_encoding
print(r.status_code)
# print(r.text)
tree = etree.HTML(r.text)
link = tree.xpath("//div[@id='vervideoTlist']/div/div/div/a/@href")[0]

url = original_url + link

r_1 = requests.get(url,headers=headers,timeout=30)
r_1.raise_for_status()
r_1.encoding=r_1.apparent_encoding
print(r_1.status_code)
tree_1 = etree.HTML(r_1.text)
video = tree_1.xpath("//div[@id='JprismPlayer']//video//@src")
print(video)



