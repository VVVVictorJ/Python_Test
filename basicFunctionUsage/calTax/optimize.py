incomeBoundary = [
    [0, 36000],
    [36000, 144000],
    [144001, 300000],
    [300001, 420000],
    [420001, 660000],
    [660001, 960000],
    [960001],
]


def f0(x):
    if x <= 36000:
        return x * 0.03
    if x >= 36001 and x <= 144000:
        return 0.1 * (x - 60000) - 2520
    if x >= 144001 and x <= 300000:
        return 0.1 * (x - 60000) - 2520
    if x >= 300001 and x <= 420000:
        return 0.25 * (x - 60000) - 31920
    if x >= 420001 and x <= 660000:
        return 0.3 * (x - 60000) - 52920
    if x >= 660001 and x <= 960000:
        return 0.35 * (x - 60000) - 85920
    if x >= 960001:
        return 0.45 * (x - 60000) - 181920


def g0(x):
    if x <= 36000:
        return x * 0.03
    if x >= 36001 and x <= 144000:
        return 0.1 * (x - 60000) - 210
    if x >= 144001 and x <= 300000:
        return 0.1 * (x - 60000) - 1410
    if x >= 300001 and x <= 420000:
        return 0.25 * (x - 60000) - 2660
    if x >= 420001 and x <= 660000:
        return 0.3 * (x - 60000) - 4410
    if x >= 660001 and x <= 960000:
        return 0.35 * (x - 60000) - 7160
    if x >= 960001:
        return 0.45 * (x - 60000) - 15160


ll = []
lll = []
# ll.append(f0(36001) + g0(1263999))
# ll.append(f0(144000) + g0(1156000))
# ll.append(f0(144001) + g0(1155999))
# ll.append(f0(300000) + g0(1000000))
# ll.append(f0(300001) + g0(999999))
# ll.append(f0(999999) + g0(300001))
# ll.append(f0(300001) + g0(999999))
# ll.append(f0(999999) + g0(300001))
# ll.append(f0(420001) + g0(879999))
# ll.append(f0(660000) + g0(640000))
# ll.append(f0(660001) + g0(639999))
# ll.append(f0(960000) + g0(340000))
# ll.append(f0(960001) + g0(339999))

# print(ll)
# print(max(ll), min(ll))
salary = 1300000
for i in range(1, salary+1, 1):
    # print(i)
    lll.append([i, salary - i])
    ll.append(f0(i) + g0(salary - i))

# print(ll[-1])
print(min(ll))
# print(lll.index([144000, 256000]))
# print(ll[143999])
print(lll[ll.index(min(ll))])
# print(lll[ll.index((24070.0))])
