import datetime
import uuid
from collections import defaultdict

import xlrd
from dbUtils import MutilpleDatabaseOperation
from tqdm import tqdm
from xlrd import xldate_as_tuple

create_dict = lambda key, value: {key: value}


class processModule:
    def Process(self, fileList: list, SheetName):
        """
        Process the given file list and sheet name.

        Args:
            fileList (list): A list of files to process.
            SheetName: The name of the sheet to process.

        Returns:
            The result of calling the PreprocessWeeklyReport method with the given file list and sheet name.
        """
        return self.PreprocessWeeklyReport(fileList, SheetName)

    def PreprocessWeeklyReport(self, fileList: list, SheetName):
        """
        Preprocesses a weekly report.

        Args:
            fileList (list): A list of file paths.
            SheetName: The name of the sheet in the workbook.

        Returns:
            list: A list of errors encountered during preprocessing.
        """
        errorList = []
        problems_record = []
        for filepath in tqdm(
            fileList,
            desc="Preprocessing xls files Weekly Report",
            # total=len(fileList),
            ncols=100,
            ascii=False,
        ):
            # print(filepath)
            workbook = xlrd.open_workbook(
                filepath,
                formatting_info=True,
            )
            sheet1_object = workbook.sheet_by_name(SheetName)
            if sheet1_object.cell(1, 10).ctype != 3:
                errorList.append(
                    create_dict(
                        str(sheet1_object.cell_value(1, 1)),
                        "项目开始时间填写错误, 请检查格式以及是否为正常日期。",
                    )
                )
            # 阶段开始时间单元格校验
            if sheet1_object.cell(2, 7).ctype != 3:
                errorList.append(
                    create_dict(
                        str(sheet1_object.cell_value(1, 1)),
                        "阶段开始时间填写错误, 请检查格式以及是否为正常日期。",
                    )
                )
            # 项目结束时间单元格校验
            if sheet1_object.cell(2, 10).ctype != 3:
                errorList.append(
                    create_dict(
                        str(sheet1_object.cell_value(1, 1)),
                        "项目结束时间填写错误, 请检查格式以及是否为正常日期。",
                    )
                )
            # 阶段结束时间单元格校验
            # print(sheet1_object.cell(3, 7).ctype)
            if sheet1_object.cell(3, 7).ctype != 3:
                errorList.append(
                    create_dict(
                        str(sheet1_object.cell_value(1, 1)),
                        "阶段结束时间填写错误, 请检查格式以及是否为正常日期。",
                    )
                )
            # 交工验收结束时间单元格校验
            if sheet1_object.cell(3, 10).ctype != 3:
                errorList.append(
                    create_dict(
                        str(sheet1_object.cell_value(1, 1)),
                        "交工验收结束时间填写错误, 请检查格式以及是否为正常日期。",
                    )
                )

            n = 8
            nn = 8
            length = 0
            recordsIndexList = defaultdict(list)
            recordsIndexList[filepath].append(nn)
            while True:
                if sheet1_object.cell(nn, 0).value == "":
                    break
                else:
                    nn = nn + 1
                    length = length + 1
                    recordsIndexList[filepath].append(nn)
            # print(recordsIndexList)

            if len(recordsIndexList) > 0:
                recordsIndexList["projectId"] = str(sheet1_object.cell_value(1, 1))
                problems_record.append(recordsIndexList)

            # print(problems_record)
        return self.PreProcessProblemsRecord(errorList, problems_record, SheetName)

    def PreProcessProblemsRecord(self, errorList, problems_record, SheetName):
        """
        Preprocesses the problems record by iterating through the `problems_record` list and performing various operations on each item. It opens each file in `problems_record` using `xlrd` library, retrieves the specified sheet named `SheetName`, and checks the values of certain cells for validity. It appends the filepath to `filelist` if the value in the first cell of the current row is "无". It also checks the format and validity of the values in the cells representing the expected resolution time, the submission time, and the actual resolution time. If any of these values are incorrect, an error message is appended to `errorList`. After iterating through all items, it removes any items from `problems_record` that had errors. Finally, it calls the `ProcessFileWeeklyReport` method with the updated `problems_record`, `errorList`, and `SheetName` as arguments and returns the result.

        :param errorList: A list to store error messages.
        :type errorList: list
        :param problems_record: The list of problems records.
        :type problems_record: list
        :param SheetName: The name of the sheet to retrieve from each file.
        :type SheetName: str
        :return: The result of the `ProcessFileWeeklyReport` method.
        :rtype: unknown
        """
        filelist = []
        # print(len(problems_record))
        for key, item in tqdm(
            enumerate(problems_record),
            desc="PreProcessing xls files Problems Record",
            total=len(problems_record),
            ncols=100,
            ascii=False,
        ):
            for filepath, problemsIndexList in item.items():
                # print("filepath is {}, problemsIndexList is {}".format(filepath, problemsIndexList))
                if filepath != "projectId":
                    workbook = xlrd.open_workbook(
                        filepath,
                        formatting_info=True,
                    )
                    # print(filepath)
                    sheet1_object = workbook.sheet_by_name(SheetName)
                    flag = False
                    # print(problemsIndexList[2])
                    for item in range(
                        problemsIndexList[0],
                        problemsIndexList[0] + len(problemsIndexList) - 1,
                    ):
                        # print(item)
                        # print(sheet1_object.cell(item, 0).value)
                        # # 解决方案、建议
                        # print(sheet1_object.cell(item, 1).value)
                        # # 问题进展情况
                        # print(sheet1_object.cell(item, 2).value)
                        # # 问题严重程度
                        # print(sheet1_object.cell(item, 3).value)
                        # # 责任人
                        # print(sheet1_object.cell(item, 4).value)
                        # # 预计解决时间
                        # print(sheet1_object.cell(item, 5).value)
                        # # 问题状态
                        # print(sheet1_object.cell(item, 6).ctype)
                        # # 提出时间
                        # print(sheet1_object.cell(item, 7).value)
                        # # 实际解决时间
                        # print(sheet1_object.cell(item, 8).ctype)
                        # # 未解决原因
                        # print(sheet1_object.cell(item, 9).ctype)
                        # # 确认人
                        # print(sheet1_object.cell(item, 10).ctype)
                        # # 部门处理意见
                        # print(sheet1_object.cell(item, 11).ctype)
                        # print(sheet1_object.cell_value(6, 4))
                        if sheet1_object.cell(item, 0).value == "无":
                            filelist.append(filepath)
                            continue
                        else:
                            # print(sheet1_object.cell(item, 5).value)
                            if sheet1_object.cell(item, 5).ctype != 3:
                                errorList.append(
                                    create_dict(
                                        str(sheet1_object.cell_value(1, 1)),
                                        "预计解决时间填写错误, 请检查格式以及是否为正常日期。",
                                    )
                                )
                                flag = True
                                # problems_record.pop(key)
                                # break
                            if sheet1_object.cell(item, 7).ctype != 3:
                                errorList.append(
                                    create_dict(
                                        str(sheet1_object.cell_value(1, 1)),
                                        "提出时间填写错误, 请检查格式以及是否为正常日期。",
                                    )
                                )
                                flag = True
                                # problems_record.pop(key)
                                # break
                            if (
                                sheet1_object.cell(item, 8).ctype != 3
                                and sheet1_object.cell(item, 8).ctype != 6
                            ):
                                errorList.append(
                                    create_dict(
                                        str(sheet1_object.cell_value(1, 1)),
                                        "实际解决时间填写错误, 请检查格式以及是否为正常日期。",
                                    )
                                )
                                flag = True
                                # problems_record.pop(key)
                                # break
                            if flag:
                                problems_record.pop(key)
                            flag = False

            for k, v in enumerate(problems_record):
                for i in errorList:
                    # print("errorlist item key is {}, projectid is {}".format(list((lambda d: d.keys())(i))[0], v['projectId']))
                    if list((lambda d: d.keys())(i))[0] == v["projectId"]:
                        problems_record.pop(k)

        return self.ProcessFileWeeklyReport(problems_record, errorList, SheetName)
        # return self.ProcessFile(filelist, errorList)

    def ProcessFileWeeklyReport(self, problems_record, errorList, SheetName):
        """
        Process the weekly report file.

        Args:
            problems_record (list): A list of dictionaries representing the problems recorded.
            errorList (list): A list to store any errors encountered during processing.
            SheetName (str): The name of the sheet in the workbook.

        Returns:
            str: The result of calling the ProcessFileProblemRecord function.
        """
        obj = MutilpleDatabaseOperation()
        for key, item in tqdm(
            enumerate(problems_record),
            desc="Processing xls files ",
            total=len(problems_record),
            ncols=100,
            ascii=False,
        ):
            for filepath, problemsIndexList in item.items():
                # print("filepath is {}, problemsIndexList is {}".format(filepath, problemsIndexList))
                if filepath != "projectId":
                    workbook = xlrd.open_workbook(
                        filepath,
                        formatting_info=True,
                    )
                    # print(filepath)
                    sheet1_object = workbook.sheet_by_name(SheetName)
                    uuidstr = uuid.uuid1()
                    obj.delete(str(sheet1_object.cell_value(1, 1)), SheetName)
                    obj.delete1(str(sheet1_object.cell_value(1, 1)), SheetName)

                    try:
                        obj.write_to_db(
                            uuidstr,
                            SheetName,
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
                            sheet1_object.cell_value(6, 1),
                            sheet1_object.cell_value(6, 4),
                            sheet1_object.cell_value(6, 7),
                            sheet1_object.cell_value(6, 10),
                        )
                    except Exception as e:
                        errorList.append(
                            create_dict(str(sheet1_object.cell_value(1, 1)), str(e))
                        )
                        problems_record.pop(key)
            obj.close()
        return self.ProcessFileProblemRecord(problems_record, errorList, SheetName)

    def ProcessFileProblemRecord(self, problems_record, errorList, SheetName):
        """
        Process the given problems record and write the data to a database.

        Parameters:
        - problems_record: A list of dictionaries containing information about problems and file paths.
        - errorList: A list to store any encountered errors.
        - SheetName: The name of the sheet to read from the workbook.

        Returns:
        - errorList: A list of dictionaries containing error messages.

        This function processes each item in the problems_record list. For each item, it iterates over the file paths and performs the following steps:
        - Opens the workbook using the filepath.
        - Retrieves the sheet object using the SheetName.
        - Generates a unique UUID.
        - Iterates over the range of the problemsIndexList.
        - Checks conditions based on cell values and types.
        - Calls the write_to_db1 method of the MutilpleDatabaseOperation object with the necessary arguments.
        - Appends any encountered errors to the errorList.

        Finally, the function closes the MutilpleDatabaseOperation object and returns the errorList.
        """
        obj = MutilpleDatabaseOperation()
        for key, item in tqdm(
            enumerate(problems_record),
            desc="Processing xls files ",
            total=len(problems_record),
            ncols=100,
            ascii=False,
        ):
            for filepath, problemsIndexList in item.items():
                # print("filepath is {}, problemsIndexList is {}".format(filepath, problemsIndexList))
                if filepath != "projectId":
                    workbook = xlrd.open_workbook(
                        filepath,
                        formatting_info=True,
                    )
                    # print(filepath)
                    sheet1_object = workbook.sheet_by_name(SheetName)
                    uuidstr = uuid.uuid1()
                    for item in range(
                        problemsIndexList[0],
                        problemsIndexList[0] + len(problemsIndexList) - 1,
                    ):
                        uuidstr = uuid.uuid1()
                        if (
                            sheet1_object.cell(item, 0).value == "无"
                            and sheet1_object.cell(item, 5).ctype == 6
                            and sheet1_object.cell(item, 7).ctype == 6
                            and sheet1_object.cell(item, 8).ctype == 6
                        ):
                            try:
                                obj.write_to_db1(
                                    uuidstr,
                                    SheetName,
                                    sheet1_object.cell_value(1, 1),
                                    sheet1_object.cell(item, 0).value,
                                    sheet1_object.cell(item, 1).value,
                                    sheet1_object.cell(item, 2).value,
                                    sheet1_object.cell(item, 3).value,
                                    sheet1_object.cell(item, 4).value,
                                    sheet1_object.cell(item, 5).value,
                                    sheet1_object.cell(item, 6).value,
                                    sheet1_object.cell(item, 7).value,
                                    sheet1_object.cell(item, 8).value,
                                    sheet1_object.cell(item, 9).value,
                                    sheet1_object.cell(item, 10).value,
                                    sheet1_object.cell(item, 11).value,
                                )
                            except Exception as e:
                                errorList.append(
                                    create_dict(
                                        str(sheet1_object.cell_value(1, 1)), str(e)
                                    )
                                )
                        elif (
                            sheet1_object.cell(item, 5).ctype == 3
                            and sheet1_object.cell(item, 7).ctype == 6
                            and sheet1_object.cell(item, 8).ctype == 6
                        ):
                            try:
                                obj.write_to_db1(
                                    uuidstr,
                                    SheetName,
                                    sheet1_object.cell_value(1, 1),
                                    sheet1_object.cell(item, 0).value,
                                    sheet1_object.cell(item, 1).value,
                                    sheet1_object.cell(item, 2).value,
                                    sheet1_object.cell(item, 3).value,
                                    sheet1_object.cell(item, 4).value,
                                    datetime.datetime(
                                        *xldate_as_tuple(
                                            sheet1_object.cell(item, 5).value, 0
                                        )
                                    ).strftime("%Y-%m-%d"),
                                    sheet1_object.cell(item, 6).value,
                                    sheet1_object.cell(item, 7).value,
                                    sheet1_object.cell(item, 8).value,
                                    sheet1_object.cell(item, 9).value,
                                    sheet1_object.cell(item, 10).value,
                                    sheet1_object.cell(item, 11).value,
                                )
                            except Exception as e:
                                errorList.append(
                                    create_dict(
                                        str(sheet1_object.cell_value(1, 1)), str(e)
                                    )
                                )
                        elif (
                            sheet1_object.cell(item, 5).ctype == 3
                            and sheet1_object.cell(item, 7).ctype == 3
                            and sheet1_object.cell(item, 8).ctype == 3
                        ):
                            try:
                                obj.write_to_db1(
                                    uuidstr,
                                    SheetName,
                                    sheet1_object.cell_value(1, 1),
                                    sheet1_object.cell(item, 0).value,
                                    sheet1_object.cell(item, 1).value,
                                    sheet1_object.cell(item, 2).value,
                                    sheet1_object.cell(item, 3).value,
                                    sheet1_object.cell(item, 4).value,
                                    datetime.datetime(
                                        *xldate_as_tuple(
                                            sheet1_object.cell(item, 5).value, 0
                                        )
                                    ).strftime("%Y-%m-%d"),
                                    sheet1_object.cell(item, 6).value,
                                    datetime.datetime(
                                        *xldate_as_tuple(
                                            sheet1_object.cell(item, 7).value, 0
                                        )
                                    ).strftime("%Y-%m-%d"),
                                    datetime.datetime(
                                        *xldate_as_tuple(
                                            sheet1_object.cell(item, 8).value, 0
                                        )
                                    ).strftime("%Y-%m-%d"),
                                    sheet1_object.cell(item, 9).value,
                                    sheet1_object.cell(item, 10).value,
                                    sheet1_object.cell(item, 11).value,
                                )
                            except Exception as e:
                                errorList.append(
                                    create_dict(
                                        str(sheet1_object.cell_value(1, 1)), str(e)
                                    )
                                )
                        elif (
                            sheet1_object.cell(item, 5).ctype == 3
                            and sheet1_object.cell(item, 7).ctype == 3
                            and sheet1_object.cell(item, 8).ctype != 3
                            and sheet1_object.cell(item, 8).ctype == 6
                        ):
                            try:
                                obj.write_to_db1(
                                    uuidstr,
                                    SheetName,
                                    sheet1_object.cell_value(1, 1),
                                    sheet1_object.cell(item, 0).value,
                                    sheet1_object.cell(item, 1).value,
                                    sheet1_object.cell(item, 2).value,
                                    sheet1_object.cell(item, 3).value,
                                    sheet1_object.cell(item, 4).value,
                                    datetime.datetime(
                                        *xldate_as_tuple(
                                            sheet1_object.cell(item, 5).value, 0
                                        )
                                    ).strftime("%Y-%m-%d"),
                                    sheet1_object.cell(item, 6).value,
                                    datetime.datetime(
                                        *xldate_as_tuple(
                                            sheet1_object.cell(item, 7).value, 0
                                        )
                                    ).strftime("%Y-%m-%d"),
                                    sheet1_object.cell(item, 8).value,
                                    sheet1_object.cell(item, 9).value,
                                    sheet1_object.cell(item, 10).value,
                                    sheet1_object.cell(item, 11).value,
                                )
                            except Exception as e:
                                errorList.append(
                                    create_dict(
                                        str(sheet1_object.cell_value(1, 1)), str(e)
                                    )
                                )
        obj.close()
        return errorList
