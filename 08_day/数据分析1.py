import pandas as pd
# 加载数据集
#df=pd.read_csv('student.csv',encoding='gbk）
# names= 字段名(标题名)
df=pd.read_csv('student.csv',names=['name','height','weight','sex','age'])
# 读头部数据
# print(df.head())
# print(df.head(2))
# 读尾部数据
# print(df.tail()) #5条
# print(df.tail(1))
# loc iloc ix
# print(df.iloc[1:3])
# print(df['name'])
#name height weight --多列名，用列表
# print(df[['name','height','weight']])
# 提取指定行
# print(df.iloc[2]) #索引是2的元素
# print(df.iloc[[2,4]])
#提取索引为1、5的name weight 二行二列
# print(df[['name','weight']][[1,5]])
# print(df.ilot[[1,5],[0,2]])

# print(df['sex']=='nv')
# print(df[df['sex']=='nv'])
# 提取年龄大于25岁的学生、姓名身高、体重
# print(df[df['sex']=='nv'][df['age']>25][['name','height','weight']])
# print(df[(df('sex')=='nv')&(df['age']>25)][['name','height','weight']])

# df['school']=['a','b','c','a','b','c','c']
# print(df)
#
# #增加字段，将体重化为公斤
# df['kg']=df['weight']/2
print(df)

#value_count()
df_sex=df['sex'].value_counts()
print(type(df_sex))
print(df_sex)
print(df_sex.index) #提取series索引值
print(df_sex.value) #提取series值