#创建列表
# list1=[] # 空列表
# list2=[11,22,33]
#支持多种数据类型
# list3=[11,'hello',34.5,True]
# print(list3)

#列表切片
# list4=[11,22,33,44,55]
# print(list4[3])
# print(list4[-2])
# print(list4[1:4])
# print(list4[:3])

#列表的赋值
# list5=[11,22,33,44,55]
# list5[1:3]=88
# list5[1:3]=[77,88]
# print(list5)

#列表运算
# list6=[11,22,33]
# list7=[55,66]
# print(list6+list7)
# 'hello'*10
# print(list6*10)
# print(55 in list7)
#力扣 --算法 数组去重

#列表遍历
# list1=[11,22,33,44,55]
# for i in list1:
#     if i>30:
#         print(i)

#列表的属性与方法
# list2=[11,22,33,44,55]
# print(len(list2))  #列表长度
# 追加append,在末尾添加
# list2.append("abc")
#删除 pop 默认删除表中末尾一个元素
#         可指定索引值删除
# list2.pop()
# print(list2)
# list2.pop(0)
# print(list2)

#-1 reverse()反向列表元素
# list2.reverse()
# print(list2)

# list2=[11,22,11,22,11]
# print(list2.count(11))

'''
练习：
    1、列表去重list1=[11,22,33,44,55,11,33,33]
    2、统计列表中元素出现的次数,禁用count
       11 3
       22 2
'''
# list1=[11,22,33,44,55,11,33,33]
# n=len(list1)
# list2=[]
# num=[]
# for i in range(n):
#     t=list1[i]
#     if t in list2:
#         for j in range(len(list2)):
#             if t == list2[j]:
#                 num[j] += 1
#                 break
#     else:
#         list2.append(t)
#         num.append(1)
#
# print(list2)
# for i in range(len(list2)):
#     print(list2[i],num[i])

#dict字典的创建
# dict1={} #空字典
# dict2={'name':'zs','age':23}
#访问,无序
# print(dict2['name'])
# print(dict2['age'])
#修改
# dict2['name']='ls'
#新增元素
# dict2['school']='nefu'
#删除
# del dict2['age']
#遍历
# for i in dict2:
#     print(i)
#     print(dict2[i])

'''
需求：学生信息录入，信息查询
1、录入学生姓名、姓名、专业 （分割方法split）
  可输入多个
2、存储格式从【[【】,【】]】

'''
str1=input("请输入学生信息，用逗号分隔：")
list_r=str1.split(',')
list_stu=[]
item=[]
for i in range(0,len(list_r),3):
    dict_tem = {}
    dict_tem['name']=list_r[i]
    dict_tem['age']=int(list_r[i+1])
    dict_tem['zy']=list_r[i+2]
    list_stu.append(dict_tem)
    print(list_stu)
print("name age zy")
for i in list_stu:
    print('%s %d %s'%(i['name'],i['age'],i['zy']))

str2=input("输入姓名来查询：")
flag=0
for i in list_stu:
    if i['name']==str2:
        flag=1
        print("查询成功")
        print('%s %d %s' % (i['name'], i['age'], i['zy']))
        break
if flag==0:
    print("查无此人")




