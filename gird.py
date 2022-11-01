import time
from threading import Thread

# from selenium.webdriver import Remote
from selenium import webdriver


def baidu():
    # print("start: {}".format(time.ctime()))
    # print("浏览器: {}".format(db))
    url = 'http://10.168.20.17:8081/'
    # # driver = webdriver.Firefox()
    # node = {"browserName": db}
    # driver = webdriver.Remote(command_executor=host,
    #                           desired_capabilities=node  # 浏览器名称
    #                           )

    driver = webdriver.Chrome()
    driver.get(url=url)
    ri = driver.get_cookies()
    print(len(ri), ri)
    driver.find_element_by_xpath('//*[@id="app"]/div/form/div/div[2]/div[2]/div/div[1]/div/input').send_keys(
        "suchangzhou")
    driver.find_element_by_xpath('//*[@id="app"]/div/form/div/div[2]/div[5]/div/div/div/input').send_keys("sjky2018")
    driver.find_element_by_xpath('//*[@id="app"]/div/form/div/div[2]/button').click()
    time.sleep(5)
    cookies = driver.get_cookies()
    print(cookies, len(cookies))
    return cookies
    # # driver.quit()
    # time.sleep(2)
    # driver.delete_all_cookies()
    # print("清除后：{}".format(driver.get_cookies()))
    # time.sleep(2)
    # driver.get('http://10.168.20.17:8081/odr/odrListOrder')
    # time.sleep(2)
    # for i in cookies:
    #     driver.add_cookie(i)
    # time.sleep(2)
    # driver.get("http://10.168.20.17:8081/odr/odrListOrder")
    # time.sleep(3)


def query():
    driver = webdriver.Chrome()
    driver.get("http://10.168.20.17:8081/odr/odrNewOrder")
    cookies = baidu()
    for j in cookies:
        driver.add_cookie(j)
    time.sleep(1)
    driver.get("http://10.168.20.17:8081/odr/odrNewOrder")


if __name__ == '__main__':
    # lists = {'http://10.27.1.12:5555/wd/hub': 'firefox',
    #          'http://10.27.1.12:5556/wd/hub': 'chrome',
    #          # 'http://10.27.1.169:6666/wd/hub': 'chrome'
    #          }
    # threads = []
    # files = range(len(lists))
    # start = time.time()
    # for browser, search in lists.items():
    #     t = Thread(target=baidu, args=(browser, search))
    #     threads.append(t)
    # for i in threads:
    #     i.start()
    # for i in threads:
    #     i.join()
    # end = time.time()
    # print('进程消耗时间: {0}'.format(end - start))
    query()
