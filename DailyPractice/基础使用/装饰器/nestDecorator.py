import time
from functools import wraps

from decorator import decorator


@decorator
def hint(func, *args, **kwargs):
    print("{} is running".format(func.__name__))
    print("{}-{}".format(k, v) for k, v in kwargs.items())
    return func(*args, **kwargs)


def cache(instance):
    def wrapper(func):
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            joint_args = ".".join((str(x) for x in args))
            joint_kwargs = ",".join(
                "{}={}".format(k, v) for k, v in sorted(kwargs.items())
            )
            key = "{}::{}::{}".format(func.__name__, joint_args, joint_kwargs)
            print(key)
            result = instance.get(key)
            print(result)
            if result is not None:
                return result
            result = func(*args, **kwargs)
            instance.set(key, result)
            return result

        return inner_wrapper

    return wrapper


class Dictcache:
    def __init__(self) -> None:
        self.cache = dict()

    def get(self, key):
        return self.cache.get(key)

    def set(self, key, value):
        self.cache[key] = value

    def __str__(self) -> str:
        return str(self.cache)

    def __repr__(self) -> str:
        return repr(self.cache)

cache_instance = Dictcache()


@cache(cache_instance)
def long_time_func(x, **kwargs):
    time.sleep(x)
    return x


if __name__ == "__main__":
    cache_instance.set(3, "11")
    long_time_func(3, z=1, h=2)
    long_time_func(3, z=1, h=2)
