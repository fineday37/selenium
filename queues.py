import queue

q = queue.Queue(maxsize=5)
q.put(1, block=False)
q.put(2, block=False)
q.put(3, block=True)
q.put(4, block=True)
print(q.get())

print(q.qsize())
import threading
import time

sum_1 = 0


def run(i):
    global sum_1
    time.sleep(1)
    # lock.acquire()
    semaphore.acquire()
    sum_1 += 1
    print("线程%s来了,并修改了sum_1的值为：%s" % (i, sum_1))
    semaphore.release()
    # lock.release()


# lock = threading.Lock()
semaphore = threading.RLock()
name = ["第一个", "第二个", "第三个", "第四个"]
threadings = []
for x in name:
    t = threading.Thread(target=run, args=(x,))
    threadings.append(t)
for i in threadings:
    i.start()
for j in threadings:
    j.join()
while threading.active_count() != 1:
    pass

print(threadings)


def light():
    count = 1
    event.set()  # 设置标志位 True
    while True:
        if count <= 10:
            print("现在是绿灯")
            time.sleep(1)
        elif count <= 15:
            print("现在是红灯")
            event.clear()  # 清空标志位(将标志位改为false)
            time.sleep(1)
        else:
            count = 0
            event.set()
        count += 1


def car(name):
    while True:
        if event.is_set():
            print("----------%s在起飞-------------" % name)
            time.sleep(1)
        else:
            print("---------%s在等红灯---------------" % name)
            event.wait()  # 等待标志位被设置位True程序才继续往下运行


event = threading.Event()
light_1 = threading.Thread(target=light)
light_1.start()
for x in range(5):
    car_1 = threading.Thread(target=car, args=("马自达" + str(x),))
    car_1.start()
