import numpy as np
# from matplotlib import pyplot as plt
import matplotlib.pyplot as plt

# ndarray 数据类型
# a1=np.array([2,3,4,5,6])
# print(type(a1)) #<class 'numpy.ndarray'>
# b1=np.array([6,7,2,3,9])
# 折线图
# plt.plot(a1,b1)
# plt.plot(a1,b1,
#          linewidth=5,# 线宽
#          color='g',# 线颜色
#          linestyle='-',# : - -- -.线样式
#          marker='^'#对对应的点做标记 o * ^
#          )
# plt.xlabel('x-a1')
# plt.ylabel('y-b1')
# plt.show()


x=np.linspace(-10,10)#等差数列
y=np.sin(x)
plt.plot(x,y)
plt.show()