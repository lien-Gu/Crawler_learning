#ajax---js局部刷新，异步交互---XHR
# 不用form提交，ajax提交
'''
get地址构成：主机：端口/地址？参数名：参数值&参数名：参数值。。。
http://app.cnstock.com/api/waterfall?callback=jQuery1910752567803697797_1593478514351
&colunm=qmt-sns_yw
&page=3
&num=10
&showstock=0
&_=1593478514354
'''

import requests
jz_urls=[]
for i in range(1,5):
    url='http://app.cnstock.com/api/waterfall?' \
        'callback=jQuery1910752567803697797_1593478514351&colunm=qmt-sns_yw' \
        '&page='+str(i)+'&num=10&showstock=0&_=1593478514356'
    jz_urls.append(url)
# print(jz_urls)
# 加载请求头,字典格式
cn_headers={'Referer':'http://news.cnstock.com/news/sns_yw/index.html'}

v_res=requests.get(jz_urls[0],headers=cn_headers)
# print(v_res.text)
# print(type(v_res.text))
# 只要该数据：{"msg":"success","code":"200","data":{"date":"2020-06-30"。。。

'''
split函数
str1=v_res.text.split("(",1)[1].split(')',1)[0]

index函数
content=v_res.text
start=content.index('(')+1
end=content.index(')')
str1=content[start:end]
'''
'''
# 正则表达式
. 任意字符，除了换行符
* 0次或任意次
  .* aa
  .*? 匹配任意字符
'''
import re #python正则表达式
content=v_res.text
re_content=re.findall('\((.*?)\)',content)[0]
# print(re_content)

# python的json处理
import json
# print(re_content[])
# json库，目的将字符型转化而可用json访问的类
json_content=json.loads(re_content)
print(json_content['data'])










