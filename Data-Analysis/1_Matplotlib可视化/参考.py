import requests
import os



url1 = "https://img1.doubanio.com/view/photo/l/public/p2593388447.webp"
url2 = "https://timgsa.baidu.com/timg?image&amp;quality=80&amp;size=b9999_10000&amp;sec=1588766788812&amp;di=08018862bda1ebf5e007b80f535b63b2&amp;imgtype=0&amp;src=http%3A%2F%2Fimg1.doubanio.com%2Fview%2Fphoto%2Fl%2Fpublic%2Fp2542950619.jpg"
url3 = "https://image1.ljcdn.com/x-se/hdic-frame/standard_279dcefa-b08c-43d8-9106-dcb6ada585f2.png.1440x1080.jpg"
# r = requests.get(url3)
root = "/Users/georgel./Downloads/"
#path = "/Users/georgel./Downloads/abc.jpg"
path_new = root + url3.split('/')[-1]

try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path_new):
        r = requests.get(url3)
        with open(path_new,"wb") as f:
            print(r.content)
            f.write(r.content)
            f.close()
            print("图片保存成功")
    else:
        print("文件已存在")
except:
    print("图片抓取失败")
