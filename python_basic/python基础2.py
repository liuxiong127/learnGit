# -*- encoding=utf8 -*- 
'''
@Time:  2022/4/2-16:07
@User:  Administrator
@File:  python基础2.py
@Email：  liuxiong@fcbox.com
'''
'''
python的输入输出
'''
# a = input("请输入>>>>>:")
# print(a)


'''
python的条件及循环语句

if……else
for循环
while循环
'''




'''
for循环
'''
#
# for i in a:
#     print(i)
#
# print("-------------------")
# for i in range(len(a)):
#     print(a[i])

'''
九九乘法表
'''
for i in range(1,10):
    for j in range(1,i+1):
        print("%2d*%2d=%2d"%(i,j,i*j), end='')
    print()
else:
    print("九九乘法表打印完成")


'''
while循环
'''

i = 100
count = 0
while i>0:
    count +=i
    i-=1
print(count)


a = int(input("请输入数字>>>\n"))
if a ==1:
    print("厉害")
elif a==2:
    print("输了")

'''
while循环
if...else条件语句

'''

'''
while和if……else条件结合使用
'''

user = "admin"
password = "123456"
i = 3
while True:
    if i==0:
        break
    account = input("请输入用户名>>:")
    if account != user:
        i-=1
        print("用户不存在!")
        if i==0:
            print("三次机会用完了")
            break
        continue
    passwd = input("请输入密码>>:")
    if account==user and password==passwd:
        print("login success！！")
    else:
        i-=1
        print("用户或密码错误！！")
        if i==0:
            print("三次机会用完了！！")
        continue


'''
break 结束当前循环
continue 结束本次循环，进入下次循环
'''
