import requests
import json
from bs4 import BeautifulSoup

def getRes(url):
    res=requests.get(url)
    return res.text

url='https://www.yicai.com/api/ajax/getjuhelist?action=news&page=2&pagesize=25'
news=getRes(url)
# print(res.text)
js_news=json.loads(news)
# print(js_news)
for i in js_news:
    title=i['NewsTitle']
    time=i['LastDate']
    news_url='https://www.yicai.com'+i['url']
    news1=getRes(news_url)
    bs=BeautifulSoup(news1,'lxml')
    content=bs.find('div',{'class':'m-txt'}).text
    # print(content)
    c1=content.replace('\r','').replace('\n','').replace('\xa0','')
    with open('zuoye2.csv','a',encoding='utf-8-sig') as file:
        # file.write(title + ',' + time +'\n')
        file.write(title+','+time+','+c1+'\n')