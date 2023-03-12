import logging


def use_logging(func):

    def wrapper():
        logging.warning("{} is running".format(func.__name__))
        return func()
    return wrapper

# 省略最后一步赋值
@use_logging
def foo():
        print('I am foo')

if __name__ == '__main__':
    # foo = use_logging(foo)    
    foo()
