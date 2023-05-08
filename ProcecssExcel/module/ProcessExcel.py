import logging

import pandas as pd
import xlrd


class ProcessExcel:
    def __init__(self, InputFileLocation: str, SheetName: str = "Sheet1") -> None:
        self.InputFileLocation = InputFileLocation
        self.DataFrame = pd.read_excel(InputFileLocation, sheet_name="Sheet1")
        self.ColumnsTitle = []
        self.DataSet = {}

    def getTitle(self):
        # print(self.DataFrame.columns)
        for k, v in enumerate(self.DataFrame.columns):
            # print("key is {}, value is {}".format(k + 1, v))
            self.ColumnsTitle.append(v)

    def getDataFromTitle(self):
        for i in range(len(self.ColumnsTitle)):
            # print(len(self.DataFrame[self.ColumnsTitle[i]]))
            self.DataSet[self.ColumnsTitle[i]] = (
                list(pd.Series(self.DataFrame[self.ColumnsTitle[i]].values))
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

    def showData(self):
        print(self.DataSet)


if __name__ == "__main__":
    obj = ProcessExcel("E:\\code\\Python\\ProcecssExcel\\src\\test.xlsx")
    obj.getTitle()
    obj.getDataFromTitle()
    obj.showData()
