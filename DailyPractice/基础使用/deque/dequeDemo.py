from collections import deque

my_queue = deque(maxlen=10)

for i in range(10):
    my_queue.append(i + 1)

print(my_queue)

for i in range(10, 15):
    my_queue.append(i + 1)
    
print(my_queue)
