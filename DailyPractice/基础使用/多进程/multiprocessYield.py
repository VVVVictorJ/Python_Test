import os
import time
import psutil
from multiprocessing import Process, Pool
from threading import Thread


def count(x, y):
    # 使程序完成50万计算
    c = 0
    while c < 10:
        c += 1
        x += x
        y += y


def genarator():
    for el in range(160):
        yield el


def func(x):
    time.sleep(1)
    print('【exec time {}】'.format(
        time.strftime(
            "%Y-%m-%d %H:%M:%S",
            time.localtime(psutil.Process(os.getpid()).create_time()))))
    return x + 1


if __name__ == '__main__':
    # t = time.time()
    # for x in range(10):
    #     count(1, 1)
    # print("Line", time.time() - t)

    # counts = []
    # t = time.time()
    # for x in range(16):
    #     thread = Thread(target=count, args=(1, 1))
    #     counts.append(thread)
    #     thread.start()
    # for thread in counts:
    #     thread.join()
    # print("Threading", time.time() - t)

    # counts = []
    t = time.time()
    # for x in range(16):
    #     process = Process(target=count, args=(1, 1))
    #     counts.append(process)
    #     process.start()
    # for process in counts:
    #     process.join()
    # print("Multiprocess", time.time() - t)
    gen = genarator()
    result = []
    with Pool(16) as p:
        results = p.imap(func, gen, 16)
        for res in results:
            print("res:", res)

    print("Multiprocess", time.time() - t)
