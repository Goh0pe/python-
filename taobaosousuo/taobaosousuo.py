import requests
import re

#获取页面
def getHTMLText(url):
	try:
		r = requests.get(url,timeout = 30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return ""

#处理页面
def parsePage(ilt,html):
	try:
		#'\'符号是为了获取特殊符号如 " :
		#获取价格
		plt=re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
		#获取名称  最小匹配
		tlt=re.findall(r'\"raw_title\"\:\".*?\"',html)
		for i in range(len(plt)):
			#目的是去无用部分  eval去双引号  split以：分割  [1]取分割后后半部分
			price = eval(plt[i].split(":")[1])
			title = eval(tlt[i].split(":")[1])
			ilt.append([price,title])
		ilt.sorted(key=lambda s: s[0])
	except:
		print("")

#打印结果
def printGoodsList(ilt):
	tplt = "{:4}\t{:8}\t{:16}"
	print(tplt.format("序号","价格","商品名称"))
	count = 0
	for g in ilt:
		count += 1
		print(tplt.format(count,g[0],g[1]))

def main():
	goods = "书包"
	depth = 2
	start_url = 'https://s.taobao.com/search?q=' + goods
	infoList = []
	for i in range(depth):
		try:
			#str函数功能时将对象转换成其'字符串'表现形式，如果不传入参数，将返回空字符串。
			url = start_url + '&s=' + str(44*i)
			html = getHTMLText(url)
			parsePage(infoList,html)
		except:
			continue
	printGoodsList(infoList)

main()