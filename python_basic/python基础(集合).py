# -*- encoding=utf8 -*- 
'''
@Time:  2022/4/6-15:01
@User:  Administrator
@File:  python基础(集合).py
@Email：  liuxiong@fcbox.com
'''
'''
集合（Set）
集合是无序和无索引的集合。在 Python 中，集合用花括号编写
作用：去重，关系运算

可存放元素：数字 字符串  元组 （不可变类型）


优先掌握的操作：
1、长度len
2、成员运算in和not in

3、|合集
4、&交集
5、-差集
6、^对称差集
7、==
8、父集：>,>= 
9、子集：<,<=    


'''
# 集合创建
# s2 = {"apple", "banana", "cherry"}
# s1 = set("123")
# print(s1)
# print(s2, type(s2))

'''
集合的关系运算
'''

# 报名python学生
pythons = {"mike","jack","egon","oldboy"}
# 报名Linux的学生
linuxs = {"tom", "jerry", "mike"}
# 同时报名python和Linux
# 求交集
print("-----求交集----")
print(pythons & linuxs)
print(pythons.intersection(linuxs))
# 报名学习的学生
# 求并集
print("求并集".center(40, '-'))
print(pythons | linuxs)
print(pythons.union(linuxs))
# 只报了python,没有报linux学生
# 求差集
print("----求差集----")
print(pythons-linuxs)
print(pythons.difference(linuxs))
# 没用同时报这两门课学生的名字
print("交叉补集".center(40,'-'))
print(pythons ^ linuxs)
print(pythons.symmetric_difference(linuxs))

'''
去重
'''
print("去重".center(40,'-'))

l = [3,'a',1,2,3,4,5,'a']
print(set(l))

# 去重并保留原有的顺序
l1=[]
s=set()
for i in l:
    if i not in s:
        s.add(i)
        l1.append(i)

print(l1)