from collections import defaultdict

""" 
试图访问不存在的键值,不会引发错误
访问不存在的键值,其对应的默认值是根据创建defaultdict对象时作为参数传递的数据类型
自动设置的。
"""
names_dict = defaultdict(int)
names_dict["Bob"] = 1
names_dict["Katie"] = 2
sara_number = names_dict["Sara"]
print(names_dict)
