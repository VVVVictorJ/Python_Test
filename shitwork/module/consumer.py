# TODO 根据队列值进行数据库插入
import os

sep = os.path.sep

s1 = "D:\\archiveWork\\doc"
s2 = "5月员工试用期跟踪表-庄鸿杰.doc"

l = []
l.append(s1)
l.append(s2)

print(sep.join(l))
