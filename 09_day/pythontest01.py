# s1='hello;world;students'
# r_s=s1.split(';')
# print(type(r_s))
# print(r_s)

import pandas as pd
# 创建数据集
d1={
    'stuid':[12,13,14,15],
    'stusport':['lq;ppq','lq','zq;lq;ppq','bq;zq;ppq']
}
df=pd.DataFrame(d1)
# print(type(df))
# print(df)
# pandas---str
# print(df['stusport'].str.split(';'))
# expand=True展开，分成多列
# print(df['stusport'].str.split(';',expand=True))
# print('------------------------------------------')
# stack --改变显示模式
print(df['stusport'].str.split(';',expand=True).stack())
print('------------------------------------------')

# 重置索引 reset_index()
# reset_index()[0]  提取列名为0（数值型）的值
print(df['stusport'].str.split(';',expand=True).stack().reset_index()[0])



