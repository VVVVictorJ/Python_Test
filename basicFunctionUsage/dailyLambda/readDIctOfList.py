# data = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 35}]

# # 使用lambda函数读取存储字典的列表中字典的所有键和值
# result = list(map(lambda d: (list(d.keys()), list(d.values())), data))

# print(result)

data = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35},
]

data1 = [{"errorMsg": "Out of index"}]

# 使用lambda函数读取存储字典的列表中字典的所有键值，一次输出一对键值
result = list(map(lambda d: [(k, v) for k, v in d.items()], data1))

# print(result)

for k, v in enumerate(result):
    print(v[0][0], v[0][1])

create_list = lambda *elements: list(elements)

data = create_list("Alice", "Bob", "Charlie")

print(data)

create_list = lambda *elements: [dict(element) for element in elements]

data = create_list(
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35},
)

print(data)

create_list = lambda *elements: [dict(element) for element in elements]

data = create_list({"name": "Alice", "age": 25}, {"name": "Bob", "age": 30})

# 累计添加新的字典元素
data.append({"name": "Charlie", "age": 35})

print(data)

data = (lambda *elements: [dict(element) for element in elements])(
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35},
)

print(data)

data = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35},
]

result = list(map(lambda element: dict(element), data))

print(result)

# 生成字典
create_dict = lambda key, value: {key: value}

result = create_dict("name", "Alice")

print(result)
