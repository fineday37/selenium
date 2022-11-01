import time
from threading import Thread

from selenium.webdriver import Remote, DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


# option = webdriver.ChromeOptions()
#
# option.add_argument("headless")


class BasePage:
    def __init__(self, drivers, db):
        node = {"browserName": db}
        self.driver = Remote(command_executor=drivers,
                             desired_capabilities=node
                             )

    def login(self):
        self.driver.get("https://work.taobao.com/")

        # driver.implicitly_wait(10)

        self.driver.find_element_by_xpath('//*[@id="ice-container"]/div/div[1]/div/a/button').click()
        time.sleep(1)
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        self.driver.switch_to.frame('alibaba-login-box')
        time.sleep(3)
        self.driver.find_element_by_css_selector('[name="fm-login-id"]').send_keys("世纪开元旗舰店:李虎")
        self.driver.find_element_by_css_selector('[name="fm-login-password"]').send_keys("sjky36588")
        self.driver.find_element_by_css_selector('[type="submit"]').click()
        time.sleep(2)
        self.driver.switch_to.frame('baxia-dialog-content')
        slider = self.driver.find_element_by_css_selector("#nocaptcha #nc_1_n1z")

        print(slider.size["width"])
        print(slider.size["height"])

        slider_areas = self.driver.find_elements_by_css_selector('.sm-pop-inner.nc-container')
        slider_area = slider_areas[0]
        # driver.switch_to.default_content()
        time.sleep(1)
        print(slider_area.size["width"])
        print(slider_area.size["height"])
        ActionChains(self.driver).click_and_hold(slider).perform()
        time.sleep(1)
        ActionChains(self.driver).move_to_element_with_offset(slider, slider_area.size["width"],
                                                              slider_area.size["height"]).perform()

        # time.sleep(2)
        # self.driver.find_element_by_css_selector('[type="submit"]').click()

        time.sleep(5)
        self.driver.find_elements_by_css_selector(".FirstClassMenu--navList--LWMJEjL div a")[4].click()
        self.driver.find_element_by_xpath(
            '//*[@id="icestark-container"]/div/div[4]/div/ul/li[1]/ul/li[4]/div/span/a').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="icestarkNode"]/div/div/div/div/div[1]/a[2]').click()

        handle = self.driver.window_handles
        self.driver.switch_to.window(handle[-1])

    def nickname(self, name):
        self.login()
        datas = []

        self.driver.find_element_by_css_selector('.next-input.next-medium.nickname [placeholder="请输入"]').send_keys(name)
        self.driver.find_element_by_css_selector('.next-btn.next-medium.next-btn-normal.button').click()
        time.sleep(2)
        element = self.driver.find_elements_by_xpath('//*[@class="_chatWrap_1fgcw_8"]')
        print(element)
        print(len(element))
        for i in range(len(element)):
            interval = self.driver.find_elements_by_xpath('//*[@class="_chatTime_1fgcw_62"]')[i].text

            service = self.driver.find_elements_by_xpath('//*[@class="_chatName_1fgcw_54"]')[i].text

            # print(driver.find_elements_by_xpath('//*[@class="_chatName_1fgcw_54"]//preceding-sibling::*'))
            time.sleep(1)

            ls = self.driver.find_elements_by_xpath('//*[@class="_chatName_1fgcw_54"]//preceding-sibling::*')
            if not isElementExist(ls):
                customer = ls[i].text
                datas.append({"interval": interval, "customer": customer, "service": service})
        time.sleep(1)
        self.driver.find_element_by_css_selector('.next-input.next-medium.nickname [placeholder="请输入"]') \
            .send_keys(Keys.CONTROL, "a")
        self.driver.find_element_by_css_selector('.next-input.next-medium.nickname [placeholder="请输入"]') \
            .send_keys(Keys.BACKSPACE)
        time.sleep(1)

        print(datas)


def isElementExist(text):
    flag = True
    try:
        text.get_attribute("arc")
        return flag

    except:
        flag = False
        return flag


def BreakList(N, names):
    n = N
    name = [names[i:i + n] for i in range(0, len(names), n)]
    return name


def distribution(user, routing):
    for browser, search in routing.items():
        BasePage(browser, search).nickname(user)


if __name__ == '__main__':
    lists = [{'http://localhost:5555/wd/hub': 'chrome',
              # 'http://10.27.1.171:5555/wd/hub': 'firefox',
              # 'http://10.27.1.169:6670/wd/hub': 'chrome'
              }, {'http://localhost:4444/wd/hub': 'chrome'}]
    users = ["w15620401365", "wangyiying2oo41119"]
    threads = []
    start = time.time()
    for z in list(zip(lists, users)):
        t = Thread(target=distribution, args=(z[1], z[0]))
        threads.append(t)
    for i in threads:
        i.start()
    for i in threads:
        i.join()
    end = time.time()
    print('进程消耗时间: {:.2f}'.format(end - start))
