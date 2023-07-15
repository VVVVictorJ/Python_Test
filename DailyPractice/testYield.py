import cython
import os
import  sys

def getPath():
    print(os.getcwd())# E:/code/python
    print(os.path.abspath('.'))# E:/code/python
    print(os.path.abspath('C://Users//VanPersie//.pip//pip.ini'))# C:/Users/VanPersie/.pip/pip.ini
    print(os.path.abspath('..'))# E:/code
    print(os.path.abspath(os.curdir))# e:/code/python

def getLocationPath():
    print(sys.argv[0]) # ./testYield.py


def joinPath():
    print(os.path.join('c:','//a//', 'b'))# c://a//b

def getFileList():
    #print(os.walk(f'E:/charRecord/qq/956951190/FileRecv/啥都有商店mod2.0/nativePC/common/facility'))
    print([i for i in os.listdir(r'E:/charRecord/qq/956951190/FileRecv/啥都有商店mod2.0/nativePC/common/facility')])


def getGenFileList():
    for i in os.listdir(r'E:/charRecord/qq/956951190/FileRecv/啥都有商店mod2.0/nativePC/common/facility'):
        # yield i
        j = yield i
        if j == -1:
            break


# FileList = getGenFileList()


# print(FileList.__next__())
# print(FileList.__next__())
# print(FileList.__next__())
# print(FileList.send(-1))
# print(FileList.__next__())

# for i in FileList:
#     print(i)
#     if i == 4:

# getLocationPath()

# getPath()

# joinPath()

# getFileList()

def gen_list():
    # 多个逻辑块 使用yield 生成一个列表
    for i in range(10):
        yield i
    for j in range(5):
        yield j * j
    for k in [100, 200, 300]:
        yield k
        
for item in gen_list():
    print(item)
