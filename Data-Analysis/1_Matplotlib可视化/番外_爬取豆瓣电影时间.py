import requests
from lxml import etree
import time
import random


url = "https://movie.douban.com/top250?start="


hd1 = {
    'Cookie': 'bid=6hSR-_LnVfo; douban-fav-remind=1; ll="108169"; push_doumail_num=0; _vwo_uuid_v2=D0D7A5503DEE818EE9ED8C2C8AB7AEB2F|d29d114b1fa775dcc53e38b6f2d49449; gr_user_id=9080cc46-5fcd-499e-9634-3361236557b7; __gads=ID=1ad919f64794e7af:T=1573972611:S=ALNI_MbfQdJGdbZ7UJWXs66dXmGF4xschQ; push_noty_num=0; douban-profile-remind=1; _ga=GA1.2.630973614.1573719791; trc_cookie_storage=taboola%2520global%253Auser-id%3D326278ea-22ba-4776-b6e7-b6422ed5c145-tuct4c519d0; __yadk_uid=LLkmYKwRB5GTlTv1BKsumbUvEGEUJF2g; __utmv=30149280.20719; __utmc=30149280; __utmc=223695111; viewed="25867570_26800951_35005667_4912723_25803380_6523921_10761575_1451694_10511414_34781804"; dbcl2="207192962:sU1rcAa96Ik"; ck=K8xU; ap_v=0,6.0; __utma=30149280.630973614.1573719791.1589439855.1589444510.180; __utmb=30149280.0.10.1589444510; __utmz=30149280.1589444510.180.33.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utma=223695111.752048804.1573998256.1589439969.1589444510.81; __utmb=223695111.0.10.1589444510; __utmz=223695111.1589444510.81.79.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1589444510%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_id.100001.4cf6=58775c79e8af8b24.1573998256.79.1589444510.1589440016.; _pk_ses.100001.4cf6=*',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}

top250_list = []
count = 1
for i in range(10):
    url_final = url + str(25*i)
    try:
        r = requests.get(url_final,headers=hd1, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        # print(r.status_code)
        html = etree.HTML(r.text)
        movies = html.xpath("//ol/li/div[@class='item']")
            # print(movies)

        for movie in movies:
                link = movie.xpath(".//div[@class='hd']/a/@href")[0]

                hd2 = {
                    'Cookie': 'bid=6hSR-_LnVfo; douban-fav-remind=1; ll="108169"; push_doumail_num=0; _vwo_uuid_v2=D0D7A5503DEE818EE9ED8C2C8AB7AEB2F|d29d114b1fa775dcc53e38b6f2d49449; gr_user_id=9080cc46-5fcd-499e-9634-3361236557b7; __gads=ID=1ad919f64794e7af:T=1573972611:S=ALNI_MbfQdJGdbZ7UJWXs66dXmGF4xschQ; push_noty_num=0; douban-profile-remind=1; _ga=GA1.2.630973614.1573719791; trc_cookie_storage=taboola%2520global%253Auser-id%3D326278ea-22ba-4776-b6e7-b6422ed5c145-tuct4c519d0; __yadk_uid=LLkmYKwRB5GTlTv1BKsumbUvEGEUJF2g; __utmv=30149280.20719; viewed="2248893_32567702_34918516_26916640_27074704_35003679_25867570_26800951_35005667_4912723"; __utmc=30149280; dbcl2="207192962:0EdSKsjH2ds"; ck=2r7M; ap_v=0,6.0; __utmz=30149280.1591766892.197.38.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmc=223695111; __utmz=223695111.1591766892.88.85.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1591773505%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_id.100001.4cf6=58775c79e8af8b24.1573998256.87.1591773505.1591766899.; _pk_ses.100001.4cf6=*; __utma=30149280.630973614.1573719791.1591766892.1591773505.198; __utmb=30149280.0.10.1591773505; __utma=223695111.752048804.1573998256.1591766892.1591773505.89; __utmb=223695111.0.10.1591773505',
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
                }

                r_each = requests.get(link,headers=hd2,timeout=30)
                r_each.raise_for_status()
                r_each.encoding=r_each.apparent_encoding
                tree = etree.HTML(r_each.text)
                runtime = tree.xpath("//div[@id='info']/span[@property='v:runtime']/@content")[0]

                runtime_str = runtime.encode('utf-8')
                runtime_int = int(runtime_str)

                top250_list.append(runtime_int)

                time.sleep(random.randint(1,4))
                print(count)
                count += 1


    except:
        print("爬取失败")

print(top250_list)
print("爬取成功")
