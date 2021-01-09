# # #输出0-9 for
# for i in [0,1,2,3,4,5,6,7,8,9]:
#     print(i)
# for i in range(10):# range(0,10,1)
#     print(i)
# for i in range(2,10):
#     print(i)
# for i in range(2,50,3):#range(起始，终止，步长)
#     print(i)

print(list(range(1,10,2)))

#遍历字符
for j in 'hello':
    print(j)
#
# #for嵌套
# #9*9乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         # print(f'{i}*{j}={i*j}')# 2*3=6
#         print('{}*{}={}\t'.format(i,j,i*j),end=' ')
#     print()#等价于：print(end='\n')
#
# import time
# print("--------执行开始--------")
# for i in range(101):
#     print(f"\r{i}%["+"*"*i+"-"*(100-i)+">]",end='')
#     time.sleep(0.1)
# print()
# print("--------执行结束--------")


#^居中 >右对齐 <左对齐
# print("{:^10.0f}".format(23))
#
# list1=[11,22,33,44,55,11,33,33]
# list2=[]
# t=list1[0]
# list2.append(t)
# print(list2)