from threading import Thread

from selenium.webdriver import Remote
import time
from selenium import webdriver

def baidu(host, db):
    print("start: {}".format(time.ctime()))
    print("浏览器: {}".format(db))
    url = 'http://www.baidu.com'
    # driver = webdriver.Firefox()
    node = {"browserName": db}
    driver = Remote(command_executor = host,
                    desired_capabilities = node # 浏览器名称
                    )

    driver.get(url=url)
    driver.find_element_by_id('kw').send_keys('python')
    driver.find_element_by_id('su').click()
    time.sleep(3)
    driver.quit()

if __name__ == '__main__':
    lists = {'http://192.168.94.1:5555/wd/hub': 'firefox',
             #'http://192.168.94.1:5556/wd/hub': 'chrome',
             'http://10.27.1.169:6666/wd/hub': 'chrome'
             }
    threads = []
    files = range(len(lists))
    start = time.time()
    for browser, search in lists.items():
        t = Thread(target=baidu, args=(browser, search))
        threads.append(t)
    for i in threads:
        i.start()
    for i in threads:
        i.join()
    end = time.time()
    print('进程消耗时间: {0}'.format(end-start))

