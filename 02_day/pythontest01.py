# # while循环求和
# sum=0
# num=1
# while num<=100:
#     sum=sum+num
#     num+=1# 没有自增
# print(sum)
#
#
# # while...else
# num=0
# while num<3:
#     print("小于3:",num)
#     num+=1
# else:
#     print("大于或者等于3:",num)
#
#
# # 判断奇偶数
# n=0
# while n<3:
#     num=int(input("请输入数字:"))
#     if num%2==0:
#         print(f'{num}是偶数')
#     else:
#         print(f'{num}是奇数')
#     n+=1
#
#
# while True:
#     num=int(input("请输入数字:"))
#     if num%2==0:
#         print(f'{num}是偶数')
#     else:
#         print(f'{num}是奇数')
#     if num==0:
#         break #跳出整体循环
#         # continue  跳出当前循环
#
#
# while True:
#     try:
#         num=int(input("请输入数字:"))
#     except Exception as ep:
#         print("错误！请输入数字。")
#         #将异常写到log日志
#         print(ep)
#         continue
#     if num%2==0:
#         print(f'{num}是偶数')
#     else:
#         print(f'{num}是奇数')
#     if num==0:
#         break
#
#
# # 斐波那契数列
# while True:
#     print("你需要几项？")
#     try:
#         n = int(input())
#         # print(n)
#     except ValueError:
#         print("错误，输入非数字！")
#         continue
#     if n<=0:
#         print("错误，输入非整数！")
#         continue
#     a1, a2 = 1, 1
#
#     i = 3
#     print(a1)
#     print(a2)
#     while i <= n:
#         a3 = a1 + a2
#         print(a3)
#         a1 = a2
#         a2 = a3
#         i = i + 1
#
while True:
    try:
        items=int(input("请输入项数："))
    except Exception as e:
        print("请输入数字！")
        continue
    if items<=0:
        print("请输入大于0的数字！")
        continue

    n1,n2=0,1
    n3=n1+n2
    num=2#循环次数
    print(n1)
    print(n2)
    while num<items:
        n3=n1+n2
        print(n3)
    #   交换 n3->n2 n2->n1
        n1=n2
        n2=n3
        num+=1
#
# #可读性






