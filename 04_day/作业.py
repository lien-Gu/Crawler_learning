import requests
from bs4 import BeautifulSoup
from time import sleep
def spider_01():
    url0='http://zqrb.com.cn'
    url=url0+'/yaowen/'
    v_response=requests.get(url)
    bs1=BeautifulSoup(v_response.text,'lxml')
    tag=bs1.find_all('div',{'class':'pd_list02'})
    news_urls=[]
    for i in tag:
        a=i.find('a')
        news_urls.append(url0+a.attrs['href'])
        # print(url0+a.attrs['href'])
    return news_urls
def spider_02(news_urls):
    for news_url in news_urls:
        # sleep(0.5)
        m_response=requests.get(news_url)
        m_response.encoding='utf-8'
        bs2=BeautifulSoup(m_response.text,'lxml')
        title=bs2.find('h1').text
        time,source=bs2.find('div',{'class':'metadata'}).text.split('\n')
        # source=bs2.find().text
        content=bs2.find('div',{'class':'content'}).text
        # print(source)
        # print(title,time,source,content)
        t1=time.replace('\n','').replace('\r','')
        s1=source.replace('\n','').replace('\r','').replace(',','')
        c1=content.replace('\n','').replace('\r','')
        with open('zqrb_news.csv','a',encoding='utf-8-sig') as file:
            file.write(title+','+t1+','+s1+','+c1+'\n')
urls=spider_01()
spider_02(urls)

#全局变量放入函数中需要global声明
'''多页数据爬取
   http://www.zqrb.com.cn/yaowen/list_1_200.html
   for page in range(100):
       url='http://www.zqrb.com.cn/yaowen/list_1_'+i+'.html'
       urls=spider_01()
       spider_02(urls)
'''
