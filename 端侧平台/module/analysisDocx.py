import os
import platform
import re
import sys
import uuid
import zipfile

import pandas as pd
from docx import Document
from lxml import etree
from processDocx import ProcessDocx
from recordFileList import RecordDirList


# TODO 将其实现成单例
# 文件生成路径有待优化 Done
# 将处理文件信息的代码重构独立至模块 Done
# 将处理图片模块的代码重构独立至模块 Done
class AnalysisDocx:
    def __init__(self, filepath: str):
        """初始化函数

        Args:
            filepath (str): 待解析文件路径

        Raises:
            TypeError: 文件路径不存在
            TypeError: 非docx文件
        """
        abspath = os.path.join(
            os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"),
            filepath,
        )
        if not os.path.isfile(abspath):
            raise TypeError("NOT FILEPATH")
        if not filepath.endswith(".docx"):
            raise TypeError("NOT DOCX FILE")
        self.filepath = abspath
        self.uuidStr = str(uuid.uuid4())
        self.resultpath = ""
        self.docxWordInfo = {}
        self.docxImageDict = {}
        self.docxImage = []
        self.record = RecordDirList()
        self.runingPlatform = platform.system().lower()

    def genResultPath(self, suffix: str = ""):
        """生成结果路径

        Args:
            suffix (str, optional): 文件尾缀,默认可为空. Defaults to ''.

        Returns:
            _type_: str
        """
        if suffix == "":
            return os.path.join(sys.path[0], "src", "images", str(uuid.uuid4()))
        else:
            a = []
            a.append(os.path.join(sys.path[0], "src", "resources", str(uuid.uuid4())))
            a.append(suffix)
            return ".".join(a)

    def genImageRecord(self, val):
        """存储图片地址至列表

        Args:
            val (str): 图片地址
        """
        self.docxImage.append(val)

    def genDocxTableInfo2TxtTest(self):
        try:
            file = Document(self.filepath)
            table = file.tables[0]
            cells = table._cells
            cells_string = [cell.text for cell in cells]
            # print(len(cells_string))
            # for k, v in enumerate(cells_string):
            #     print(k, v.replace('\n', ' ').replace(' ', ''))
            cells_value = []
            cnt = 0
            for ele in cells_string:
                if len(cells_value) == 0:
                    cells_value.append(ele)
                else:
                    # if ele == '无':
                    #     cnt += 1
                    if cells_value[-1] != ele:
                        cells_value.append(ele)
                    # elif cells_value[-1] == '无' and cnt == 7:
                    #     cells_value.append(ele)
            # print(len(cells_value))
            # cells_value = sorted(set(cells_string), key=cells_string.index)
            # print(len(cells_value))
            for k, v in enumerate(cells_value):
                print(k, v.replace("\n", " "))
        except:
            pass

    def writeToFile(self, source, dest, filename: str):
        """写入文件至指定位置

        Args:
            source (binary): 源文件
            dest (str): 目标地址
            filename (str): 文件名
        """
        destinationPath = os.path.sep.join([dest, filename])
        try:
            with open(f"{destinationPath}", "wb") as f:
                f.write(source)
        except FileNotFoundError:
            print("无法打开指定的文件!")
        except LookupError:
            print("指定了未知的编码!")
        except UnicodeDecodeError:
            print("读取文件时解码错误!")

    def genDocxTableInfoToCsv(self):
        """将docx文件数据转换为csv"""
        try:
            obj = ProcessDocx()
            self.docxWordInfo = obj.processDocxTableInfo(self.filepath)
        except:
            print("ProcessDocx 出错")

        try:
            df = pd.DataFrame(self.docxWordInfo)
            # print(df.to_string(index=False))
            df.to_csv(self.genResultPath(".csv"), index=None)
        except FileNotFoundError:
            print("无法打开指定的文件！")

    def genDocxImage(self):
        """获取docx的图片"""
        try:
            # 写入指定目录
            self.docxImageDict = ProcessDocx.processDocxImageInfo(self.filepath)
            if len(self.docxImageDict) == 0:
                print("此Docx无图片!")
            else:
                self.resultpath = self.genResultPath()
                if not os.path.exists(self.resultpath):
                    os.makedirs(self.resultpath)
                for k, v in enumerate(self.docxImageDict):
                    self.writeToFile(self.docxImageDict[v], self.resultpath, v)
        except:
            print("写入图片出错")
        finally:
            print("提取Docx图片, 已处理完。")

    def showData(self):
        """展示数据, 针对中文字符对齐优化"""
        for k, v in self.docxWordInfo.items():
            print(
                "{0:{1}<10}\t{1:^10}".format(k, chr(12288)),
                "{0}\t{1:^10}".format(v, chr(12288)),
            )
        for k, v in enumerate(self.docxImage):
            print(
                "{0:{1}<2}\t{1:^3}".format(k, chr(12288)),
                "{0}\t{1:^10}".format(v, chr(12288)),
            )


if __name__ == "__main__":
    # obj = AnalysisDocx(
    #     filepath=f"E:\\code\\Python\\shitwork\\src\\251B_20220228_湛江钢铁_厚板L3系统_故障报告书_B.docx"
    # )

    # print(os.getcwd())

    obj = AnalysisDocx(
        # filepath=f"E:\\code\\Python\\shitwork\\src\\2518_20220110_湛江钢铁_炼钢热轧L3系统_故障报告书_B.docx"
        filepath=f"2518_20220110_湛江钢铁_炼钢热轧L3系统_故障报告书_B.docx"
    )
    try:
        obj.genDocxImage()
        obj.genDocxTableInfoToCsv()
    except FileNotFoundError:
        print("无法打开指定的文件!")
    except LookupError:
        print("指定了未知的编码!")
    except UnicodeDecodeError:
        print("读取文件时解码错误!")
    except Exception as e:
        print(e)
