l = map(lambda x: x**2, [1, 2, 3, 4, 5])
print(l)

print(list(l))

l1 = [1, 2, 3]
l2 = [4, 5, 6, 7]
l3 = [8, 9, 1]
print(list(map(lambda x, y, z: x + y + z, l1, l2, l3)))

strA = "aAAAbBCC"
strB = "aA"
print(strA.count(strB))
print(sum(map(strA.count, strB)))
