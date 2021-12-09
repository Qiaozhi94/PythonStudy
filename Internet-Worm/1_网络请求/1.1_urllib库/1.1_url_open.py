import urllib.request

def load_data():
    url = "http://www.douban.com/"
    response = urllib.request.urlopen(url)
    print(response)

load_data()

