
'''
json:轻量的数据格式
    {key:value,key:value,...}
    {key:[{},{},...]}
    j1['chainType']
    应用场景：
        数据库： zs 23 nv
                 li 34 nan
                 ww 22 nv
                 ...
        查询学生信息
          后台：select数据
                s_array=[]
                for遍历数据，一行一行
                 s1={'uname':'zs','uage':23,'usex':'nv'}
                 s_array.append(s1)
              数组+json
              [{'uname':'zs','uage':23,'usex':'nv'},{'uname':'li','uage':34,'usex':'nan'},...]

          前台：接受 数组+json
'''
import requests

# url='https://www.yicai.com/news'
# v_response=requests.get(url)


# 每条新闻的链接地址
def get_secondurl(yc_urls):
    secondurls=[]
    for surl in yc_urls:
        source=requests.get(surl)
        # 调取json格式，等价于json.loads()
        j_source=source.json()
        for item in j_source:
            # print(item['url'])
            #地址拼接
            secondurls.append('https://www.yicai.com'+item['url'])
    return secondurls

# 根据二级地址爬取详细新闻数据
def get_newsdetail(secondurls):
    for url in secondurls:
        pass

# 主程序
def main():
    yc_urls = []
    for i in range(1, 3):
        url = 'https://www.yicai.com/api/ajax/getjuhelist?action=news&page=' + str(i) + '&pagesize=25'
        yc_urls.append(url)
    secondurls = get_secondurl(yc_urls)
    get_newsdetail(secondurls)











