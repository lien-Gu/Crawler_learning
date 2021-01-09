#引入库
# pip install requests
import requests

url='https://www.baidu.com/'
#获取url地址
v_response=requests.get(url)
# print(v_response)#响应对象
print(v_response.text)

url='https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'
v_response=requests.get(url)
print(v_response)
print(v_response.content)



