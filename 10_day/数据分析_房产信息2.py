import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['KaiTi']
mpl.rcParams['font.serif'] = ['KaiTi']

#读取csv文件
df_house=pd.read_csv('deal_houseinfo.csv',encoding='utf-8-sig')
# print(df_house)

#二手房屋的建筑面积与总价的情况分析--散点图
plt.scatter(df_house['总面积'],df_house['总价'],color='m')
plt.grid(linestyle=':',color='c')
plt.show()

'''
二手房小区建成年份与小区均价数据分析--折线图plot
1、将小区均价的暂无数据用小区单价替换
2、将小区建成的暂无数据删除
'''


# df_house['小区均价']=df_house.apply(lambda arg:int(arg['单价']) if arg['小区均价']=='暂无数据' else int(arg['小区均价']),axis=1)
# df_house.drop(df_house[df_house['小区建成']=='暂无数据'].index,inplace=True)
# x=df_house.groupby(['小区建成'])['小区均价'].mean().index
# y=df_house.groupby(['小区建成'])['小区均价'].mean().values
# plt.xticks(rotation=270)
# plt.plot(x,y,color='m')
# plt.show()