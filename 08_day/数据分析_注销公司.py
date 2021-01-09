import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['KaiTi']
mpl.rcParams['font.serif'] = ['KaiTi']
# 读取数据 # pip install xlrd
company=pd.read_excel('death_company.xls')

#数据清洗
# 删除id列 axis=0删除行
# com_new=company.drop(columns=['id'],axis=1)
# 在原数据集中操作
# company.drop(columns=['id'],axis=1,inplace=True)
#删除行
# com_new=company.drop([116])
company.drop(company[company['com_name']=='00'].index,inplace=True)
# print(company.head(119))

#数据统计分析
#注销公司地理位置分布情况--折线图
# x--位置 y--数量
# com_pos=company['com_position'].value_counts()
# # print(type(com_pos))
# # print(com_pos.strip)
# # print(com_pos.index)
# # print(com_pos.values)
# com_pos_x=com_pos.index
# com_pos_y=com_pos.values
# plt.plot(com_pos_x,com_pos_y,marker='^')
# plt.xlabel('position')
# plt.ylabel('counts')
# plt.show()

# 公司存活时间统计分析
#日期处理
# import datetime
# print(date_f)
# print(date_f.year)
# print(date_f.month)
# print(date_f.day)


# 数据集.apply(function)
# lambda
# def f1(arg):
#     print('aa:',arg)
# company['com_born'].apply(f1)
#将f1转换为lamda
# company['com_born'].apply(lambda arg:print('aa:',arg))

# def time_convert(b_date):
#     date_f=datetime.datetime.strptime(b_date,'%Y-%m-%d')
#     return date_f
# company['com_born_date']=company['com_born'].apply(time_convert)
# print(company)

#生成新字段 存货时长（天） live_days
import datetime
#方法一
# def time_convert(b_date):
#     date_f=datetime.datetime.strptime(b_date,'%Y-%m-%d')
#     return date_f
# company['live_days']=company['com_born'].apply(time_convert)-company['com_change_close_date'].apply(time_convert)

#方法三
# def time_convert(b_date,c_date):
# #     date_f=datetime.datetime.strptime(b_date,'%Y-%m-%d')
# #     date_f2=datetime.datetime.strptime(c_date,'%Y-%m-%d')
# #     return (date_f2-date_f).days
# # company['live_days']=company.apply(lambda x:time_convert(x['com_born'],x['com_change_close_date']),axis=1)
# # print(company['live_days'])

#方法三
# def time_convert(b_date):
#     date_f=datetime.datetime.strptime(b_date,'%Y-%m-%d')
#     return date_f
# def time_cal(item):
#     t_born_f=time_convert(item['com_born'])
#     t_dead_f = time_convert(item['com_change_close_date'])
#     return (t_dead_f-t_born_f).days
# company['live_days']=company.apply(time_cal,axis=1)
# print(company)



