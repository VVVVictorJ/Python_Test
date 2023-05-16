import logging
from functools import wraps


def use_logging(func):
    # 为了装饰过的函数__name__属性不变，我们可以使用wraps方法
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.warning("{} is running".format(func.__name__))
        return func(*args, **kwargs)

    return wrapper


# 省略最后一步赋值
@use_logging
def foo():
    print("I am foo")


if __name__ == "__main__":
    # foo = use_logging(foo)
    foo()
    print(foo.__name__)
