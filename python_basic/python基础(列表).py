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
# l1 = li.copy()
# print(l1, id(l1))
# print(li, id(li))
#
# print()

'''
count() # 统计数量
index() # 查看索引下标值
'''
# li = [1,2,3,4,5,'1','2',1]
# print(li.count(1))
# print(li.index(2))


'''
append() # 在列表末尾追加一个元素
# 给列表追加，可以是任意类型的数据
extend() # 在列表末尾追加元素，可迭代对象
insert() # 在制定位置，插入一个元素
# 插入元素，可以是任意类型的数据
'''
# li = ['mike', 1,2,3,4,"test"]
# li.append("append加入的元素")
# li.extend([1,2,3])
# li.extend("test")
# li.extend(("some","times"))
# li.insert(2,"插入的元素")
# print(li)


'''
pop() 
# 删除指定下标的元素，默认删除最后一个元素
# 返回被删除的元素
remove()
# 删除列表的元素
# 删除的元素不存在会报错
# 删除元素后，返回值为空


clear()
# 清空列表
'''

# li = [1,2,3,4,5,6,7,8]
# a = li.pop()
# b = li.pop(3)
# print(li)
# print(a,b)
#
# c = li.remove(2)
# print(li,c)
#
# li.clear()
# print(li)

'''
reverse() # 列表反转
sort() # 列表排序
# 默认升序
# 通过reverse=True|Flase来控制
'''

# li = [1,2,3,4,5,6]
# li.reverse()
# print(li)
#
#
# l1 = [1,2,4,5,6,2]
# l2 = ['a','test','cd']
# l3 = ['a','test','cd']
# l1.sort()
# l2.sort(reverse=True)
# l3.sort(reverse=False)
# print(l1)
# print(l2)
# print(l3)


'''
列表的切片操作
li[start:end]

'''

li = ["name", 1,2,3, "test"]
print(li[1])
print(li[1:])
print(li[:1])
print(li[1:3])
print(li[-2])
print(li[-3:-1])

del li[0] #删除列表的某个元素
print(li)