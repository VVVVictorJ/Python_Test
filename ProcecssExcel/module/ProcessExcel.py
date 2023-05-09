import logging

import pandas as pd
import xlrd


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
                pd.Series(self.DataFrame[self.ColumnsTitle[i]].fillna("").values)
            )
            # print(
            #     "Now Title is :{}, TitleValue are {}".format(
            #         self.ColumnsTitle[i],
            #         pd.Series(self.DataFrame[self.ColumnsTitle[i]].values)
            #         .to_string(index=False)
            #         .replace("\n", " "),
            #     )
            # )

    def setTitle():
        pass

    def GetData(self) -> dict:
        return self.DataSet

    def PackDictToList(self) -> list:
        keys = []
        values = self.GetKeySet()
        for i in self.DataSet.keys():
            tmp = []
            for j in range(self.GetRowsCount()):
                # print("{:10}".format(l.get(i)[j]), end="\t")
                keys.add(self.DataSet.get(i)[j])
            
        print("\n")

        return list

    def GetKeySet(self):
        return list(self.DataSet.keys())

    # 返回行数
    @staticmethod
    def SGetRowsCount(param:dict):
        return len(next(iter(param.values())))

    # 返回列数
    @staticmethod
    def SGetColumnsCount(param:dict):
        return len(param.keys())
    
    # 返回行数
    def GetRowsCount(self):
        return len(next(iter(self.DataSet.values())))

    # 返回列数
    def GetColumnsCount(self):
        return len(self.DataSet.keys())

if __name__ == "__main__":
    obj = ProcessExcel("E:\\code\\Python\\ProcecssExcel\\src\\test.xlsx")
    # obj.getTitle()
    # obj.getDataFromTitle()
    # print(obj.getData())
    l = obj.GetData()
    Horizontal = len(l.keys())
    Vertical = len(next(iter(l.values())))
    # print("Dict has {} Keys, One Key's value's length is {}".format(Horizontal, Vertical))
    # print(l)
    for i in l.keys():
        # print(l.get(i))
        for j in range(Vertical):
            print("{:10}".format(l.get(i)[j]), end="\t")
        print("\n")
    # for k, v in enumerate(l):
    #     # print("k = {}, v = {}".format(k, l.get(str(k+1))[0]))
    #     for i in range(len(l.get(str(k + 1)))):
    #         print(l.get(str(k + 1))[i], end="\t")
    #     print("\n")

    # keys=['a','b','c']
    # vals=[3,10,'hello','t']
    # Dt2 = dict(zip(keys,vals))
    # print(Dt2)
    print(obj.GetKeySet())
    print(obj.GetRowsCount())
    print(obj.GetColumnsCount())
    # 返回的是可迭代序列
    # print(l.keys())