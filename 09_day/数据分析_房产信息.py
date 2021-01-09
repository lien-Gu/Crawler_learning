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
# if 'a' in 'hello':
#     pass
def zx_fun(house):
    # print(type(house['套内面积']))
    if '㎡' in house['套内面积']:
        return house['装修情况']
    else:
        return house['套内面积']
# print(house_data['套内面积'])
house_data['装修情况']=house_data.apply(zx_fun)
print(house_data).head(10)




