import logging


def use_logging(level):

    def decorator(func):

        def wrapper(*args, **kwargs):
            if level == "warn":
                logging.warning("{} is running".format(func.__name__))
            elif level == "info":
                logging.info("{} is running".format(func.__name__))
            return func(*args, **kwargs)

        return wrapper

    return decorator


# 省略最后一步赋值
@use_logging(level="warn")
def foo(name, age=None, height=None):
    print('I am {}, age is {}, height {}'.format(name, age, height))


if __name__ == '__main__':
    # foo = use_logging(foo)
    foo('victor', 26, 173)
