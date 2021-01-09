# t1=()# 创建空元组
# t2=(11,22,'abc')
# # print(t2[1])
# t2[1]


# s1={} # <class 'dict'>空字典
# print(type(s1))

# s2=set() #<class 'set'>空集合
# print(type(s2))


# s3={'a','b','a','c','b'}
# print(s3) # {'a', 'b', 'c'}自动去重

# 运算
# s4={'a','b','c','d'}
# s5={'b','d','e','f'}
# print(s4-s5) # {'c', 'a'}
# print(s4+s5) 没有相加
# print(s4|s5) # {'c', 'd', 'a', 'f', 'b', 'e'}
# print(s4&s5) # {'b', 'd'}
# print(s4^s5) # {'a', 'e', 'f', 'c'}

# 函数
# 函数定义
# def fun1():
#     print('hello')
# # 函数调用
# fun1()

# 默认参数
# def fun2(a,c='jsj'):
#     s1='姓名：'+a+' 专业：'+c
#     return s1
# print(fun2('zs'))
# print(fun2('zs','tjx'))

# 不定项参数
# def fun3(*args):
#     print(args)
# fun3(1,2,3,8,9,0)


'''
练习：编写函数，可进行不定项值的累加
      函数名add_fun(2,3,4,5)
      输入参数合法性验证
'''
# def add_fun(*t1):
#     try:
#         sum = 0
#         for i in t1:
#             sum += i
#         print(sum)
#     except Exception:
#         print("请输入数字")
# add_fun(1,2,3,4,5)

# # 文件不存在会自动创建
# f1=open("afile.txt",'w')
# f1.write('hello')
# f1.write('world')
# f1.close()
#
# with open("afile.txt","w") as f1:
#     f1.write('hello')

# with open('afile.txt','a') as f1:
#     f1.write('world')
#
f1=open("afile.txt",'r')
print(f1.read())
f1.close()