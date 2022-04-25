# -*- encoding=utf8 -*- 
'''
@Time:  2022/4/20-13:13
@User:  Administrator
@File:  字符串format格式化输出.py
@Email：  liuxiong@fcbox.com
'''

tpl = "name:{} age:{} job:{}".format("mike", 50, "软测")
print(tpl)

# 按元组的下标取值
tpl1 = "name:{2} age:{1} job:{0}".format("mike", 50, "软测")
tpl11 = "name:{2} age:{1} job:{0[0]}".format(["jack","tom"], 50, "软测")
print(tpl11)


# 字典的形式
tpl2 = "name:{name}, age {age}".format(name="test", age=43)
tpl23 = "name:{name}, age {age}".format(**{"name":"test", "age":43})
print(tpl23)


tpl4 = "name:{:s}, age {:d}".format("学成", 43)
print(tpl4)

tpl5 = "name:{:s}, age {:d}".format(*("学shang", 43))
print(tpl5)

tpl6 = "name:{:s}, age {:d}".format(*["学shang", 17])
print(tpl6)

tpl7 = "name:{name:s}, age {age:d}".format(name="学shang", age=17)
print(tpl7)