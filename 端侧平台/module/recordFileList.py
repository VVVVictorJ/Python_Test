import os

"""
用于消费者类，数据库记录应该更为合理
"""


class RecordDirList:
    def __init__(self):
        self.recordFilePath = os.path.join(os.getcwd(), "record.txt")

    """
    将临时文件夹路径写入记录中
    """

    def addList(self, tmpDir: str):
        with open(self.recordFilePath, "wb+") as f:
            f.write(tmpDir.encode())

    """
    获取已存在的临时文件列表
    """

    def getExistedList():
        pass

    """
    判断是否有更新，实现像git diff的功能，若文件有更新需要添加进去，无更新去除相关记录
    数据库内记录时间戳
    """

    def isUpdate():
        pass
