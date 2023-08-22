import os 
import sys
import yaml
import xlrd
from LogUtils import Log


realpath = os.path.dirname(os.path.realpath(sys.argv[0]))
print(realpath)
path = os.path.join(realpath, "config.yaml")
print(path)

patt=r"C:\Users\vanPersie\Document\Python\analysisExcel\analysisExcel\ProcessExcel\src\test"
def getConfigValue():
    #TODO 待修改成exe所在文件夹的路径
    yamlFilePath = os.path.join(
        realpath,
        "config.yaml",
    )
    f = open(yamlFilePath, "r", encoding="utf-8")
    cfg = f.read()
    d = yaml.load(cfg, Loader=yaml.FullLoader)
    return d
# print(getConfigValue()["DATABASE_URI"])
# print(getConfigValue()["FILEPATH"])
# workbook = xlrd.open_workbook(
#     getConfigValue()["FILEPATH"],
#     formatting_info=True,
# )

# l = [os.path.join(getConfigValue()["FILEPATH"],file) for file in os.listdir(getConfigValue()["FILEPATH"])]
# for filepath in l:
#     workbook = xlrd.open_workbook(
#     filepath,
#     formatting_info=True,
#     )
#     sheet1_object = workbook.sheet_by_name(getConfigValue()["SHEETNAME"])
#     # print(sheet1_object.merged_cells)
#     print(type(sheet1_object.cell_value(1, 1)))
#     print(type(int(sheet1_object.cell_value(1, 1))))

for filepath in [
    os.path.join(getConfigValue()["FILEPATH"], file)
    for file in os.listdir(getConfigValue()["FILEPATH"]) if os.path.isfile(file) and file.endswith(".xls")
    ]:
    print(filepath)

l = [ file
    for file in os.listdir(getConfigValue()["FILEPATH"]) if os.path.isfile(file) and file.endswith(".xls")
    ]
print(getConfigValue()["FILEPATH"])
print(l)
for file in os.listdir(getConfigValue()["FILEPATH"]): 
    if os.path.isfile(os.path.join(getConfigValue()["FILEPATH"], file)) and file.endswith(".xls"):
        print(file)
# print(getConfigValue()["LOGPATH"])
# if os.path.exists(getConfigValue()["LOGPATH"]):
#     print("true")
# else:
#     os.makedirs(getConfigValue()["LOGPATH"])
#     if os.path.exists(getConfigValue()["LOGPATH"]):
#         print("true")

log = Log("a").getlog()
log.info("test")


# for file in os.listdir(path):
#     file_path = os.path.join(path, file)