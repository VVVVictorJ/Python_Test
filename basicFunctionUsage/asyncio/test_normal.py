import asyncio
import datetime
import os
import time
import uuid
from collections import defaultdict

import xlrd
from dbUtils import MutilpleDatabaseOperation
from xlrd import xldate_as_tuple

FilePath = f"C:\\Users\\PastoreMaxwell\\Desktop\\shit\\fuck\\20230825"
errorList = []
create_dict = lambda key, value: {key: value}

def open(filepath):
    obj = MutilpleDatabaseOperation()
    workbook = xlrd.open_workbook(
        filepath,
        formatting_info=True,
    )
    sheet1_object = workbook.sheet_by_name("20230821")
    uuidstr = uuid.uuid1()
    try:
        obj.delete(str(sheet1_object.cell_value(1, 1)), "20230821")
        obj.delete1(str(sheet1_object.cell_value(1, 1)), "20230821")
        obj.write_to_db1(
            uuidstr,
            "20230821",
            sheet1_object.cell_value(1, 1),
            sheet1_object.cell_value(1, 4),
            sheet1_object.cell_value(1, 7),
            datetime.datetime(
                *xldate_as_tuple(sheet1_object.cell_value(1, 10), 0)
            ).strftime("%Y-%m-%d"),
            sheet1_object.cell_value(2, 1),
            sheet1_object.cell_value(2, 4),
            datetime.datetime(
                *xldate_as_tuple(sheet1_object.cell_value(2, 7), 0)
            ).strftime("%Y-%m-%d"),
            datetime.datetime(
                *xldate_as_tuple(sheet1_object.cell_value(2, 10), 0)
            ).strftime("%Y-%m-%d"),
            sheet1_object.cell_value(3, 1),
            sheet1_object.cell_value(3, 4),
            datetime.datetime(
                *xldate_as_tuple(sheet1_object.cell_value(3, 7), 0)
            ).strftime("%Y-%m-%d"),
            datetime.datetime(
                *xldate_as_tuple(sheet1_object.cell_value(3, 10), 0)
            ).strftime("%Y-%m-%d"),
            sheet1_object.cell_value(4, 1),
            sheet1_object.cell_value(4, 4),
            sheet1_object.cell_value(4, 7),
            sheet1_object.cell_value(4, 10),
            sheet1_object.cell_value(6, 0),
            sheet1_object.cell_value(6, 5),
            sheet1_object.cell(6, 11).value,
        )
    except Exception as e:
        errorList.append(create_dict(str(sheet1_object.cell_value(1, 1)), str(e)))


def main():
    filelist = [
        os.path.join(FilePath, file)
        for file in os.listdir(FilePath)
        if os.path.isfile(os.path.join(FilePath, file)) and file.endswith(".xls")
    ]
    for filepath in filelist:
        open(filepath)


# async def open(filepath):
#     workbook = xlrd.open_workbook(
#         filepath,
#         formatting_info=True,
#     )
#     sheet1_object = workbook.sheet_by_name("20230821")
#     print(sheet1_object.cell_value(1, 1))


# async def main():
#     filelist = [
#         os.path.join(FilePath, file)
#         for file in os.listdir(FilePath)
#         if os.path.isfile(os.path.join(FilePath, file)) and file.endswith(".xls")
#     ]
#     tasks = [asyncio.create_task(open(filepath)) for filepath in filelist]
#     for task in tasks:
#         await task

start_time = time.perf_counter()
main()
# asyncio.run(main())
end_time = time.perf_counter()

print("总共耗时:{}".format(end_time - start_time))
