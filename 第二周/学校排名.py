import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()#产生异常信息
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "产生异常"


def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):  #tbody的子类型中可能存在字符串  这句的作用是过滤不是标签类型的子类
            tds = tr('td')#将所有tr中的td标签存为列表类型tds
            ulist.append([tds[0].string,tds[1].string,tds[3].string])


def printUnivList(ulist,num):
    tplt="{0:^10}\t{1:{3}^10}\t{2:^10}"#{3}指用第四个变量填充，即用中文空格填充
    print(tplt.format("排名","学校名称","分数",chr(12288)))#chr(12288)是中文空格
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))


def main():
    uinfo = []
    url='http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html=getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20)

main()


