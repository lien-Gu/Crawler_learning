import requests
from bs4 import BeautifulSoup

url="http://news.baidu.com"
r=requests.get(url)
# 获取源代码
# print(r.text)
# pip install bs4
# pip install lxml

# 解析
# BeautifulSoup(网页源码,解析器)
# 解析器：lxml 需要安装
#         html.parser 系统自带
# 创建解析器的实例对象
bs=BeautifulSoup(r.text,'lxml')#BeautifulSoup(r.text,'html.parser')
# print(bs)
# 解析具体内容

v_title=bs.select("#pane-news > div > ul > li.hdline0 > strong > a")[0].text #.get_text()
# print(v_title)
v_title=bs.select("#guonei > div.l-left-col.col-mod > ul:nth-child(1) > li.bold-item > a")
# v_title=bs.select("#guojie > div.l-left-col.col-mod > ul:nth-child(1) > li.bold-item > a")
print(v_title)


