import json
from pprint import pprint

a = [["Income", "Life Expectancy", "Population", "Country", "Year"]]

b = json.dumps(a)

pprint(b)

c =range(0,1300001,1000)
print(len(c))
def F1(Stax):
    if Stax <= 36000:
        return Stax * 0.03
    elif Stax <= 144000:
        return Stax * 0.1 - 2520
    elif Stax <= 300000:
        return Stax * 0.2 - 16920
    elif Stax <= 420000:
        return Stax * 0.25 - 31920
    elif Stax <= 660000:
        return Stax * 0.3 - 52920
    elif Stax <= 960000:
        return Stax * 0.35 - 85920
    else:
        return Stax * 0.45 - 181920


def F3(Stax):
    if Stax <= 15000:
        return Stax * 0.05
    elif Stax <= 30000:
        return Stax * 0.1 - 750
    elif Stax <= 60000:
        return Stax * 0.2 - 3750
    elif Stax <= 100000:
        return Stax * 0.3 - 9750
    elif Stax <= 150000:
        return Stax * 0.35 - 14750
    else:
        return Stax * 0.4 - 23250


def F4(Stax):
    return Stax * 0.2


# 计算所得税
income_range = range(0, 1300001, 1000)
tax_comprehensive = [F1(Stax) for Stax in income_range]
tax_business = [F3(Stax) for Stax in income_range]
tax_interest_dividend = [F4(Stax) for Stax in income_range]


# 计算年终奖两种方式的个人所得税
def F2(Sbonus, annual_income):
    merged_tax = F1(annual_income + Sbonus) - F1(annual_income)
    individual_tax = F1(Sbonus)
    return merged_tax, individual_tax


annual_income_range = [400000, 1000000]  # 年收入范围，示例为 40 万和 100 万
Sbonus_range = range(0, 1300001, 1000)
tax_annual_bonus_merge_40k = [[F2(Sbonus, 400000)[0], Sbonus, "个人所得税", 400000] for Sbonus in Sbonus_range]
tax_annual_bonus_individual_40k = [[F2(Sbonus, 400000)[1]] for Sbonus in Sbonus_range]
tax_annual_bonus_merge_100k = [[F2(Sbonus, 1000000)[0]] for Sbonus in Sbonus_range]
tax_annual_bonus_individual_100k = [[F2(Sbonus, 1000000)[1]] for Sbonus in Sbonus_range]

def cal():
    Sbonus_range = range(0, 1300001, 1000)
    tax_annual_bonus_merge_40k = [[F2(Sbonus, 400000)[0], Sbonus, "个人所得税", 400000] for Sbonus in Sbonus_range]
    return json.dumps(tax_annual_bonus_merge_40k,ensure_ascii=False)


b = json.dumps(tax_annual_bonus_merge_40k,ensure_ascii=False)

pprint(b)