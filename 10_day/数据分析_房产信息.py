import pandas as pd
house_data=pd.read_excel('house_info.xlsx')

# 设置列名
house_data.columns=['区/县','区域','小区','总价','单价','房屋户型','楼层','总面积',
                    '户型结构','套内面积','建筑类型','朝向','建筑结构','装修情况',
                    '梯户比例','供暖方式','配备电梯','产权年限','s','交易权属','u',
                    '形式','是否满五','产权形式','是否有房本','小区均价','小区建成','style','总栋数']

#数据清洗
#装修情况
#找规律--套内面积不包含‘㎡’，将建筑结构的值赋给装修情况
# house['套内面积'].str.contains()
# if 'a' in 'hello':
#     pass
# def zx_fun(h_data):
#     print(h_data)
#     if '㎡' in str(h_data['套内面积']):
#         return h_data['装修情况']
#     else:
#         return h_data['建筑结构']
#axis=1 按行提取
# house_data['装修情况']=house_data.apply(zx_fun,axis=1)
# print(house_data['装修情况'][:20])
#lambda 优化
# house_data['装修情况']=house_data.apply(lambda h_data:h_data['装修情况'] if '㎡' in str(h_data['套内面积']) else h_data['建筑结构'],axis=1)
# print(house_data['装修情况'].value_counts())

# print(house_data[house_data['装修情况']=='一梯三户'][['户型结构','套内面积','建筑类型','朝向','建筑结构','装修情况']])

def zx2_fun(h_data):
    if ('装' in str(h_data['建筑结构']))or('结构' in str(h_data['朝向'])):
        return h_data['建筑结构']
    elif ('装' in str(h_data['朝向']))or('暖' in str(h_data['装修情况']))or('结构' in str(h_data['建筑类型'])):
        return h_data['朝向']
    elif ('装' in str(h_data['建筑类型']))or('结构' in str(h_data['套内面积'])):
        return h_data['建筑类型']
    else:
        return h_data['装修情况']

house_data['装修情况']=house_data.apply(zx2_fun,axis=1)
# print(house_data['装修情况'].value_counts())
# print(house_data[house_data['装修情况']=='未知'][['户型结构','套内面积','建筑类型','朝向','建筑结构','装修情况']])

#房屋装修情况和房屋均价的数据分析
#groupby()  sum mean 柱形图
#方法一
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['KaiTi']
mpl.rcParams['font.serif'] = ['KaiTi']
# house_zx=house_data.groupby('装修情况').mean()['单价']
# y=house_zx.values
# x=house_zx.index
# plt.bar(x,ye)
# plt.show()
#方法二
zx_jj_data=house_data.groupby('装修情况').mean()['单价']
zx_jj_data.plot(kind='bar',color=['g','r'])
plt.xlabel('装修情况')
plt.ylabel('房屋均价')
plt.show()

#数据清洗
#楼层分解为： 楼层 总楼层
#中楼层（共25层）   中楼层 25
#strip()
#法1
# def lc_fun(h_data):
#     h_data['楼层'],h_data['总楼层']=h_data['楼层'].strip(')').split('(')
#     h_data['总楼层']=int(h_data['总楼层'].strip('共').strip('层'))
#     return h_data
# house_data=house_data.apply(lc_fun,axis=1)

#法2
# house_data['总楼层']=house_data.apply(lambda arg:str(arg['楼层'])[3:].strip('(共').strip('层)'),axis=1)
# house_data['楼层']=house_data.apply(lambda arg:str(arg['楼层'])[0:3],axis=1)
# print(house_data[['楼层','总楼层']][:20])

#数据清洗
'''
1、总面积：去掉㎡
2、小区均价：去掉元/㎡，去掉回车换行
3、小区建成：去掉建成
'''
# house_data['总面积']=house_data.apply(lambda arg:str(arg['总面积']).strip('㎡'),axis=1)
# house_data['小区均价']=house_data.apply(lambda arg:str(arg['小区均价']).strip('\n').strip('元/㎡'),axis=1)
# house_data['小区建成']=house_data.apply(lambda arg:str(arg['小区建成'])[:5],axis=1)
# print(house_data[['总面积','小区均价','小区建成']][:20])


#转存为.csv
# house_data.to_csv('deal_houseinfo.csv',encoding='utf-8-sig')