import requests

# 爬取地址
url="https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png"
#获取地址对象--与爬取地址建立联系
v_response=requests.get(url)
#获取二进制数据
v_data=v_response.content
# print(v_response.content)
with open("bd.png",'wb') as f1:
    f1.write(v_data)








