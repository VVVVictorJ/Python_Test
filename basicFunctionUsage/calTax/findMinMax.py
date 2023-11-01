from calTax import *


def divide_part(totalIncome, asumeYearIncome):
    if totalIncome < asumeYearIncome:
        return -1
    return asumeYearIncome, totalIncome - asumeYearIncome


incomeBoundary = [
    [0, 36000],
    [36000, 144000],
    [144001, 300000],
    [300001, 420000],
    [420001, 660000],
    [660001, 960000],
    [960001],
]

enumList = []

for i in range(len(incomeBoundary)):
    if incomeBoundary[i][0] == 960001:
        if divide_part(400000, incomeBoundary[i][0]) == -1:
            continue
    if type(divided_part := divide_part(400000, incomeBoundary[i][1])) == tuple:
        enumList.append(list(divided_part))
    else:
        if divide_part(400000, incomeBoundary[i][1]) == -1:
            continue

for i in enumList:
    print("TotalSalary:{}\tYearEndAwards:{}".format(i[0], i[1]))
    print("SeperateCalculate:{}\nMergeCalculate:{}\nOptimizeCalculate:{}\n".format(Seperate(i[0],i[1]), Merge(i[0],i[1]), Optimize(i[0],i[1])))
