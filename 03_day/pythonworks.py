import requests
url="http://contentcms-bj.cdn.bcebos.com/cmspic/199379e0ac30635b49a586749f199c25.jpeg?x-bce-process=image/crop,x_0,y_349,w_2000,h_1342"
v_response=requests.get(url)
# print(v_response)
v_data=v_response.content
# print(v_data)
with open("picture1.jpeg",'wb') as f1:
    f1.write(v_data)