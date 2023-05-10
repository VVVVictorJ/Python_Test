import logging

import pandas as pd
import xlrd
from FormatString import AutoFormatSqlGenarator


class ProcessExcel:
    def __init__(self, InputFileLocation: str, SheetName: str = "Sheet1") -> None:
        self.InputFileLocation = InputFileLocation
        self.DataFrame = pd.read_excel(InputFileLocation, sheet_name="Sheet1")
        # excel 纵列标题
        self.ColumnsTitle = []
        self.DataSet = {}
        self.getTitle()
        self.getDataFromTitle()

    def getTitle(self):
        # print(self.DataFrame.columns)
        for k, v in enumerate(self.DataFrame.columns):
            # print("key is {}, value is {}".format(k + 1, v))
            self.ColumnsTitle.append(v)

    def getDataFromTitle(self):
        for i in range(len(self.ColumnsTitle)):
            self.DataSet[self.ColumnsTitle[i]] = list(
                pd.Series(self.DataFrame[self.ColumnsTitle[i]].fillna("''").values)
            )

    def setTitle():
        pass

    def GetData(self) -> dict:
        return self.DataSet

    
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

    def GetKeySet(self) -> list:
        """返回标签值

        Returns:
            list: 列标签值
        """
        return list(self.DataSet.keys())

    @staticmethod
    def SGetRowsCount(param: dict) -> int:
        """staticmethod

        Args:
            param (dict): 字典

        Returns:
            int: 返回字典的长度, 既当前Excel的行数
        """
        return len(next(iter(param.values())))

    @staticmethod
    def SGetColumnsCount(param: dict) -> int:
        """staticmethod

        Args:
            param (dict): 字典

        Returns:
            int: 返回字典的Key的个数, 即当前Excel的列数
        """ 
        return len(param.keys())

    # 返回行数
    def GetRowsCount(self) -> int:
        return len(next(iter(self.DataSet.values())))

    # 返回列数
    def GetColumnsCount(self) -> int:
        return len(self.DataSet.keys())


if __name__ == "__main__":
    obj = ProcessExcel("E:\\code\\Python\\ProcessExcel\\src\\test.xlsx")
    print("Index is : {}".format(obj.GetKeySet()))
    print("Excel has {} rows".format(obj.GetRowsCount()))
    print("Excel has {} columns(index)".format(obj.GetColumnsCount()))
    tmp = AutoFormatSqlGenarator("select {},{},{},{},{} from test")
    tmp.GenFormatString(obj.PackToDict())
