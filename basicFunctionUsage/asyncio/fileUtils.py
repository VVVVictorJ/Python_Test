import os
import sys

import yaml


class FileUtils:
    @staticmethod
    def writeToFile(source, dest, filename: str):
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

    @staticmethod
    def getConfigValue():
        realpath = os.path.dirname(os.path.realpath(sys.argv[0]))
        yamlFilePath = os.path.join(
            realpath,
            "config.yaml",
        )
        f = open(yamlFilePath, "r", encoding="utf-8")
        cfg = f.read()
        d = yaml.load(cfg, Loader=yaml.FullLoader)
        return d
