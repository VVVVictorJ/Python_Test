import os
import time
from functools import wraps
from multiprocessing import Process


class timer(object):

    def __init__(self, func) -> None:
        self._func = func

    def __call__(self, *args, **kwds):
        start_time = time.time()
        self._func()
        end_time = time.time()
        print("【Now function runing time】:" + str(end_time - start_time))


def timeTicker(f):

    @wraps(f)
    def wrapper(*args):
        t1 = time.time()
        r = f(*args)
        t2 = time.time()
        print("【Now function runing time】:" + str(t2 - t1))
        return r

    return wrapper


@timeTicker
def func(name):
    # os.getpid() 获取当前进程ID
    print('【process {} starts】'.format(str(os.getpid())))
    time.sleep(2)
    print('【process {} ends】'.format(str(os.getpid())))


@timeTicker
def count(name):
    sum = 0
    print('【process {} starts】'.format(str(os.getpid())))
    for i in range(1000000):
        sum += i**2
    print('【process {} ends】'.format(str(os.getpid())))


def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    # 多线程
    # print('【main process is {}】'.format(os.getpid()))
    # func()
    # func()
    print('【main process is 】: {}'.format(str(os.getpid())))
    start_time = time.time()

    p1 = Process(target=count, args=('', ))
    p2 = Process(target=count, args=('', ))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end_time = time.time()
    print('【total time is 】: {}'.format(str(end_time - start_time)))
