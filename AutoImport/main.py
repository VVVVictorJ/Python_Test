import os
import xlrd
import sys
import io
import uuid
import getpass
import datetime
from xlrd import xldate_as_tuple
from LogUtils import Log
from dbUtils import MutilpleDatabaseOperation
from fileUtils import FileUtils

LogPath = FileUtils.getConfigValue()["LOGPATH"]
FilePath = FileUtils.getConfigValue()["FILEPATH"]

log = Log(getpass.getuser(), LogPath).getlog()

# 创建日志目录
if os.path.exists(LogPath):
    log.info("日志目录已存在")
else:
    try:
        os.makedirs(LogPath)
        log.info("创建日志目录成功")
    except Exception as e:
        log.error(e)

# 防止乱码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf8")

obj = MutilpleDatabaseOperation()

for filepath in [
    os.path.join(FilePath, file)
    for file in os.listdir(FilePath)
    if os.path.isfile(os.path.join(FilePath, file))
    and file.endswith(".xls")
]:
    workbook = xlrd.open_workbook(
        filepath,
        formatting_info=True,
    )
    uuidstr = uuid.uuid1()
    sheet1_object = workbook.sheet_by_name(str(FileUtils.getConfigValue()["SHEETNAME"]))
    obj.delete(str(sheet1_object.cell_value(1, 1)))
    obj.delete1(str(sheet1_object.cell_value(1, 1)))

    obj.write_to_db(
        uuidstr,
        sheet1_object.cell_value(1, 1),
        sheet1_object.cell_value(1, 4),
        sheet1_object.cell_value(1, 7),
        datetime.datetime(*xldate_as_tuple(sheet1_object.cell_value(1, 10), 0)).strftime('%Y-%m-%d'),
        sheet1_object.cell_value(2, 1),
        sheet1_object.cell_value(2, 4),
        datetime.datetime(*xldate_as_tuple(sheet1_object.cell_value(2, 7), 0)).strftime('%Y-%m-%d'),
        datetime.datetime(*xldate_as_tuple(sheet1_object.cell_value(2, 10), 0)).strftime('%Y-%m-%d'),
        sheet1_object.cell_value(3, 1),
        sheet1_object.cell_value(3, 4),
        datetime.datetime(*xldate_as_tuple(sheet1_object.cell_value(3, 7), 0)).strftime('%Y-%m-%d'),
        datetime.datetime(*xldate_as_tuple(sheet1_object.cell_value(3, 10), 0)).strftime('%Y-%m-%d'),
        sheet1_object.cell_value(4, 1),
        sheet1_object.cell_value(4, 4),
        sheet1_object.cell_value(4, 7),
        sheet1_object.cell_value(4, 10),
        sheet1_object.cell_value(6, 0),
        sheet1_object.cell_value(6, 5),
        sheet1_object.cell(6, 11).value,
    )

    n = 8
    nn = 8
    len = 0
    while True:
        if sheet1_object.cell(nn, 0).value == "":
            break
        nn = nn + 1
        len = len + 1

    for i in range(len):
        uuidstr = uuid.uuid1()
        obj.write_to_db1(
            uuidstr,
            sheet1_object.cell_value(1, 1),
            sheet1_object.cell(n, 0).value,
            sheet1_object.cell(n, 1).value,
            sheet1_object.cell(n, 2).value,
            sheet1_object.cell(n, 3).value,
            sheet1_object.cell(n, 4).value,
            datetime.datetime(*xldate_as_tuple(sheet1_object.cell(n, 5).value, 0)).strftime('%Y-%m-%d'),
            sheet1_object.cell(n, 6).value,
            datetime.datetime(*xldate_as_tuple(sheet1_object.cell(n, 7).value, 0)).strftime('%Y-%m-%d'),
            sheet1_object.cell(n, 8).value,
            sheet1_object.cell(n, 9).value,
            sheet1_object.cell(n, 10).value,
            sheet1_object.cell(n, 11).value,
        )
        n = n + 1

# log.info("导入完毕")
obj.close()
os.system("pause")

