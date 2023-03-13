#map(func, iter)


def square(x):
    return x**2


print(list(map(square, [1, 2, 3, 4, 5])))

print(list(map(lambda x: x**2, [1, 2, 3, 4, 5])))

#如果存在多个迭代器, 迭代器数量为min(len(iterator1), len(iterator2))

print(list(map(lambda x, y: x < y, [7, 2, 4], [9, 2, 3, 4, 5])))
