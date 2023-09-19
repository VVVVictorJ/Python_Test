import xlrd
from fileUtils import FileUtils

filepath = f'C:\\Users\\PastoreMaxwell\\Desktop\\shit\\excel\\模板\\项目号_项目名称_部门_周汇报（新版）.xls'

workbook = xlrd.open_workbook(
    filepath,
    formatting_info=True,
)

sheet = workbook.sheet_by_name("20230921")

merged = sheet.merged_cells 
#起始行，结束行，起始列，结束列
#rlow, rhigh, clow, chigh
# for (i, (rlow, rhigh, clow, chigh)) in enumerate(merged):
#     print(i, rlow, rhigh, clow, chigh)
print("本周计划:\n", sheet.cell_value(6, 1), end='\n\n')
print("本周实绩:\n", sheet.cell_value(6, 4), end='\n\n')
print("下周工作计划:\n", sheet.cell_value(6, 7), end='\n\n')
print("备注:\n", sheet.cell_value(6, 10))
# def get_cell_type(row_index, col_index):
#     """既能得到合并单元格也能得到普通单元格"""
#     cell_value = None
#     for (rlow, rhigh, clow, chigh) in merged:  # 遍历表格中所有合并单元格位置信息
#         # print(rlow,rhigh,clow,chigh)
#         if (row_index >= rlow and row_index < rhigh):  # 行坐标判断
#             if (col_index >= clow and col_index < chigh):  # 列坐标判断
#                 # 如果满足条件，就把合并单元格第一个位置的值赋给其它合并单元格
#                 cell_value = sheet.cell_value(rlow, clow)
#                 print('合并单元格')
#                 break  # 不符合条件跳出循环，防止覆盖
#             else:
#                 print('普通单元格')
#                 cell_value = sheet.cell_value(row_index, col_index)
 
#         # else:  添加改行后只那一个单元格的内容5，0 会返回2个值普通单元格/合并单元格
#         #     print('普通单元格')
#         #     cell_value = sheet.cell_value(row_index, col_index)
 
#     return cell_value
 
 
# # 直接输入单元格的坐标。来获取单元格内容
# # print(get_cell_type(5, 0))
 
# # 利用循环输出某列的单元格内容
# for i in range(1, 9):
#     print(get_cell_type(i, 2))