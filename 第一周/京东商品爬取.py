import requests
import 通用代码框架 as a



def main():
    url="https://item.jd.com/7343325.html"
    txt=a.getHTMLText(url)
    print(txt)


main()
