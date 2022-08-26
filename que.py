import threading
import time
import queues


def producer():
    count = 1
    while True:
        q.put('No.%i' % count)
        print('Producer put No.%i' % count)
        time.sleep(1)
        count += 1


def customer(name):
    while True:
        print('%s get %s' % (name, q.get()))
        time.sleep(1.5)


q = queues.Queue(maxsize=5)
p = threading.Thread(target=producer, )
c = threading.Thread(target=customer, args=('jack',))
p.start()
c.start()
