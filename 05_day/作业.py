import requests
import json
from bs4 import BeautifulSoup
from time import sleep

# 由地址获取新闻
def findContent(adr):
    a_res=requests.get(adr)
    bs=BeautifulSoup(a_res.text,'lxml')
    content=bs.find('div',{'id':'qmt_content_div'}).text
    return content


# 加载地址
def getjzurls():
    jz_urls=[]
    for i in range(1,6):
        url='http://app.cnstock.com/api/waterfall?callback=jQuery1910752567803697797_1593478514351&colunm=qmt-sns_yw&page='+str(i)+'&num=10&showstock=0&_=1593478514356'
        jz_urls.append(url)
    return jz_urls
# print(urls)  测试5次加载地址

# 与网站连接加载内容
def getReponse(jz_url):
    jz_header={'Referer':'http://news.cnstock.com/news/sns_yw/index.html'}
    v_res=requests.get(jz_urls[0],headers=jz_header)
    return v_res

# 将获取的一条记录存入文件
def storeRecord(i):
    time = i['dateline']
    title = i['title']
    content = findContent(i['link'])
    t1 = time.replace('\r', '').replace('\n', '')
    c1 = content.replace('\r', '').replace('\n', '')
    with open('zuoye.csv', 'a',encoding='utf-8-sig') as file:
        file.write(title + ',' + t1 + ',' + c1 + '\n')

#取内部数据：标题、时间、内容
def getjzNeirong(jz_url):
    content=getReponse(jz_url).text.split('(')[1].split(')')[0]
    js_content=json.loads(content)
    items=js_content['data']['item']
    # print(items)
    for i in items:
        # print(type(i))
        storeRecord(i)

jz_urls=getjzurls()
# print(len(jz_urls))
for i in range(5):
    res=getReponse(jz_urls[i])
    getjzNeirong(res)
    sleep(0.1)


