import requests
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text[:1000]
    except:
        return "产生异常"

url="https://python123.io/ws/demo.html"
demo = getHTMLText(url)
soup = BeautifulSoup(demo,"html.parser")
print(soup)
