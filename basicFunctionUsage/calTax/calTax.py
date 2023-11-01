import matplotlib.pyplot as plt
import pyecharts.options as opts
import seaborn as sns
from pandas import DataFrame
from pyecharts.charts import Line

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

yearAward_boundary = {
    "1": [36000],
    "2": [36000, 144000],
    "3": [144000, 300000],
    "4": [300000, 420000],
    "5": [420000, 660000],
    "6": [660000, 960000],
    "7": [960000],
}


def GetTax(Sbonus):
    if Sbonus <= 36000:
        return (
            tax_rate_and_deduction.get("1")[0],
            tax_rate_and_deduction.get("1")[1],
            boundary.get("1")[0],
        )
    elif Sbonus > 36000 and Sbonus <= 144000:
        return (
            tax_rate_and_deduction.get("2")[0],
            tax_rate_and_deduction.get("2")[1],
            boundary.get("2")[0],
        )
    elif Sbonus > 144000 and Sbonus <= 300000:
        return (
            tax_rate_and_deduction.get("3")[0],
            tax_rate_and_deduction.get("3")[1],
            boundary.get("3")[0],
        )
    elif Sbonus > 300000 and Sbonus <= 420000:
        return (
            tax_rate_and_deduction.get("4")[0],
            tax_rate_and_deduction.get("4")[1],
            boundary.get("4")[0],
        )
    elif Sbonus > 420000 and Sbonus <= 660000:
        return (
            tax_rate_and_deduction.get("5")[0],
            tax_rate_and_deduction.get("5")[1],
            boundary.get("5")[0],
        )
    elif Sbonus > 660000 and Sbonus <= 960000:
        return (
            tax_rate_and_deduction.get("6")[0],
            tax_rate_and_deduction.get("6")[1],
            boundary.get("6")[0],
        )
    elif Sbonus > 960000:
        return (
            tax_rate_and_deduction.get("7")[0],
            tax_rate_and_deduction.get("7")[1],
            boundary.get("7")[0],
        )


def getTaxYearAward(Sbonus):
    if Sbonus / 12 <= 3000:
        return (
            yearAward_tax_rate_and_deduction.get("1")[0],
            yearAward_tax_rate_and_deduction.get("1")[1],
            yearAward_boundary.get("1")[0],
        )
    elif Sbonus / 12 > 3000 and Sbonus / 12 <= 12000:
        # print("SplitPart:{}".format(SplitPart))
        return (
            yearAward_tax_rate_and_deduction.get("2")[0],
            yearAward_tax_rate_and_deduction.get("2")[1],
            yearAward_boundary.get("2")[0],
        )
    elif Sbonus / 12 > 12000 and Sbonus / 12 <= 25000:
        return (
            yearAward_tax_rate_and_deduction.get("3")[0],
            yearAward_tax_rate_and_deduction.get("3")[1],
            yearAward_boundary.get("3")[0],
        )
    elif Sbonus / 12 > 25000 and Sbonus / 12 <= 35000:
        return (
            yearAward_tax_rate_and_deduction.get("4")[0],
            yearAward_tax_rate_and_deduction.get("4")[1],
            yearAward_boundary.get("4")[0],
        )
    elif Sbonus / 12 > 35000 and Sbonus / 12 <= 55000:
        return (
            yearAward_tax_rate_and_deduction.get("5")[0],
            yearAward_tax_rate_and_deduction.get("5")[1],
            yearAward_boundary.get("5")[0],
        )
    elif Sbonus / 12 > 55000 and Sbonus / 12 <= 80000:
        return (
            yearAward_tax_rate_and_deduction.get("6")[0],
            yearAward_tax_rate_and_deduction.get("6")[1],
            yearAward_boundary.get("6")[0],
        )
    elif Sbonus / 12 > 80000:
        return (
            yearAward_tax_rate_and_deduction.get("7")[0],
            yearAward_tax_rate_and_deduction.get("7")[1],
            yearAward_boundary.get("7")[0],
        )


def Seperate(TotalSalary, YearEndAwards):
    if TotalSalary < 60000:
        return 0
    taxRateTotal, deductionTotal, _ = GetTax(TotalSalary)
    taxRateYearAwards, deductionYearAwards, _ = getTaxYearAward(YearEndAwards)
    return (
        taxRateTotal * TotalSalary
        - deductionTotal
        + (taxRateYearAwards * YearEndAwards - deductionYearAwards)
    )


def Merge(TotalSalary, YearEndAwards):
    if TotalSalary < 60000:
        return 0
    Sum = TotalSalary + YearEndAwards
    # print("Sum:{}".format(Sum))
    taxRate, deduction, _ = GetTax(TotalSalary)
    # print("Merge:\ttaxRate:{}\tdeduction:{}\t_:{}".format(taxRate, deduction, _))
    # return (Sum - 60000 - 1000 * 12 - 2000 * 12) * taxRate - deduction
    return Sum * taxRate - deduction


def Optimize(TotalSalary, YearEndAwards):
    if TotalSalary < 60000:
        return 0
    taxRateYear, deductionYear, boundaryYear = getTaxYearAward(YearEndAwards)
    remainYearEndAwards = boundaryYear
    sumAllYearIncome = (YearEndAwards - boundaryYear) + (TotalSalary - 60000)
    taxRateSum, deductionSum, _ = GetTax(sumAllYearIncome)
    taxRateRemain, deductionRemain, _ = getTaxYearAward(remainYearEndAwards)
    # Sum_Year_Tax = (
    #     sumAllYearIncome - 1000 * 12 - 2000 * 12
    # ) * taxRateSum - deductionSum
    Sum_Year_Tax = (sumAllYearIncome) * taxRateSum - deductionSum
    Remain_Year_Tax = remainYearEndAwards * taxRateRemain - deductionRemain
    return Sum_Year_Tax + Remain_Year_Tax


def F2(Sbonus):
    pass


def image(tax_name, x, y1, y2):
    line = Line().add_xaxis(x)
    line.add_yaxis(
        "合并计算",
        y1,
        is_smooth=True,
        label_opts=opts.LabelOpts(is_show=False),
        is_connect_nones=True,
    )
    line.add_yaxis(
        "单独计算",
        y2,
        is_smooth=True,
        label_opts=opts.LabelOpts(is_show=False),
        is_connect_nones=True,
    )
    # line.add_yaxis(
    #     "其他所得税",
    #     y3,
    #     is_smooth=True,
    #     label_opts=opts.LabelOpts(is_show=False),
    #     is_connect_nones=True,
    # )
    line.set_global_opts(
        title_opts=opts.TitleOpts(title=tax_name + " 计算 "),
        xaxis_opts=opts.AxisOpts(name="总收入", type_="category", boundary_gap=False),
        yaxis_opts=opts.AxisOpts(name="应缴所得税"),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
    ).render(tax_name + ".html")


wages_list_x = []
wage_taxList_y = []

operate_amount_x = []
operate_taxList_y = []

# other_amount_x = []
# other_taxList_y = []

wage = 0
while wage <= 1300000:
    wages_list_x.append(str(wage))
    wage_tax = Merge(144000, wage)
    wage_taxList_y.append(wage_tax)

    operate_amount_x.append(str(wage))
    operate_tax = Seperate(144000, wage)
    operate_taxList_y.append(operate_tax)

    # other_amount_x.append(str(wage))
    # other_tax = Merge(wage)
    # other_taxList_y.append(other_tax)
    wage += 1

image("第一题 第2小题", wages_list_x, wage_taxList_y, operate_taxList_y)

# print("Seperate Calculate: {}".format(Seperate(144000, 1300000)))
# print("Merge Calculate: {}".format(Merge(144000, 1300000)))
# print("Optimize Calculate: {}".format(Optimize(144000, 1300000)))


# sns.set()
# rangevalue=400001
# data = {
#     "yearAwards": [i for i in range(0, rangevalue, 1000)] * 3,
#     "tax": [Seperate(360000, i) for i in range(0, rangevalue, 1000)]
#     + [Merge(360000, i) for i in range(0, rangevalue, 1000)]
#     + [Optimize(360000, i) for i in range(0, rangevalue, 1000)],
#     "property": ["Sep" for i in range(0, rangevalue, 1000)]
#     + ["Merge" for i in range(0, rangevalue, 1000)]
#     + ["Optimize" for i in range(0, rangevalue, 1000)],
# }

# df = DataFrame(data)
# print(df)
# fig, ax = plt.subplots(figsize=(16, 10), dpi=200)
# # sns.stripplot(x=df.sg, y=df.hwy, jitter=0.25, size=8, ax=ax, linewidth=0.5)
# # sns.stripplot(
# #     x="yearAwards",
# #     y="tax",
# #     data=df,
# #     hue="property",
# #     jitter=0.25,
# #     size=8,
# #     ax=ax,
# #     linewidth=0.5,
# #     dodge=True,
# # )
# sns.swarmplot(
#     x="yearAwards",
#     y="tax",
#     data=df,
#     hue="property",
#     dodge=True,
#     palette="husl",
#     ax=ax,
#     marker="v",
# )
# plt.savefig("2.png")
