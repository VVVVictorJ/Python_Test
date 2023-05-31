import logging
from functools import wraps

import pandas as pd
from FormatString import AutoFormatSqlGenarator

logging.basicConfig(
    filename="example.log",
    encoding="utf-8",
    level=logging.DEBUG,
)


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        from time import time

        t_start = time()
        result = func(*args, **kwargs)
        t_end = time()
        # print("time spend: {}".format(t_end - t_start))
        logging.debug(
            "Function {:<20}, Using Time: {} s".format(func.__name__, t_end - t_start)
        )
        return result

    return wrapper


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.debug("Function {} is running.".format(func.__name__))
        result = func(*args, **kwargs)
        logging.debug("Function {} is finising.\n".format(func.__name__))
        return result

    return wrapper


class ProcessExcel:
    @log
    @timer
    def __init__(self, InputFileLocation: str, SheetName: str = "Sheet1") -> None:
        self.InputFileLocation = InputFileLocation
        self.DataFrame = pd.read_excel(InputFileLocation, sheet_name="Sheet1")
        # excel 纵列标题
        self.ColumnsTitle = []
        self.DataSet = {}
        self.getTitle()
        self.getDataFromTitle()

    @timer
    def getTitle(self):
        # print(self.DataFrame.columns)
        for k, v in enumerate(self.DataFrame.columns):
            # print("key is {}, value is {}".format(k + 1, v))
            self.ColumnsTitle.append(v)

    @timer
    def getDataFromTitle(self):
        for i in range(len(self.ColumnsTitle)):
            self.DataSet[self.ColumnsTitle[i]] = list(
                pd.Series(self.DataFrame[self.ColumnsTitle[i]].fillna("''").values)
            )

    @timer
    def setTitle():
        pass

    @timer
    def GetData(self) -> dict:
        return self.DataSet

    @timer
    def PackToDict(self) -> dict:
        """按行读取生成字典

        Returns:
            dict: key值为行数, value为Excel 一行的值
        """
        keys = [x for x in range(self.GetRowsCount())]
        values = []
        for i in range(self.GetRowsCount()):
            value = []
            for j in self.DataSet.keys():
                value.append(self.DataSet.get(j)[i])
            values.append(value)
        return dict(zip(keys, values))

    @timer
    def GetKeySet(self) -> list:
        """返回标签值

        Returns:
            list: 列标签值
        """
        return list(self.DataSet.keys())

    @timer
    @staticmethod
    def SGetRowsCount(param: dict) -> int:
        """staticmethod

        Args:
            param (dict): 字典

        Returns:
            int: 返回字典的长度, 既当前Excel的行数
        """
        return len(next(iter(param.values())))

    @timer
    @staticmethod
    def SGetColumnsCount(param: dict) -> int:
        """staticmethod

        Args:
            param (dict): 字典

        Returns:
            int: 返回字典的Key的个数, 即当前Excel的列数
        """
        return len(param.keys())

    @timer
    # 返回行数
    def GetRowsCount(self) -> int:
        return len(next(iter(self.DataSet.values())))

    @timer
    # 返回列数
    def GetColumnsCount(self) -> int:
        return len(self.DataSet.keys())


if __name__ == "__main__":
    # obj = ProcessExcel("E:\\code\\Python\\ProcessExcel\\src\\test.xlsx")
    obj = ProcessExcel("E:\\code\\Python\\ProcessExcel\\src\\合同备案.xlsx")
    print("Index is : {}".format(obj.GetKeySet()))
    print("Excel has {} rows".format(obj.GetRowsCount()))
    print("Excel has {} columns(index)".format(obj.GetColumnsCount()))
    # tmp = AutoFormatSqlGenarator("select {0[0]},{0[1]},{0[2]},{0[3]},{0[4]} from test")
    tmp = AutoFormatSqlGenarator(
        """UPDATE {0[0]} SET REC_CREATE_TIME = '{0[1]}'
        WHERE 
        REC_CREATE_TIME = 
        (SELECT REC_CREATE_TIME FROM T_OMCT_BA_CONTRACT_JK WHERE CONTRACT_SERIAL_NO = '{0[2]}' 
        ORDER BY REC_CREATE_TIME DESC FETCH FIRST 1 ROWS ONLY) 
        AND CONTRACT_SERIAL_NO = '{0[2]}'"""
    )
    tmp.GenFormatString(obj.PackToDict())
