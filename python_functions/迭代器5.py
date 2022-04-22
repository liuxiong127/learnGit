# -*- encoding=utf8 -*- 
'''
@Time:  2022/4/20-18:10
@User:  Administrator
@File:  迭代器5.py
@Email：  liuxiong@fcbox.com
'''

'''
迭代器
一 迭代的概念

复制代码
#迭代器即迭代的工具，那什么是迭代呢？
#迭代是一个重复的过程，每次重复即一次迭代，并且每次迭代的结果都是下一次迭代的初始值

'''

# while True:  # 只是单纯地重复，因而不是迭代
#     print('===>')

# l = [1, 2, 3]
# count = 0
# while count < len(l):  # 迭代
#     print(l[count])
#     count += 1


'''
二 为何要有迭代器？什么是可迭代对象？什么是迭代器对象？


复制代码
#1、为何要有迭代器？
对于序列类型：字符串、列表、元组，我们可以使用索引的方式迭代取出其包含的元素。
但对于字典、集合、文件等类型是没有索引的，若还想取出其内部包含的元素，则必须找出一种不依赖于索引的迭代方式，这就是迭代器

#2、什么是可迭代对象？
可迭代对象指的是内置有__iter__方法的对象，即obj.__iter__，如下
'hello'.__iter__
(1,2,3).__iter__
[1,2,3].__iter__
{'a':1}.__iter__
{'a','b'}.__iter__
open('a.txt').__iter__

#3、什么是迭代器对象？
可迭代对象执行obj.__iter__()得到的结果就是迭代器对象
而迭代器对象指的是即内置有__iter__又内置有__next__方法的对象

文件类型是迭代器对象
open('a.txt').__iter__()
open('a.txt').__next__()


#4、注意：
迭代器对象一定是可迭代对象，而可迭代对象不一定是迭代器对象


'''

# a = "hello"
# b = a.__iter__()
# print(b.__next__())
# print(b.__next__())
# print(b.__next__())
# print(b.__next__())
# print(b.__next__())

#三 迭代器对象的使用

l1 = [1,2,3,4,5,6]
for i in l1:
    print(i)

# 使用迭代器 来实现for循环
l1_iter = l1.__iter__()
while 1:
    try :
        print(l1_iter.__next__())
    except StopIteration:
        break

'''
#基于for循环，我们可以完全不再依赖索引去取值了
dic={'a':1,'b':2,'c':3}
for k in dic:
    print(dic[k])

#for循环的工作原理
#1：执行in后对象的dic.__iter__()方法，得到一个迭代器对象iter_dic
#2: 执行next(iter_dic),将得到的值赋值给k,然后执行循环体代码
#3: 重复过程2，直到捕捉到异常StopIteration,结束循环
'''

'''
五 迭代器的优缺点

优点：
  - 提供一种统一的、不依赖于索引的迭代方式
  - 惰性计算，节省内存
缺点：
  - 无法获取长度（只有在next完毕才知道到底有几个值）
  - 一次性的，只能往后走，不能往前退
'''
