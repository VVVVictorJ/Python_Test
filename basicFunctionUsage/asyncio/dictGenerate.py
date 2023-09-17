import random
import time
from functools import wraps
from pprint import pprint

a = [
    {
        "unique_id": "1295227",
        "week_date": "20230911",
        "project_id": "123",
        "department": "123",
        "current_period": "123",
        "deploy_type": "123",
        "project_start_time": "2023-07-27",
        "project_end_time": "2023-07-27",
        "period_start_time": "2023-07-27",
        "period_end_time": "2023-07-27",
        "finance_property": "123",
        "finish_time": "123",
        "project_scale": "123",
        "project_name": "123",
        "next_period": "123",
        "telephone": "123",
        "period_switch_status": "123",
        "current_week_status": "123",
        "next_week_plan": "123",
        "postscript": "123",
        "project_manager": "123",
    }
]

# 固定的键
fixed_keys = list(a[0].keys())

# 随机生成值
random_values = [str(random.randint(1, 100)) for _ in fixed_keys]

# 生成新的字典
new_dict = {key: value for key, value in zip(fixed_keys, random_values)}

# result = []

# result.append(new_dict)
# pprint(result)

# c = range(10)
# N = 1
# index1 = random.sample(c, N)
# index2 = random.sample(c, N)

# print(index1)
# print(index2)



def cost_time(func):
    def fun(*args, **kwargs):
        t = time.perf_counter()
        result = func(*args, **kwargs)
        print(f'func {func.__name__} cost time:{time.perf_counter() - t:.8f} s')
        return result

    return fun


@cost_time
def randomValue(inputList: dict):
    result = []
    c = range(1000000)
    # 固定的键
    fixed_keys = list(inputList[0].keys())

    # 随机生成值
    random_values = [str(random.sample(c, 1)) for _ in fixed_keys]

    # 生成新的字典
    new_dict = {key: value for key, value in zip(fixed_keys, random_values)}
    result.append(new_dict)
    return result

randomValue(a)