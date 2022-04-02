# -*- encoding=utf8 -*- 
'''
@Time:  2022/4/2-11:41
@User:  Administrator
@File:  python基础1.py
@Email：  liuxiong@fcbox.com
'''


# python基础知识
'''
python注释
'''



'''
数据类型
数值
字符串
列表
元组
字典
集合
'''

# 数值
'''
整数  int
浮点数 float
复数 complex

int() 将字符串转换为数值
bit_length() 用二进制表示所需要的最少位数
'''
# num1 = 23
# num2 = 34.56
# num3 = 4+5j
# print(num1, type(num1))
# print(num2, type(num2))
# print(num3, type(num3))
#
#
# print(num1.bit_length())
#
# str1 = "123"
# str2 = "34.67"
# str3 = "4-6j"
# n1 = int(str1)
# n2 = float(str2)
# n3 = complex(str3)
# print(n1, type(n2))
# print(n2, type(n2))
# print(n3, type(n3))


'''
字符串的 
标识：str


'''

# 字符串的表示方法
str1 = "abcdefg"
str2 = '123123好的'
str3 = '''测试员真的好不好'''

print(str1, str2, str3)

# capitalize() 首字母大写，其余变小写
v = "alex MKike"
print(v.capitalize())
# casefold()变成小写
print(v.casefold())

print(v.center(50, '*'))
print(v.count('e',1,10))

print(v.endswith('ke'))
print(v.startswith('al'))

v = "alex123123123\thaode\t123"
# print(v.expandtabs())