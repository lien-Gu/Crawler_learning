import requests
from  bs4 import  BeautifulSoup
from time import sleep

# 第一次爬取
def first_spider():
    url="http://news.cnstock.com/news/sns_yw/index.html"
    v_response=requests.get(url)
    bs=BeautifulSoup(v_response.text,'lxml')
    tag1=bs.find_all('li',{'class','newslist'})
    news_urls=[]
    for i in tag1:
        a=i.find('a')
        news_urls.append(a.attrs['href'])
    return news_urls

# 第二次爬取
def second_spider(news_urls):
    for news_url in news_urls:
        # sleep(0.5)#自己调节
        m_response=requests.get(news_url)
        bs1=BeautifulSoup(m_response.text,'lxml')
        title=bs1.find('h1',{'class':'title'}).text
        time=bs1.find('span',{'class':'timer'}).text
        source=bs1.find('span',{'class':'source'}).text
        content = bs1.find('div', {'id': 'qmt_content_div'}).text
        # print(title,time,source,content)
        # 数据格式：元素，元素，元素。。。
        #           元素，元素，元素
        # 逗号分割，回车换行

        # content内容处理，去掉回车
        c1=content.replace('\n','').replace('\r','')
        with open('cnstock_news.csv','a',encoding='utf-8-sig') as file:
            file.write(title+','+time+','+source+','+c1+'\n')


r_news_urls=first_spider()
second_spider(r_news_urls)


#.csv



