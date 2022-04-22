# -*- encoding=utf8 -*- 
'''
@Time:  2022/4/20-22:44
@User:  Administrator
@File:  生成器6.py
@Email：  liuxiong@fcbox.com
'''

'''
一 什么是生成器

复制代码
#只要函数内部包含有yield关键字，那么函数名()的到的结果就是生成器，并且不会执行函数内部代码
'''

def func():
    print('====>first')
    yield 1
    print('====>second')
    yield 2
    print('====>third')
    yield 3
    print('====>end')

g=func()
# print(g.__next__())
# print(g.__next__())

# 二 生成器就是迭代器

g.__iter__()
g.__next__()
#2、所以生成器就是迭代器，因此可以这么取值
res=next(g)
print(res)

# 这点不太理解？？？？？？？？

'''
四 协程函数


复制代码
#yield关键字的另外一种使用形式：表达式形式的yield
def eater(name):
    print('%s 准备开始吃饭啦' %name)
    food_list=[]
    while True:
        food=yield food_list
        print('%s 吃了 %s' % (name,food))
        food_list.append(food)

g=eater('egon')
g.send(None) #对于表达式形式的yield，在使用时，第一次必须传None，g.send(None)等同于next(g)
g.send('蒸羊羔')
g.send('蒸鹿茸')
g.send('蒸熊掌')
g.send('烧素鸭')
g.close()
g.send('烧素鹅')
g.send('烧鹿尾')

'''

'''
yield总结

#1、把函数做成迭代器
#2、对比return，可以返回多次值，可以挂起/保存函数的运行状态

'''