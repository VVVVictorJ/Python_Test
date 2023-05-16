from collections import Counter

"""
Counter()是字典对象的子类。Counter()可接收一个可迭代遍历的对象（例如字符串、列表或元组）作为参数，并返回计数器字典。
字典的键将是可遍历对象中的唯一元素，每个键的值将是可迭代对象中的每个唯一元素对应的计数。
"""
lst = [1, 2, 3, 3, 2, 1, 1, 1, 2, 2, 3, 1, 2, 1, 1]
counter = Counter(lst)
print(counter[1])

"""
Counter对象最有用的功能是most_common()函数。
将其应用于Counter对象时,它将返回N个最常见元素及其计数的列表,按从最常见到最不常见的顺序排列。
每个元组的第一个元素是列表中的唯一原始，每个元组的第二个元素是计数。
"""
print(counter.most_common(2)[0])