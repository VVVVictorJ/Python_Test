from collections import namedtuple

""" 
Python中创建常规元组时,其元素是通用的且未命名,可以使用具名元组namedtuple来解决
这个问题。
该namedtuple()返回与用于所述元组中的每个位置和一个通用名固定名称的元组namedtuple对象
要使用namedtuple,请先为其创建一个模板。下面的代码创建一个namedtuple名为Person的模板
,其属性为name,age和job
"""
Person = namedtuple("Person", "name age job")

Mike = Person(name='Mike', age=30, job='Data Scientist')
Kate = Person(name='Kate', age=28, job='Project Manager')

# 可以直接使用元组的元素了,再不用使用索引了
print(Mike.age)
print(Kate)
