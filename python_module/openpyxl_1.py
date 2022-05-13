import shelve
from tkinter import W
from openpyxl import Workbook
import time

from pyparsing import col

'''
Excel文件的创建和数据写入保存
'''


# 创建工作簿
book = Workbook()
# 获取对活动工作表的引用
sheet1 = book.active

'''
openpyxl写入单元格的两种基本方法：
1.使用工作表的键（例如 A1 或 D3）
2.通过cell()方法使用行和列表示法
'''
sheet1['A1'] = 56
sheet1['A2'] = 43
now = time.strftime('%X')
sheet1['A3'] = now

sheet1.cell(row=2, column=2).value = "测试测试"

'''
使用append()方法，我们可以在当前工作表的底部附加一组值
'''

row1 = ("用例目录",'用例标题','操作步骤','预期结果','实际结果')
sheet1.append(row1)

rows = (
    (88, 46, 57),
    (89, 38, 12),
    (23, 59, 78),
    (56, 21, 98),
    (24, 18, 43),
    (34, 15, 67)
)

# 逐行浏览容器，并使用append()方法插入数据行
for row in rows:
    sheet1.append(row)
# save() 将写入的内容保存到Excel
book.save("sample.xlsx")