# -*- encoding=utf8 -*- 
'''
@Time:  2022/4/11-15:20
@User:  Administrator
@File:  函数基础.py
@Email：  liuxiong@fcbox.com
'''

'''
#语法
def 函数名(参数1,参数2,参数3,...):
    
    函数体
    return 返回的值

#函数名要能反映其意义
'''

# def auth(user:str, passwd:str):
#     '''
#     用户鉴权
#     :param user: 用户名
#     :param passwd: 密码
#     :return:
#     '''
#     if user=="admin" and passwd=="n123456":
#         return 1
#     else:
#         return 0
#
# user = input("please enter your account>>")
# passwd = input("please enter your password>>")
# res = auth(user, passwd)
# print(res)

'''
二 函数使用的原则：先定义，再调用
函数即“变量”，“变量”必须先定义后引用。
未定义而直接引用函数，就相当于在引用一个不存在的变量名
'''

# def foo():
#     print("from foo")
#     bar()
#
# def bar():
#     print("from bar")
# foo()

'''
三 函数在定义阶段都干了哪些事？

#只检测语法，不执行代码
也就说，语法错误在函数定义阶段就会检测出来，而代码的逻辑错误只有在执行时才会知道
'''

'''
四 定义函数的三种形式

1、无参：应用场景仅仅只是执行一些操作，比如与用户交互，打印
2、有参：需要根据外部传进来的参数，才能执行相应的逻辑，比如统计长度，求最大值最小值
3、空函数：设计代码结构
'''

# 无参函数

def logs():
    print(" this is a Logs!!")

logs()

# 有参函数
def add(a:int ,b:int):
    print(a+b)

add(3,7)

# 有参函数，部分入参赋予默认值
def add_1(a, b=2):
    print(a**b)

add_1(4, b=3)
add_1(4)


# 空函数
def auth(user:str, passwd:str)->int:
    '''
    参数说明
    :param user: 账户
    :param passwd: 密码
    :return:
    '''
    pass

def get_filename(filename):
    '''
    :param filename:
    :return:
    '''
    pass



'''
一 调用函数

函数的调用：函数名加括号
1 先找到名字
2 根据名字调用代码
二 函数返回值

无return->None
return 1个值->返回1个值
return 逗号分隔多个值->元组
什么时候该有返回值？
　　　　调用函数，经过一系列的操作，最后要拿到一个明确的结果，则必须要有返回值
　　　　通常有参函数需要有返回值，输入参数，经过计算，得到一个最终的结果
什么时候不需要有返回值？
　　　　调用函数，仅仅只是执行一系列的操作，最后不需要得到什么结果，则无需有返回值
　　　　通常无参函数不需要有返回值


一 形参与实参
#形参即变量名，实参即变量值，函数调用时，将值绑定到变量名上，函数调用结束，解除绑定

#1、位置参数：按照从左到右的顺序定义的参数
        位置形参：必选参数
        位置实参：按照位置给形参传值

#2、关键字参数：按照key=value的形式定义的实参
        无需按照位置为形参传值
        注意的问题：
                1. 关键字实参必须在位置实参右面
                2. 对同一个形参不能重复传值

#3、默认参数：形参在定义时就已经为其赋值
        可以传值也可以不传值，经常需要变得参数定义成位置形参，变化较小的参数定义成默认参数（形参）
        注意的问题：
                1. 只在定义时赋值一次
                2. 默认参数的定义应该在位置形参右面
                3. 默认参数通常应该定义成不可变类型


#4、可变长参数：
        可变长指的是实参值的个数不固定
        而实参有按位置和按关键字两种形式定义，针对这两种形式的可变长，形参对应有两种解决方案来完整地存放它们，
        分别是*args，**kwargs

'''
print("------------------函数说明------------")
print("---------args----------")
def foo(x,y,*args):
    print(x,y)
    print(args)

foo(1,2,[1,2,3,4,5])
foo(1,2,*[1,2,3,4,5])

def foo1(x,y,z):
    print(x,y,z)

foo1(*[1,2,3])

print("---------kwargs----------")

def foo2(x,y,**kwargs):
    pass