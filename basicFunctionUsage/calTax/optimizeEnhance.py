"""
计算个人所得税
"""


def f0(x):
    if x > 0 and x <= 36000:
        return x * 0.03
    elif x >= 36001 and x <= 144000:
        return 0.1 * (x - 60000) - 2520
    elif x >= 144001 and x <= 300000:
        return 0.1 * (x - 60000) - 2520
    elif x >= 300001 and x <= 420000:
        return 0.25 * (x - 60000) - 31920
    elif x >= 420001 and x <= 660000:
        return 0.3 * (x - 60000) - 52920
    elif x >= 660001 and x <= 960000:
        return 0.35 * (x - 60000) - 85920
    elif x >= 960001:
        return 0.45 * (x - 60000) - 181920


"""
计算年终奖税
"""


def g0(x):
    if x <= 36000:
        return x * 0.03
    elif x >= 36001 and x <= 144000:
        return 0.1 * (x - 60000) - 210
    elif x >= 144001 and x <= 300000:
        return 0.1 * (x - 60000) - 1410
    elif x >= 300001 and x <= 420000:
        return 0.25 * (x - 60000) - 2660
    elif x >= 420001 and x <= 660000:
        return 0.3 * (x - 60000) - 4410
    elif x >= 660001 and x <= 960000:
        return 0.35 * (x - 60000) - 7160
    elif x >= 960001:
        return 0.45 * (x - 60000) - 15160


def find_max_and_min(total_income):
    a = total_income
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
    if a > 960000:
        b.append([960000, a])
        c.append([960000, a])
    for i in b:
        if a >= i[1]:
            l.append([a - i[1], a - i[0]])
            ll.append((a - i[0], a - i[1]))
            lll.append([i[0], i[1]])
        else:
            break
    for k, v in enumerate(ll):
        for i in c:
            if l[k][0] > i[0] and l[k][0] < i[1]:
                if lll[k][1] >= a - i[1] >= lll[k][0]:
                    llll.append((a - i[1], i[1]))
                if lll[k][1] >= a - i[0] >= lll[k][0]:
                    llll.append((a - i[0], i[0]))
            if l[k][1] > i[0] and l[k][1] < i[1]:
                if lll[k][1] >= a - i[1] >= lll[k][0]:
                    # 返回端点元组
                    llll.append((a - i[1], i[1]))
                if lll[k][1] >= a - i[0] >= lll[k][0]:
                    llll.append((a - i[0], i[0]))
                llll.append(tuple(zip(b[k], v))[0])
        llll.append(tuple(zip(b[k], v))[1])

    kk = {}.fromkeys(llll).keys()
    kk = list(kk)

    min, max = f0(kk[1][0]) + g0(kk[1][1]), f0(kk[1][0]) + g0(kk[1][1])
    index_min = 0
    index_max = 0
    for k, v in enumerate(kk):
        if v[0] == 0:
            continue
        if min >= f0(v[0]) + g0(v[1]):
            min = f0(v[0]) + g0(v[1])
            index_min = k
        if max <= f0(v[0]) + g0(v[1]):
            max = f0(v[0]) + g0(v[1])
            index_max = k

    for k, v in enumerate(kk):
        if v[0] == 0:
            continue
        if min == f0(v[0]) + g0(v[1]):
            print("min:{} 工资:{} 年终奖:{}".format(f0(v[0]) + g0(v[1]), v[0], v[1]))
        if max == f0(v[0]) + g0(v[1]):
            print("max:{} 工资:{} 年终奖:{}".format(f0(v[0]) + g0(v[1]), v[0], v[1]))
    print(end='\n')

find_max_and_min(400000)
find_max_and_min(1300000)
