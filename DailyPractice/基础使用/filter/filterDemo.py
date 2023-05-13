import math

l = filter(lambda x: x % 2 == 0, range(10))
print(l)
print(list(l))


def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ["A", "", "B", None, "C", "  "])))


def isPrime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
            return True


l1 = [-1, 0, 2, 3, 6, 7, 8]
l2 = list(filter(isPrime, l1))
print(l2)
