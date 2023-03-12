import logging


def use_logging(func):
    # 参数
    def wrapper(*args, **kwargs):
        logging.warning("{} is running".format(func.__name__))
        return func(*args, **kwargs)

    return wrapper


# 省略最后一步赋值
@use_logging
def foo(name, age=None, height=None):
    print('I am {}, age is {}, height {}'.format(name, age, height))


if __name__ == '__main__':
    # foo = use_logging(foo)
    foo('victor', 26, 173)
