import requests

url="https://www.amazon.cn/dp/B00M2DL02A/ref=sr_1_42?ie=UTF8&qid=1532590909&sr=8-42&keywords=python"

try:
    #修改User-agent来使亚马逊接受  Mozilla/5.0是一些浏览器的标识
    kv={'User-agent':'Mozilla/5.0'}
    r = requests.get(url,headers = kv,timeout=30)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text[:5000])
except:
    print("产生异常")
