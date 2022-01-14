import threading
import time

people = 500  # 假设有500个人


def action(num):
    global people
    while people > 0:
        people -= 50  # 每次运输50人
        print("车辆编号：%d, 当前车站人数：%d" % (num, people))
        time.sleep(1)


start = time.time()
vehicles = []  # 新建车辆组
for num in range(5):
    vehicle = threading.Thread(target=action, args=(num,))  # 新建车辆
    vehicles.append(vehicle)  # 添加车辆到车辆组中

for vehicle in vehicles:
    vehicle.start()  # 分别启动车辆

for vehicle in vehicles:
    vehicle.join()  # 分别检查到站车辆
end = time.time()
print("Duration time: {0}".format(end - start))
