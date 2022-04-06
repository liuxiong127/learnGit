# -*- encoding=utf8 -*- 
'''
@Time:  2022/4/6-13:15
@User:  Administrator
@File:  元组.py.py
@Email：  liuxiong@fcbox.com
'''

'''
元组：
标识符：tuple
元组不可修改

'''
'''
index()
count()

'''

t1 = (1,2,5,4,2,3,4)
print(t1.count(2))
print(t1.index(3,0,6))


# 将列表变为元组,可迭代对象才可以变成元组
li = ['a','b','c']
str1 = "abcdef"
num1 = 45
t2 = tuple(li)
t3 = tuple(str1)
# t4 = tuple(num1)
print(t2)
# print(t3)

