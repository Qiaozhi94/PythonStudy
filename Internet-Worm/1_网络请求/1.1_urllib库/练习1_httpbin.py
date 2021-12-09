import urllib.request
import ssl
import string

ssl._create_default_https_context = ssl._create_unverified_context

def data_url():
    url = "http://httpbin.org"



    end_url = urllib.parse.quote(url,safe=string.printable)
    response = urllib.request.urlopen(end_url)
    data = response.read().decode("utf-8")
    print(data)

data_url()