import os
from collections import defaultdict

import xlrd
from fileUtils import FileUtils
from tqdm import tqdm
from xlrd import xldate_as_tuple

FilePath = FileUtils.getConfigValue()["FILEPATH"]
SheetName = str(FileUtils.getConfigValue()["SHEETNAME"])

create_dict = lambda key, value: {key: value}

filelist = [
    os.path.join(FilePath, file)
    for file in os.listdir(FilePath)
    if os.path.isfile(os.path.join(FilePath, file)) and file.endswith(".xls")
]
print("Before:{}".format(len(filelist)))

errorFileList = []

# 上半区校验
for k, filepath in tqdm(
    enumerate(filelist),
    desc="Processing xls files",
    total=len(filelist),
    ncols=100,
    ascii=False,
):
    workbook = xlrd.open_workbook(
        filepath,
        formatting_info=True,
    )
    sheet1_object = workbook.sheet_by_name(SheetName)
    # print(*xldate_as_tuple(sheet1_object.cell_value(1, 10), 0))
    # 项目开始时间单元格类型校验
    if sheet1_object.cell(1, 10).ctype != 3:
        errorFileList.append(
            create_dict(
                str(sheet1_object.cell_value(1, 1)), "项目开始时间填写错误, 请检查格式以及是否为正常日期。"
            )
        )
        filelist.pop(k)
    # 阶段开始时间单元格校验
    if sheet1_object.cell(2, 7).ctype != 3:
        errorFileList.append(
            create_dict(
                str(sheet1_object.cell_value(1, 1)), "阶段开始时间填写错误, 请检查格式以及是否为正常日期。"
            )
        )
        filelist.pop(k)
    if sheet1_object.cell(2, 10).ctype != 3:
        errorFileList.append(
            create_dict(
                str(sheet1_object.cell_value(1, 1)), "项目结束时间填写错误, 请检查格式以及是否为正常日期。"
            )
        )
        filelist.pop(k)
    if sheet1_object.cell(3, 7).ctype != 3:
        errorFileList.append(
            create_dict(
                str(sheet1_object.cell_value(1, 1)), "阶段结束时间填写错误, 请检查格式以及是否为正常日期。"
            )
        )
        filelist.pop(k)
    if sheet1_object.cell(3, 10).ctype != 3:
        errorFileList.append(
            create_dict(
                str(sheet1_object.cell_value(1, 1)), "交工验收结束时间填写错误, 请检查格式以及是否为正常日期。"
            )
        )
        filelist.pop(k)

problems = []

for k, filepath in tqdm(
    enumerate(filelist),
    desc="Processing xls files",
    total=len(filelist),
    ncols=100,
    ascii=False,
):
    # for k, filepath in enumerate(filelist):
    workbook = xlrd.open_workbook(
        filepath,
        formatting_info=True,
    )
    sheet1_object = workbook.sheet_by_name(SheetName)

    n = 8
    nn = 8
    len1 = 0
    d = defaultdict(list)
    while True:
        if sheet1_object.cell(nn, 0).value == "":
            break
        else:
            nn = nn + 1
            len1 = len1 + 1
            d[filepath].append(nn)
    # for k, v in d.items():
    #     print(type(d[k][0]))
    if len(d) > 0:
        problems.append(d)
    
# print(len(problems))
# for i in problems:
#     for k, v in i.items():
#         for i in v:
#             print(i, end='\t')
#         print()

# for k, v in enumerate(problems):
#     print(v)

    # tmp_list = [i for i in range(n, len1 + n)]

    # 下半区校验
for key, i in tqdm(
    enumerate(problems),
    desc="PreProcessing {} project_problems_record".format(
        sheet1_object.cell_value(1, 1)
    ),
    total=len(problems),
    ncols=100,
    ascii=False,
):
    for k, v in i.items():
        print(key, k)
        for i in v:
            print(i, end='\t')
        print()
    # # for k, v in enumerate(tmp_list):
    # # 存在风险或问题
    # print(sheet1_object.cell(v, 0).value)
    # # 解决方案、建议
    # print(sheet1_object.cell(v, 1).value)
    # # 问题进展情况
    # print(sheet1_object.cell(v, 2).value)
    # # 问题严重程度
    # print(sheet1_object.cell(v, 3).value)
    # # 责任人
    # print(sheet1_object.cell(v, 4).value)
    # # 预计解决时间
    # print(sheet1_object.cell(v, 5).value)
    # # 问题状态
    # print(sheet1_object.cell(v, 6).ctype)
    # # 提出时间
    # print(sheet1_object.cell(v, 7).value)
    # # 实际解决时间
    # print(sheet1_object.cell(v, 8).ctype)
    # # 未解决原因
    # print(sheet1_object.cell(v, 9).ctype)
    # # 确认人
    # print(sheet1_object.cell(v, 10).ctype)
    # # 部门处理意见
    # print(sheet1_object.cell(v, 11).ctype)
            # if sheet1_object.cell(i, 0).value == "无":
            #     continue
            # else:
            #     if sheet1_object.cell(i, 5).ctype != 3:
            #         errorFileList.append(
            #             create_dict(
            #                 str(sheet1_object.cell_value(1, 1)),
            #                 "预计解决时间填写错误, 请检查格式以及是否为正常日期。",
            #             )
            #         )
            #     if sheet1_object.cell(i, 7).ctype != 3:
            #         errorFileList.append(
            #             create_dict(
            #                 str(sheet1_object.cell_value(1, 1)), "提出时间填写错误, 请检查格式以及是否为正常日期。"
            #             )
            #         )
            #     if (
            #         sheet1_object.cell(i, 8).ctype != 3
            #         and sheet1_object.cell(i, 8).ctype != 6
            #     ):
            #         errorFileList.append(
            #             create_dict(
            #                 str(sheet1_object.cell_value(1, 1)),
            #                 "实际解决时间填写错误, 请检查格式以及是否为正常日期。",
            #             )
            #         )

        # print("After:{}".format(str(len1(filelist))))

for i in errorFileList:
    print(
        "导入失败的项目编号为{}\n报错信息:{}".format(
            (lambda d: d.keys())(i), (lambda d: d.values())(i)
        )
    )
