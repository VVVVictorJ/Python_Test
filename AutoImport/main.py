import datetime
import getpass
import io
import os
import sys
import uuid

import xlrd
from dbUtils import MutilpleDatabaseOperation
from fileUtils import FileUtils
from LogUtils import Log
from processModule import processModule
from tqdm import tqdm
from xlrd import xldate_as_tuple

LogPath = FileUtils.getConfigValue()["LOGPATH"]
FilePath = FileUtils.getConfigValue()["FILEPATH"]
SheetName = str(FileUtils.getConfigValue()["SHEETNAME"])

log = Log(getpass.getuser(), LogPath).getlog()

create_dict = lambda key, value: {key: value}

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

# obj = MutilpleDatabaseOperation()
filelist = [
    os.path.join(FilePath, file)
    for file in os.listdir(FilePath)
    if os.path.isfile(os.path.join(FilePath, file)) and file.endswith(".xls")
]
errorFileList = []

problems_record = []

processObj = processModule()

errorFileList = processObj.Process(filelist, SheetName)

for i in errorFileList:
    # print(
    #     "导入失败的项目编号为{}\n报错信息:{}".format(
    #         list((lambda d: d.keys())(i))[0], list((lambda d: d.values())(i))[0]
    #     )
    # )
    log.error(
        "导入失败的项目编号为{}\n报错信息:{}".format(
            list((lambda d: d.keys())(i))[0], list((lambda d: d.values())(i))[0]
        )
    )
# os.system("pause")
