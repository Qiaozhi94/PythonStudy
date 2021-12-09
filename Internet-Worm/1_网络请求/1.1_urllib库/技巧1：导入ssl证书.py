#通过导入ssl模块把证书改成不用验证就可以解决使用urllib.urlopen显示urllib.error.URLError的错误
#方法如下

import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
response = urllib.request.urlopen('https://www.python.org')
print(response.read().decode('utf-8'))