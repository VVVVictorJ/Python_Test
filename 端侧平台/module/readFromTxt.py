import os


class readFromTxt:

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.fileList = []
        self.paraDict = {}

    def getKeyAndValue(self):
        for k, v in enumerate(self.fileList):
            if os.path.splitext(v)[-1] == '.txt':
                with open(v, "r") as f:
                    for line in f.readlines():
                        str = line
                        # print(str[:str.find(chr(12288))],
                        #       str[str.index('@') + 1:])
                        self.genData(str[:str.find(chr(12288))],
                                     str[str.index('@') + 1:].strip())

    def genData(self, k, v):
        self.paraDict[k] = v

    def getFileList(self):
        tmp = [i for i in os.listdir(self.filepath)]
        for i in tmp:
            self.fileList.append(os.path.join(self.filepath, i))
    def getDict(self):
        self.getFileList()
        self.getKeyAndValue()
        return self.paraDict


if __name__ == '__main__':
    obj = readFromTxt(
        '/home/victor/Python/shitwork/module/57d42e7f-29ce-44fa-af46-d0692564d4b7'
    )
    # obj.getFileList()
    # obj.getKeyAndValue()
    for i in obj.getDict().items():
        print(i)