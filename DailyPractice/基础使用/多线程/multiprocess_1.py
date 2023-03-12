import datetime
import os
import random
import time
import psutil
from multiprocessing import Pool, Process, cpu_count


def func(name):
    # os.getpid() 获取当前进程ID
    print('【process {} starts】'.format(os.getpid()))
    print('【process create time {}】'.format(
        time.strftime(
            "%Y-%m-%d %H:%M:%S",
            time.localtime(psutil.Process(os.getpid()).create_time()))))
    # time.sleep(random.randint(1,3))
    time.sleep(2)
    # currentDateAndTime = datetime.now()
    # print('【process {} ends】【now is {}】'.format(str(os.getpid()), currentDateAndTime))
    print('【process {} ends】'.format(os.getpid()))


def task(n):
    print('【process {} starts】'.format(os.getpid()))
    time.sleep(n)  # 模拟任务执行的时间
    print('【process {} ends】'.format(os.getpid()))


if __name__ == '__main__':
    print('【main process is 】 {}'.format(os.getpid()))
    print('【core number is 】{}'.format(cpu_count()))
    start_time = time.time()
    # multiprocess pool
    p = Pool(processes=4)
    # # 方法一
    # for i in range(14):
    #     # 往进程池中添加待执行的任务
    #     p.apply_async(task)

    #方法二
    p.map_async(func, range(32))

    #方法三
    # for i in range(4):
    #     p.apply_async(func, (i,))
    p.close()
    p.join()
    end_time = time.time()
    print('【total time is 】{}'.format(str(end_time - start_time)))