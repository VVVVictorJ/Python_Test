import json

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

tax_rate_and_deduction = {
    "1": [3, 0],
    "2": [10, 210],
    "3": [20, 1410],
    "4": [25, 2660],
    "5": [30, 4410],
    "6": [35, 7160],
    "7": [45, 15160],
}


def F2(Sbonus):
    if month_avg_income := Sbonus / 12 <= 3000:
        return tax_rate_and_deduction.get("1")
    elif month_avg_income :=Sbonus/12 > 3000 and month_avg_income <= 12000:
        return tax_rate_and_deduction.get("2")
    elif month_avg_income :=Sbonus/12 > 12000 and month_avg_income <= 25000:
        return tax_rate_and_deduction.get("3")
    elif month_avg_income :=Sbonus/12 > 25000 and month_avg_income <= 55000:
        return tax_rate_and_deduction.get("4")
    elif month_avg_income :=Sbonus/12 > 55000 and month_avg_income <= 80000:
        return tax_rate_and_deduction.get("5")
    elif month_avg_income :=Sbonus/12 > 80000:
        return tax_rate_and_deduction.get("6")
    elif month_avg_income :=Sbonus/12 > 0:
        return tax_rate_and_deduction.get("7")


print(F2(360001))