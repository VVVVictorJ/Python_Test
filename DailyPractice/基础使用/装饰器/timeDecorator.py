from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        from time import time

        t_start = time()
        result = func(*args, **kwargs)
        t_end = time()
        print("time spend: {}".format(t_end - t_start))
        return result

    return wrapper


@timer
def test():
    n = 1
    for i in range(1, 10000):
        n = n**i

test()