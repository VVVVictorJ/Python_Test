from multiprocessing import Process

'''
协程, 生产者生产消息后, 通过yield跳转到消费者执行, 待消费者执行完毕后， 切换回生产者继续生产, 效率极高.
'''

def consumer():
    print("[CONSUMER] start")
    r = 'start'
    while True:
        # 接受信号后再生成
        n = yield r
        # if not n:
        #     print("n is empty")
        #     continue
        print("[CONSUMER] Consumer is consuming {}".format(n))
        r = "200 ok"

def producer(c):
    start_value = c.send(None)
    print(start_value)
    n = 0
    while n < 3:
        n += 1
        print("[PRODUCER] Producer is producing {}".format(n))
        # 通过send发送信息
        r = c.send(n+5)
        print('[PRODUCER] Consumer return: {}' .format(r))
    c.close()

# 创建生成器
c = consumer()
# 传入generator
producer(c)
