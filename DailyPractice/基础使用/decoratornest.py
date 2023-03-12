def a(func):

    def test_a(*args, **kwargs):
        print("now is wrapper: a")
        print(func.__name__)
        print(func.__doc__)
        return func(*args, **kwargs)

    return test_a


def b(func):

    def test_b(*args, **kwargs):
        print("now is wrapper: b")
        print(func.__name__)
        print(func.__doc__)
        return func(*args, **kwargs)

    return test_b


def c(func):

    def test_c(*args, **kwargs):
        print("now is wrapper: c")
        print(func.__name__)
        print(func.__doc__)
        return func(*args, **kwargs)

    return test_c


@a
@b
@c
def f(x):
    """now is f()"""
    return x * x * x


if __name__ == '__main__':
    # 装饰器调用顺序a(b(c)),调用顺序从里至外
    f(2)