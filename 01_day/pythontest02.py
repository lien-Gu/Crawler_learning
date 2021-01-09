# 数值型
# python 弱类型语言 类似js
# num1=10.23  #<class 'float'>
# num1=10  #<class 'int'>
# num1='10'  #<class 'str'>
# print(type(num1))

#多变量赋值
# n1=2
# n2='hello'
# n3=True
# n1,n2,n3=2,'hello',True
# print(n2)

#字符型,列表同理
#s1='hello' #<class 'str'>
#print(type(s1))
#切片 默认切片提取由左到右，起始包含，终止不包含
# [起始，终止，步长]
#步长改为负数
#java [12,13,14,15,16] hello
# print(s1[4])
# print(s1[1:3])
# print(s1[-3:-1]) # print(s1[-1:-3])
# print(s1[1:3:2])
# print(s1[1:])
# print(s1[-4:])
# print(s1[::-1]) #逆序输出
# print(s1[:])

#练习：仿trim函数，实现去除字符串左右空格的功能，利用且切片
str='   abc   '
n=len(str)
i=0
while str[i]==' ':
    i=i+1
p1=i
i=n-1
while str[i]==' ':
    i=i-1
p2=i+1
print(str[p1:p2])


# #字符串格式化
# name='zs'
# age=23
# score=76.56
# print("我的名字是"+name)
# print("我的名字是",name) #有空格
# # %方式 %s字符型  %d整型 %0.1f浮点数，可精确小数
# print("我的名字是%s,年龄是%d,分数是%0.1f"%(name,age,score))
#
# # format方式
# # print("我的名字是{0},年龄是{1}".format(name,age))
#
# #3.6新增 f-string
# name='zs'
# print(f'我的名字：{name}')
# print(f'我的名字：{name.upper()}')
#
# sum_fun=lambda x,y:x+y
# print(f'求和结果{sum_fun(2,3)}')

'''
练习1：用户输入数字（若输入不合法给出提示）
     计算该数字平方根
     用三种方式输出：
'''
# num1=input('请输入数字')
# if(num1.isdigit()):
#     num2 = int(num1)
#     num3=num2**0.5
#     print("%s数字的平方根是%f" % (num1, num3))
#     print("{0}数字的平方根是{1}".format(num1, num3))
#     print(f'{num1}数字的平方根是{num3}')

