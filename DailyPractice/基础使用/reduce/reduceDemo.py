from functools import reduce

print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))

print(reduce(lambda x, y: x * y, [1, 2, 3, 4, 5]))

print(reduce(lambda x, y: x * y, range(1, 5)))

for i in range(1,5):
    print(i)