'''
1、阿姆斯特朗数，检测用户输入的数是否为 阿姆斯特朗数
   153=1 3+5 3+3 3

2、输出指定范围内的所有素数
'''
# 2
# import math
# try:
#     scale=int(input("请输入范围"))
# except Exception as ep:#检查是否输入错误
#     print(ep)
#     print("输入错误")
# listnum=[]#素数列表
# for i in range(2,scale+1):#判断是否素数
#     flag=True
#     temp=int(pow(i,0.5))
#     for j in range(2,temp+1):
#         if i%j==0:
#             flag=False
#             break
#     if flag:
#         listnum.append(i)
# print(listnum)

import math
try:
    num=int(input("请输入一个正整数"))
except ValueError:
    print("输入错误")
if num<=0:
    print("输入错误")
else:
    flag=False
    temp=int(pow(num,1/3))
    # print(temp)
    for i in range(1,temp+1):
        for j in range(1,i):
            for k in range(1,j):
                if pow(i,3)+pow(j,3)+pow(k,3)==num:
                    flag=True
                    print(f'{num}={i}^3+{j}^3+{k}^3是阿姆斯特朗数')
                    break
    if flag==False:
        print("{}不是阿姆斯特朗数".format(num))
