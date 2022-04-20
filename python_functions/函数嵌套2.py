# -*- encoding=utf8 -*- 
'''
@Time:  2022/4/20-14:47
@User:  Administrator
@File:  函数嵌套.py
@Email：  liuxiong@fcbox.com
'''
'''
函数的嵌套调用
'''
def max(x,y):
    return x if x>y else y


def max2(x,y,z):
    res1 = max(x,y)
    res2 = max(res1,z)
    return res2

res = max2(3,1,5)
print(res)

'''
函数的嵌套定义
'''

def f1():
    print("from f1")
    def f2():
        print("from f2")
        def f3():
            print("from f3")
        f3()
    f2()

f1()
#这里直接调用f3会报错