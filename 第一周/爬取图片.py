import requests
import os
url="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1532603999414&di=95dbfa2c72c966a31b82cbc1df5b245e&imgtype=0&src=http%3A%2F%2Fimgsrc.baidu.com%2Fimgad%2Fpic%2Fitem%2Fbf096b63f6246b60553a62a0e1f81a4c510fa22a.jpg"
root="H://学习/网络/python网络爬虫/图片/"
path = root + url.split('%')[-1] #获取网址最后一部分
try:
    if not os.path.exists(root): #如果不存在目录
        os.mkdir(root)
    if not os.path.exists(path): #如果不存在图片
        r=requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close();
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")
