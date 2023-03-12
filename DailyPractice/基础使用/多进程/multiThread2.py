import os
import time

from multiprocessing import Process, cpu_count, Pool

def write_to_queue(queue):
    for index in range(5):
        print('write {} to {}'.format(str(index), queue))
        queue.put(index)
        time.sleep(1)


def read_from_queue(queue):
    while True:
        result = queue.get()
        if result is None:break
        print('get {} from {}'.format(str(result), queue))


if __name__ == '__main__':

    print('main process is {}'.format(os.getpid()))
    print('core number is {}'.format(cpu_count()))  # 8
    start_time = time.time()
	### multiprocess queue
    from multiprocessing import Queue
    queue = Queue()
    pw = Process(target=write_to_queue, args=(queue,))
    pr = Process(target=read_from_queue, args=(queue,))
    pw.start()
    pr.start()
    pw.join()
    # 结束信号
    queue.put(None)
    end_time = time.time()
    print('total time is {}'.format(str(end_time - start_time)))
