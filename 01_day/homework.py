'''
作业：
1、摄氏度和华氏度相互转化，华氏度=摄氏度*1.8+32
        摄氏度转为华氏度请按1
        华氏度转化为摄氏度请按2
        1
        请输入摄氏度：23
        23.0 摄氏度转化为华氏度为：73.4

2、计算三角形的面积
   三个格式化输出结果：三条边分别为X,X,面积为X
'''
# import math
# print("请输入三角形的三条边长度：")
# a=float(input("a:"))
# b=float(input("b:"))
# c=float(input("b:"))
# if a+b>c and math.fabs(a-b)<c:
#     p=(a+b+c)/2
#     s=math.sqrt(p*(p-a)*(p-b)*(p-c))
#     print("三条边分别为%.1f,%.1f,%.1f,面积为%.2f"%(a,b,c,s))
#     print("三条边分别为{0:.1f},{1:.1f},{2:.1f},面积为{3:.2f}".format(a,b,c,s))
#     print(f'三条边分别为{a:.1f},{b:.1f},{c:.1f},面积为{s:.2f}')
# else:
#     print("输入错误")


print("摄氏度转为华氏度请按1,华氏度转化为摄氏度请按2")
tab=input("输入：")
if tab=='1':
    C = input("请输入摄氏度：")
    F=float(C)*1.8+32
    print(f'{C}摄氏度转化为华氏度为：{F}')
elif tab=="2":
    F=input("请输入华氏度：")
    C=(float(F)-32)/1.8
    print(f'{F}华氏度转化为摄氏度为：{C}')
else:
    print("输入错误")

