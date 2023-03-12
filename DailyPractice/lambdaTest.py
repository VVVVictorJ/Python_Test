res = lambda x, y: x + y
print(res(1, 2))

print((lambda x, y: x if x > y else y)(1, 2))

# filter
# 第一个参数为函数

a = ['聚魔之地','怪物猎人']

print(list(filter(lambda x:x=='怪物猎人', a)))

print(list(filter(None, [1, '老胡', 0, False])))


def testfilter(x):
    return x % 2


print(list(filter(testfilter, range(31))))

print(list(filter(lambda x: x % 2, range(31))))

# map
# 对可迭代序列进行运算

print(list(map(lambda x: x * 2, [1, 2, 3, 4, 5])))

a = [1, 2, 3, 4]
b = [2, 4, 6, 8]
c = [3, 6, 9, 12]
print(list(map(lambda x, y, z: x * y * z, a, b, c)))
