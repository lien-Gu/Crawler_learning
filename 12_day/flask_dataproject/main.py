from flask import Flask,render_template
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['KaiTi']
mpl.rcParams['font.serif'] = ['KaiTi']
import os

# 创建Flask对象实例
app=Flask(__name__)

@app.route('/')
def index():
    # return 'hello world!'
    return render_template('index.html')

#爬虫数据展示
@app.route('/datashow')
def datashow():
    # return 'hello world!'
    company=pd.read_excel('death_company.xls')
    #将company转换为列表
    company_data=np.array(company)
    company_data_1=company_data.tolist()
    return render_template('data_show.html',result=company_data_1[:20])

#注销公司时长分析
@app.route('/time_ana')
def time_ana():
    company = pd.read_excel('death_company.xls')

    company.drop(columns=['id'], axis=1, inplace=True)
    company.drop(company[company['com_name'] == '00'].index, inplace=True)
    # 公司存活时间分析
    def time_convert(b_date, c_date):
        date_f = datetime.datetime.strptime(b_date, '%Y-%m-%d')
        date_f2 = datetime.datetime.strptime(c_date, '%Y-%m-%d')
        return (date_f2 - date_f).days

    company['live_days'] = company.apply(lambda x: time_convert(x['com_born'], x['com_change_close_date']), axis=1)
    com_live=company.sort_values(by='live_days',ascending=False)[:10]
    # print(com_live)
    live_x=com_live['com_name']
    live_y=com_live['live_days']
    plt.bar(live_x,live_y)

    #x/y 坐标说明
    plt.xlabel('公司名称',fontsize=12)
    plt.ylabel('存活时长',fontsize=12)
    #标题
    plt.title('公司存货时长前10的数据分布情况',fontsize=14)

    #图片保存
    basedir = os.path.abspath(os.path.dirname(__file__))
    # print(basedir+'/static/images/')
    plt.savefig(basedir + '/static/images/' + 'zx_company_live.png')
    return render_template('date_time_ana.html')

#注销公司融资分布情况
@app.route('/com_found')
def com_found():
    company = pd.read_excel('death_company.xls')

    company.drop(columns=['id'], axis=1, inplace=True)
    company.drop(company[company['com_name'] == '00'].index, inplace=True)

    com_found=company['com_fund_status_name'].value_counts()[:5]
    # print(type(com_found))  #<class 'pandas.core.series.Series'>
    value=com_found.values  #[3410 1782  522  238   64]
    reason=com_found.index   #Index(['不明确', '尚未获投', '天使轮', 'A轮', 'B轮'], dtype='object')
    plt.pie(value,labels=reason,autopct='%.2f%%',
            shadow=True,
            colors=['y','r','b','g','w'],
            explode=[0,0.1,0,0,0],
            startangle=150)
    basedir = os.path.abspath(os.path.dirname(__file__))
    # print(basedir+'/static/images/')
    plt.savefig(basedir + '/static/images/' + 'zx_company_found.png')
    return render_template('data_com_found.html')


@app.route('/death_reason')
def death_reason():
    company = pd.read_excel('death_company.xls')

    company.drop(columns=['id'], axis=1, inplace=True)
    company.drop(company[company['com_name'] == '00'].index, inplace=True)

    def get_data(company):
        death_reason = company['death_reason'].str.strip('/').str.split('/', expand=True).stack().reset_index()[0]
        # print(death_reason)
        return death_reason

    def data_deal(death_reason):
        d_r = death_reason.value_counts()[:20]
        x = d_r.index
        y = d_r.values
        print(type(x))
        pic = plt.bar(x, y)
        plt.xticks(rotation=45)
        basedir = os.path.abspath(os.path.dirname(__file__))
        plt.savefig(basedir + '/static/images/' + 'zx_company_death_reason.png')

    death_reason = get_data(company)
    data_deal(death_reason)

    return render_template('data_death_reason.html')

if __name__=='__main__':
    # 启动web服务器
    app.run()























