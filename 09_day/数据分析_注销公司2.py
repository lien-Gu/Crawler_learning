import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['KaiTi']
mpl.rcParams['font.serif'] = ['KaiTi']
import datetime
company=pd.read_excel('death_company.xls')
company.drop(columns=['id'],axis=1,inplace=True)
company.drop(company[company['com_name']=='00'].index,inplace=True)

#公司存活时间分析
def time_convert(b_date,c_date):
    date_f=datetime.datetime.strptime(b_date,'%Y-%m-%d')
    date_f2=datetime.datetime.strptime(c_date,'%Y-%m-%d')
    return (date_f2-date_f).days
company['live_days']=company.apply(lambda x:time_convert(x['com_born'],x['com_change_close_date']),axis=1)
# print(company)
#平均存活天数
# print(company['live_days'].mean())
#按区域计算公司的平均存活时长
#groupby 分组
com_group=company.groupby('com_position')
print(com_group)
print(com_group.mean())

# # 提取存活时间最短的公司 idxmn
# print(company['com_name'][company['live_days'].idxmin()])
# print(company.loc[company['live_days'].idxmin(),'com_name'])
# # 提取存活时间最短长的公司 idxmax
# print(company['com_name'][company['live_days'].idxmax()])
# print(company.loc[company['live_days'].idxmax(),'com_name'])
# # 存活时间排序 sort_values
# # 默认--升序ascending=True  降序ascending=Fasle
# print(company['live_days'].sort_values(ascending=False))
# print(company.sort_values(by='live_days',ascending=False)[:20]['com_name'])


#绘制柱状图--公司存货时长前10的数据分布情况
# # plt.plot
# # plt.bar
# com_live=company.sort_values(by='live_days',ascending=False)[:10]
# # print(com_live)
# live_x=com_live['com_name']
# live_y=com_live['live_days']
# p1=plt.bar(live_x,live_y)
# # 图例
# # plt.legend(p1,['aaa'],loc='upper right')#上右
# #x/y 坐标说明
# plt.xlabel('公司名称',fontsize=12)
# plt.ylabel('存活时长',fontsize=12)
# #标题
# plt.title('公司存货时长前10的数据分布情况',fontsize=14)
# #图片保存
# plt.savefig('zx_company_live.png')
# plt.show()

#注销公司融资分布情况Top5
# 饼形图 plt.pie(值，labels)
import numpy as np
# com_found=company['com_fund_status_name'].value_counts()[:5]
# # print(type(com_found))  #<class 'pandas.core.series.Series'>
# value=com_found.values  #[3410 1782  522  238   64]
# reason=com_found.index   #Index(['不明确', '尚未获投', '天使轮', 'A轮', 'B轮'], dtype='object')
# plt.pie(value,labels=reason,autopct='%.2f%%',
#         shadow=True,
#         colors=['y','r','b','g','w'],
#         explode=[0,0.1,0,0,0],
#         startangle=150)
# plt.show()

#A轮注销公司所在城市情况分析Top10
# found_A=company[company['com_fund_status_name']=='A轮']
# found_A_pos=found_A['com_position'].value_counts()[:10]
# print(found_A_pos)
# value=found_A_pos.values
# label=found_A_pos.index
# plt.pie(value,labels=label,autopct='%.2f%%',shadow=True)
# plt.legend(loc='best')
# plt.title('A轮注销公司所在城市情况分析Top10')
# plt.show()

'''
公司注销原因分布情况（柱形图）Top20
现金流断裂 300
业务调整 200
难点：1、数据末尾有/
      2、如何提取出新列，形成新的数据集分析
'''


# def get_data(company):
#     death_reason=company['death_reason'].str.strip('/').str.split('/',expand=True).stack().reset_index()[0]
#     # print(death_reason)
#     return death_reason
#
# def data_deal(death_reason):
#     d_r=death_reason.value_counts()[:20]
#     x=d_r.index
#     y=d_r.values
#     print(type(x))
#     pic=plt.bar(x,y)
#     plt.xticks(rotation=45)
#     plt.show()
#
# death_reason=get_data(company)
# data_deal(death_reason)

# death_reason_df=company['death_reason'].str.split('/',expand=True).stack().reset_index()
# print(death_reason_df)
# print('--------------')
# # 方法一
# # death_reason_df.drop(death_reason_df[death_reason_df[0]==''].index,inplace=True)
# # print(death_reason_df)
# #方法二
# death_reason_n=death_reason_df[death_reason_df[0]!=''][0]
# c_death_reason=death_reason_n[:20].value_counts()



















