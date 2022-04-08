# -*- encoding=utf8 -*- 
'''
@Time:  2022/4/8-18:04
@User:  Administrator
@File:  运算符.py
@Email：  liuxiong@fcbox.com
'''

'''
算数运算
+
-
*
/
% 取余
**  幂运算
//  取整
'''
a = 10
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)


'''
比较运算
>
>=
<
<=
==
!=
<> # python3弃用
'''
print(a>b)
print(a>=b)
print(a<b)
print(a<=b)
print(a==b)
print(a!=b)

'''
赋值运算符：
=
+=
-=
*=
/=
%=
**=
//=
'''
a = 8
b = 3
a+=b
print(a)
a-=b
print(a)


print("-----------------位运算-----------------")
'''
位运算
&
|
^
~ 按位取反
<<  左移
>>  右移
'''

a = 4
b = 7
print(a&b)
print(a|b)
print(a^b)
print(a<<1)
print(a>>1)
print(~a)