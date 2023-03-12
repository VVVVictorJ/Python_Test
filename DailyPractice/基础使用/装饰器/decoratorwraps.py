# 装饰器
def logged(func):
    def with_logging(*args, **kwargs):
        print(func.__name__)      # python2输出 'with_logging' python3输出 f
        print(func.__doc__)       # python2输出 None python3输出 does some math
        return func(*args, **kwargs)
    return with_logging

# 函数
@logged
def f(x):
   """does some math"""
   return x + x * x

logged(f(2))