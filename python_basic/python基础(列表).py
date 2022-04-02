# -*- encoding=utf8 -*- 
'''
@Time:  2022/4/2-17:12
@User:  Administrator
@File:  python基础(列表).py
@Email：  liuxiong@fcbox.com
'''
'''
列表的标识符：list
列表的元素可以是任何数据类型
'''


# li = [1,'good',[1,2,34], (1,2,"mike"),67]
# # 给列表追加，可以是任意类型的数据
# li.append(1)
# li.append('A')
# li.append(["nihao",45])
# li.append(("good",44445))
# print(li)

# li = [1,'good',[1,2,34], (1,2,"mike"),67]
# li.clear() # 清空列表的所有元素
# print(li)

li = [1,'good',[1,2,34], (1,2,"mike"),67]
l1 = li.copy()
print(l1, id(l1))
print(li, id(li))

print()