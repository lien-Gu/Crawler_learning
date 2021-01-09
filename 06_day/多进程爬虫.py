import requests
from lxml import etree
from time import sleep

url='https://bj.ke.com/ershoufang/'
# 前端框架--jQuery
v_response=requests.get(url).text
# print(v_response)
# 解析
e_html=etree.HTML(v_response)
# print(e_html)
'''
# xpath
元素索引从1开始
提取某个标签的属性 a/@title  <a title=''...
//*[@id="beike"]/div[1]/div[4]/div[1]/div[4]/ul/li[11]/div/div[1]/a
* 通配符=body
//查询多个元素
a/text() 提取标签文本  <a>XXXXXX</a>
地址、小区名称、总价格、房屋户型、建筑面积、小区建造时间、平均单价
'''
# source=e_html.xpath('//*[@id="beike"]/div[1]/div[4]/div[1]/div[4]/ul/li[1]/a/@href')
# print(source)
#自定义Xpath 所有标题
s_urls=e_html.xpath('//ul[@class="sellListContent"]//li[@class="clear"]/a/@href')
for s_url in s_urls:
    v1_repsonse=requests.get(s_url).text
    # print(v1_repsonse)
    e1_html=etree.HTML(v1_repsonse)
    # print(e1_html)
    xiaoqu=e1_html.xpath('//div[@class="communityName"]/a[1]/text()')
    dizhi=e1_html.xpath('//div[@class="areaName"]/span[2]//a/text()')
    zongjia=e1_html.xpath('//div[@class="price "]/span[@class="total"]/text()')
    huxing=e1_html.xpath('//div[@class="room"]/div[1]/text()')
    sjianzhu=e1_html.xpath('//div[@class="area"]/div[1]/text()')
    tjianzao=e1_html.xpath('//div[@class="area"]/div[2]/text()')
    danjia=e1_html.xpath('//div[@class="unitPrice"]/span/text()')
    print(xiaoqu,dizhi,zongjia,huxing,sjianzhu,tjianzao,danjia)

'''
ascii
iso-8859-1 java tomcat
gb2312
gbk支持繁体
Big5 台湾
...
unicode
a

utf-8
utf-16
...
'''









