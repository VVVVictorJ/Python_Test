import os
import time

from multiprocessing import Process, cpu_count, Pool
from multiprocessing import Queue


def consumer(q, name):
    while True:
        res = q.get()
        if res is None:break
        print("{} 吃了 {}".format(name, res))


def producer(q, name, food):
    for i in range(3):
        time.sleep(1)
        res = "{} {}".format(food, i)
        print("{} 生产了 {}".format(name, res))
        q.put(res)


if __name__ == "__main__":
    #创建队列
    q = Queue()
    # 创建生产者
    p1 = Process(target=producer, args=(q, "kelly", "西瓜"))
    c1 = Process(target=consumer, args=(
        q,
        "peter",
    ))
    p1.start()
    c1.start()

    p1.join()
    q.put(None)
    print("主进程")
