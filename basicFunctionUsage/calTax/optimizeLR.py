from pprint import pprint

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
    if x > 0 and x <= 36000:
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


# 总收入
a = 400000

b = [
    [0, 36000],
    [36000, 144000],
    [144000, 300000],
    [300000, 420000],
    [420000, 660000],
    [660000, 960000],
]

c = [
    [0, 36000],
    [36000, 144000],
    [144000, 300000],
    [300000, 420000],
    [420000, 660000],
    [660000, 960000],
]



l = []
ll = []
# 已使用b区间
lll = []
# 边界值点
llll = []

def pre(x):
    a= x
    if a > 960000:
        b.append([960000, a])
        c.append([960000, a])
    for i in b:
        # print(i)
        if a >= i[1]:
            # print("a - i[1]:{}\ta - i[0]:{}t".format(a - i[1], a - i[0]))
            l.append([a - i[1], a - i[0]])
            ll.append((a - i[0], a - i[1]))
            lll.append([i[0], i[1]])
        else:
            break

# print(b)
# print(l)

# for k, v in enumerate(l):
#     print(b[k], v)


def divide(x, y, z):
    for i in c:
        if x[0] > i[0] and x[0] < i[1]:
            # print(
            #     "x[0]:{}\tx[1]:{}\ti:[0]:{}\ti[1]:{}\t".format(x[0], x[1], i[0], i[1])
            # )
            if z[1] >= y - i[1] >= z[0]:
                llll.append((y - i[1], i[1]))
            if z[1] >= y - i[0] >= z[0]:
                llll.append((y - i[0], i[0]))
            # print([i[0], i[1]])
        if x[1] > i[0] and x[1] < i[1]:
            # print(
            #     "x[0]:{}\tx[1]:{}\ti:[0]:{}\ti[1]:{}\t".format(x[0], x[1], i[0], i[1])
            # )
            # print("bs:{}bx:{}".format(i[0], i[1]))

            # c = i[1],b = y-c,检查b是否属于[144000,300000]
            # b = y-i[0], b = y-i[1]
            if z[1] >= y - i[1] >= z[0]:
                # 返回端点元组
                llll.append((y - i[1], i[1]))
            if z[1] >= y - i[0] >= z[0]:
                llll.append((y - i[0], i[0]))


# print(i[0], i[1])

# print(i[0], i[1])
# print([i[0], i[1]])


def k(u,ll):
    pre(u)
    # 边界值
    for k, v in enumerate(ll):
        divide(l[k], a, lll[k])
        llll.append(tuple(zip(b[k], v))[0])
        llll.append(tuple(zip(b[k], v))[1])

    # pprint(llll)

    kk = {}.fromkeys(llll).keys()
    kk = list(kk)

    # print(kk)
    min, max = f0(kk[1][0]) + g0(kk[1][1]), f0(kk[1][0]) + g0(kk[1][1])

    for k, v in enumerate(kk):
        # print("k:{}, v:{}".format(k, v))
        if v[0] == 0:
            continue
        if min >= f0(v[0]) + g0(v[1]):
            min = f0(v[0]) + g0(v[1])
        if max < f0(v[0]) + g0(v[1]):
            max = f0(v[0]) + g0(v[1])
        # print("min:{} max:{}".format(min, max))
        print("k:{} 工资:{} 年终奖:{} 税:{}".format(k, v[0], v[1], f0(v[0]) + g0(v[1])))
    print("min:{} max:{}".format(min, max))


# print(f0(100000)+g0(300000))
# 263670.0
# k(1300000, ll)
k(400000, ll)
