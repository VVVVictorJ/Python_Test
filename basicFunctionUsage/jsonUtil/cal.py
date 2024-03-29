import warnings

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pandas import DataFrame, Series

warnings.filterwarnings(action="once")

"""
年终奖单独计算
1、年终奖金额除以12, 得到月平均数
2、用月平均数查表, 看月平均数在哪个区间,确定适用税率和速算扣除数
3、用年终奖全额乘以适用税率,再减去速算扣除数即可得到年终奖所得税
"""
"""
年终奖并入计算
年终奖金额为a, 年收入为b, 将二者合并计算, 
作为综合所得, 使用综合所得的适用税率来计算年终奖所得税
"""
# TODO 年终奖速算扣除数与综合所得速算扣除数不一致

tax_rate_and_deduction = {
    "1": [0.03, 0],
    "2": [0.10, 2520],
    "3": [0.20, 16920],
    "4": [0.25, 31920],
    "5": [0.30, 52920],
    "6": [0.35, 85920],
    "7": [0.45, 181920],
}

boundary = {
    "1": [36000],
    "2": [36000, 144000],
    "3": [144000, 300000],
    "4": [300000, 420000],
    "5": [420000, 660000],
    "6": [660000, 960000],
    "7": [960000],
}

yearAward_tax_rate_and_deduction = {
    "1": [0.03, 0],
    "2": [0.10, 210],
    "3": [0.20, 1410],
    "4": [0.25, 2660],
    "5": [0.30, 4410],
    "6": [0.35, 7160],
    "7": [0.45, 15160],
}


def GetTax(Sbonus, flag):
    if flag == 0:
        if month_avg_income := Sbonus / 12 <= 3000:
            return (
                tax_rate_and_deduction.get("1")[0],
                tax_rate_and_deduction.get("1")[1],
                boundary.get("1")[0],
            )
        elif month_avg_income := Sbonus / 12 > 3000 and month_avg_income <= 12000:
            return (
                tax_rate_and_deduction.get("2")[0],
                tax_rate_and_deduction.get("2")[1],
                boundary.get("2")[0],
            )
        elif month_avg_income := Sbonus / 12 > 12000 and month_avg_income <= 25000:
            return (
                tax_rate_and_deduction.get("3")[0],
                tax_rate_and_deduction.get("3")[1],
                boundary.get("3")[0],
            )
        elif month_avg_income := Sbonus / 12 > 25000 and month_avg_income <= 35000:
            return (
                tax_rate_and_deduction.get("4")[0],
                tax_rate_and_deduction.get("4")[1],
                boundary.get("4")[0],
            )
        elif month_avg_income := Sbonus / 12 > 35000 and month_avg_income <= 55000:
            return (
                tax_rate_and_deduction.get("5")[0],
                tax_rate_and_deduction.get("5")[1],
                boundary.get("5")[0],
            )
        elif month_avg_income := Sbonus / 12 > 55000 and month_avg_income <= 80000:
            return (
                tax_rate_and_deduction.get("6")[0],
                tax_rate_and_deduction.get("6")[1],
                boundary.get("6")[0],
            )
        elif month_avg_income := Sbonus / 12 > 80000:
            return (
                tax_rate_and_deduction.get("7")[0],
                tax_rate_and_deduction.get("7")[1],
                boundary.get("7")[0],
            )
    else:
        if month_avg_income := Sbonus <= 3000:
            return (
                tax_rate_and_deduction.get("1")[0],
                tax_rate_and_deduction.get("1")[1],
                boundary.get("1")[0],
            )
        elif month_avg_income := Sbonus > 3000 and month_avg_income <= 12000:
            return (
                tax_rate_and_deduction.get("2")[0],
                tax_rate_and_deduction.get("2")[1],
                boundary.get("2")[0],
            )
        elif month_avg_income := Sbonus > 12000 and month_avg_income <= 25000:
            return (
                tax_rate_and_deduction.get("3")[0],
                tax_rate_and_deduction.get("3")[1],
                boundary.get("3")[0],
            )
        elif month_avg_income := Sbonus > 25000 and month_avg_income <= 35000:
            return (
                tax_rate_and_deduction.get("4")[0],
                tax_rate_and_deduction.get("4")[1],
                boundary.get("4")[0],
            )
        elif month_avg_income := Sbonus > 35000 and month_avg_income <= 55000:
            return (
                tax_rate_and_deduction.get("5")[0],
                tax_rate_and_deduction.get("5")[1],
                boundary.get("5")[0],
            )
        elif month_avg_income := Sbonus > 55000 and month_avg_income <= 80000:
            return (
                tax_rate_and_deduction.get("6")[0],
                tax_rate_and_deduction.get("6")[1],
                boundary.get("6")[0],
            )
        elif month_avg_income := Sbonus > 80000:
            return (
                tax_rate_and_deduction.get("7")[0],
                tax_rate_and_deduction.get("7")[1],
                boundary.get("7")[0],
            )


def getTaxYearAward(Sbonus):
    if SplitPart := Sbonus / 12 < 3000:
        return (
            yearAward_tax_rate_and_deduction.get("1")[0],
            yearAward_tax_rate_and_deduction.get("1")[1],
        )
    elif SplitPart := Sbonus / 12 >= 3000 and SplitPart < 12000:
        return (
            yearAward_tax_rate_and_deduction.get("2")[0],
            yearAward_tax_rate_and_deduction.get("2")[1],
        )
    elif SplitPart := Sbonus / 12 >= 1200 and SplitPart < 25000:
        return (
            yearAward_tax_rate_and_deduction.get("3")[0],
            yearAward_tax_rate_and_deduction.get("3")[1],
        )
    elif SplitPart := Sbonus / 12 >= 25000 and SplitPart < 35000:
        return (
            yearAward_tax_rate_and_deduction.get("4")[0],
            yearAward_tax_rate_and_deduction.get("4")[1],
        )
    elif SplitPart := Sbonus / 12 >= 35000 and SplitPart < 55000:
        return (
            yearAward_tax_rate_and_deduction.get("5")[0],
            yearAward_tax_rate_and_deduction.get("5")[1],
        )
    elif SplitPart := Sbonus / 12 >= 55000 and SplitPart < 80000:
        return (
            yearAward_tax_rate_and_deduction.get("6")[0],
            yearAward_tax_rate_and_deduction.get("6")[1],
        )
    elif SplitPart := Sbonus / 12 >= 80000:
        return (
            yearAward_tax_rate_and_deduction.get("7")[0],
            yearAward_tax_rate_and_deduction.get("7")[1],
        )


def common_cal(MonthSalary):
    # return MonthSalary * 12 - 60000 - 1000 * 12 - 2000 * 12
    return MonthSalary * 12 - 60000


def SeperateCal(MonthSalary, YearEndAwards):
    if MonthSalary == 0:
        return "Invaild Salary"

    if sumYearIncome := MonthSalary * 12 <= 60000:
        return "SumYearIncome is less than 60000"

    taxRateMonth, deductionMonth, _ = GetTax(MonthSalary, 1)
    taxRateYear, deductionYear = getTaxYearAward(YearEndAwards)
    Personal_Income_Tax = common_cal(MonthSalary) * taxRateMonth - deductionMonth
    YearEndAwards_Income_Tax = YearEndAwards * taxRateYear - deductionYear

    return Personal_Income_Tax + YearEndAwards_Income_Tax


def MergeCal(MonthSalary, YearEndAwards):
    if MonthSalary == 0:
        return "Invaild Salary"

    if sumYearIncome := MonthSalary * 12 <= 60000:
        return "SumYearIncome is less than 60000"

    taxRate, deduction, _ = GetTax(MonthSalary, 1)
    a = common_cal(MonthSalary)
    # print(taxRate, deduction, _)
    Personal_Income_Tax = (a + YearEndAwards) * taxRate - deduction

    return Personal_Income_Tax


def OptimizeCal(MonthSalary, YearEndAwards):
    if MonthSalary == 0:
        return "Invaild Salary"

    if sumYearIncome := MonthSalary * 12 <= 60000:
        return "SumYearIncome is less than 60000"
    taxRateYear, deductionYear, boundaryYear = GetTax(YearEndAwards, 0)
    remainYearEndAwards = boundaryYear
    sumAllYearIncome = YearEndAwards - boundaryYear + common_cal(MonthSalary)

    taxRateSum, deductionSum, _ = GetTax(sumAllYearIncome, 0)
    taxRateRemain, deductionRemain, _ = GetTax(remainYearEndAwards, 0)

    Remain_Year_Tax = remainYearEndAwards * taxRateRemain - deductionRemain
    Sum_Year_Tax = sumAllYearIncome * taxRateSum - deductionSum

    return Remain_Year_Tax + Sum_Year_Tax

    # 计算年终奖与边界值的差，使用差值计算速算扣除数，除差值外部分合并入总额，与综合所得计算税


# 目前收入未知

print("Seperate Calculate: {}".format(SeperateCal(12000, 1000000)))
print("Merge Calculate: {}".format(MergeCal(12000, 1000000)))
print("Optimize Calculate: {}".format(OptimizeCal(12000, 1000000)))
# print([i for i in range(0, 130001, 1000)] * 3)
# print([SeperateCal(12000,i)for i in range(0, 130001, 1000)]+ [MergeCal(12000,i)for i in range(0, 130001, 1000)] + [OptimizeCal(12000,i)for i in range(0, 130001, 1000)])
# print([MergeCal(12000,i)for i in range(0, 130001, 1000)])
# print([OptimizeCal(12000,i)for i in range(0, 130001, 1000)])

# # # print("Merge Calculate: {}".format(MergeCal(0, 40000)))
# sns.set()

# data = {
#     # "salary": [12000, 12000, 12000, 12000, 12000, 12000, 12000, 12000, 12000],
#     "yearAwards": [i for i in range(0, 130001, 1000)] * 3,
#     "tax": [SeperateCal(12000, i) for i in range(0, 130001, 1000)]
#     + [MergeCal(12000, i) for i in range(0, 130001, 1000)]
#     + [OptimizeCal(12000, i) for i in range(0, 130001, 1000)],
#     "property": ["Sep" for i in range(0, 130001, 1000)]+["Merge" for i in range(0, 130001, 1000)]+["Optimize" for i in range(0, 130001, 1000)],
# }
# # data = {

# # }
# df = DataFrame(data)
# print(df)
# fig, ax = plt.subplots(figsize=(16, 10), dpi=80)
# # sns.stripplot(x=df.sg, y=df.hwy, jitter=0.25, size=8, ax=ax, linewidth=0.5)
# sns.swarmplot(
#     x="yearAwards", y="tax", data=df, hue="property", dodge=False, palette="husl"
# )
# plt.savefig("1.png")
