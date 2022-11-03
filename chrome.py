import datetime

import time
from threading import Thread

from selenium.webdriver import Remote, DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from edge import getList, BreakList

# option = webdriver.ChromeOptions()
#
# option.add_argument("headless")
ls = webdriver.Chrome()
ls.get("https://work.taobao.com/")

ls.find_element_by_xpath('//*[@id="ice-container"]/div/div[1]/div/a/button').click()
time.sleep(1)
handles = ls.window_handles
ls.switch_to.window(handles[-1])
ls.switch_to.frame('alibaba-login-box')
time.sleep(1)
ls.find_element_by_css_selector('[name="fm-login-id"]').send_keys("益好旗舰店:李虎")
ls.find_element_by_css_selector('[name="fm-login-password"]').send_keys("sjky2022")
ls.find_element_by_css_selector('[type="submit"]').click()
time.sleep(2)


def isElementExist(text):
    flag = True
    try:
        ls.find_element_by_css_selector(text)
        return flag

    except:
        flag = False
        return flag


if isElementExist('#baxia-dialog-content'):
    ls.switch_to.frame('baxia-dialog-content')
    slider = ls.find_element_by_css_selector("#nocaptcha #nc_1_n1z")

    print(slider.size["width"])
    print(slider.size["height"])

    slider_areas = ls.find_elements_by_css_selector('.sm-pop-inner.nc-container')
    slider_area = slider_areas[0]
    time.sleep(1)
    print(slider_area.size["width"])
    print(slider_area.size["height"])
    ActionChains(ls).click_and_hold(slider).perform()
    time.sleep(1)
    ActionChains(ls).move_to_element_with_offset(slider, slider_area.size["width"],
                                                 slider_area.size["height"]).perform()

cookies = ls.get_cookies()
ls.quit()


class BasePage:
    def __init__(self, drivers, db):
        node = {'platform': 'ANY', "browserName": db, 'version': '', 'javascriptEnabled': True}
        self.driver = Remote(command_executor=drivers,
                             desired_capabilities=node
                             )

    def check_element_exists(self, element):
        try:
            self.driver.find_element_by_xpath(element)
            return True
        except Exception as e:
            return False

    def nickname(self, names):
        self.driver.get(
            "https://market.m.taobao.com/app/qn/im-history-search/index.html?spm=a21dfk.22864181.0.0.61cc74c8B4r8FE#/")
        self.driver.delete_all_cookies()
        for cookie in cookies:
            self.driver.add_cookie(
                {
                    "domain": ".taobao.com",
                    "name": cookie["name"],
                    "value": cookie["value"],
                    "path": "/",
                    "expires": None
                }
            )
        self.driver.get(
            "https://market.m.taobao.com/app/qn/im-history-search/index.html?spm=a21dfk.22864181.0.0.61cc74c8B4r8FE#/")
        datas = []
        time.sleep(2)

        yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        self.driver.find_element_by_css_selector('[placeholder="起始日期"]').click()
        time.sleep(1)
        self.driver.find_elements_by_css_selector('[placeholder="YYYY-MM-DD"]')[0].send_keys(Keys.CONTROL, "a")
        self.driver.find_elements_by_css_selector('[placeholder="YYYY-MM-DD"]')[0].send_keys(Keys.BACKSPACE)
        self.driver.find_elements_by_css_selector('[placeholder="YYYY-MM-DD"]')[0].send_keys(str(yesterday))
        self.driver.find_elements_by_css_selector('[placeholder="YYYY-MM-DD"]')[1].click()
        self.driver.find_elements_by_css_selector('[placeholder="YYYY-MM-DD"]')[1].send_keys(str(yesterday))
        self.driver.find_elements_by_css_selector('[placeholder="YYYY-MM-DD"]')[0].click()
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button/span').click()
        time.sleep(2)
        for name in names:
            try:
                self.driver.find_element_by_css_selector(
                    '.next-input.next-medium.nickname [placeholder="请输入"]').send_keys(name)
                self.driver.find_element_by_css_selector('.next-btn.next-medium.next-btn-normal.button').click()
                time.sleep(3)
                if not self.check_element_exists('//*[@class="results-list"]'):
                    element = self.driver.find_elements_by_xpath('//*[@class="_chatWrap_1fgcw_8"]')
                    # print(element)
                    print(len(element))
                    self.traverse(element, datas, name, yesterday)
                else:
                    same_names = self.driver.find_elements_by_css_selector('.message-list-left .results-list')
                    for o in same_names:
                        o.click()
                        time.sleep(1)
                        element_same = self.driver.find_elements_by_xpath('//*[@class="_chatWrap_1fgcw_8"]')
                        for s in range(len(element_same)):
                            interval = self.driver.find_elements_by_xpath('//*[@class="_chatTime_1fgcw_62"]')[s].text

                            service = self.driver.find_elements_by_xpath('//*[@class="_chatName_1fgcw_54"]')[s].text

                            ls = self.driver.find_elements_by_xpath(
                                '//*[@class="_chatName_1fgcw_54"]//preceding-sibling::*')
                            if ls[s].get_attribute("class") == "_chatTextLeft_1fgcw_32":
                                customer = ls[s].text
                                datas.append(
                                    {"customCare": name, "datetime": str(yesterday) + " " + interval,
                                     "customer": customer,
                                     "service": service})
                            elif ls[s].get_attribute("class") == "_img_1fgcw_50":
                                customer = ls[s].get_attribute("src")
                                datas.append(
                                    {"customCare": name, "datetime": str(yesterday) + " " + interval,
                                     "customer": customer,
                                     "service": service})
                self.driver.find_element_by_css_selector('.next-input.next-medium.nickname [placeholder="请输入"]') \
                    .send_keys(Keys.CONTROL, "a")
                self.driver.find_element_by_css_selector('.next-input.next-medium.nickname [placeholder="请输入"]') \
                    .send_keys(Keys.BACKSPACE)
            except Exception as e:
                print(e)
                with open("./error.txt", mode="a") as f:
                    f.write(name)
                    f.write('\n')
                time.sleep(10)
                self.driver.find_element_by_css_selector('.next-input.next-medium.nickname [placeholder="请输入"]') \
                    .send_keys(Keys.CONTROL, "a")
                self.driver.find_element_by_css_selector('.next-input.next-medium.nickname [placeholder="请输入"]') \
                    .send_keys(Keys.BACKSPACE)

        time.sleep(1)
        self.driver.quit()

    def traverse(self, element, datas, name, yesterday):
        for i in range(len(element)):
            interval = self.driver.find_elements_by_xpath('//*[@class="_chatTime_1fgcw_62"]')[i].text

            service = self.driver.find_elements_by_xpath('//*[@class="_chatName_1fgcw_54"]')[i].text

            ls = self.driver.find_elements_by_xpath('//*[@class="_chatName_1fgcw_54"]//preceding-sibling::*')
            if ls[i].get_attribute("class") == "_chatTextLeft_1fgcw_32":
                customer = ls[i].text
                datas.append({"customCare": name, "datetime": str(yesterday) + " " + interval, "customer": customer,
                              "service": service})
            elif ls[i].get_attribute("class") == "_img_1fgcw_50":
                customer = ls[i].get_attribute("src")
                datas.append({"customCare": name, "datetime": str(yesterday) + " " + interval, "customer": customer,
                              "service": service})


def distribution(user, routing):
    for browser, search in routing.items():
        BasePage(browser, search).nickname(user)


if __name__ == '__main__':
    lists = [
        {'http://10.27.1.100:8888/wd/hub': 'chrome'},
        {"http://10.27.1.100:6666/wd/hub": 'chrome'},
        {'http://10.27.1.100:7777/wd/hub': 'chrome'},
        {'http://10.27.1.100:9999/wd/hub': 'chrome'},
        {"http://10.27.1.100:6668/wd/hub": 'chrome'},
        {"http://10.27.1.100:6669/wd/hub": 'chrome'},
        {"http://10.27.1.100:6667/wd/hub": 'chrome'},
        {'http://10.27.1.12:5555/wd/hub': 'chrome'},
        {'http://10.27.1.12:6688/wd/hub': 'chrome'},
        {'http://10.27.1.12:5558/wd/hub': 'chrome'},
        ]
    # lists = [
    #     {'http://10.27.1.12:5555/wd/hub': 'chrome'},
    #     {'http://10.27.1.12:6688/wd/hub': 'chrome'},
    #     ]
    # users = [["woshinide1998程思雨", "世纪开元旗舰店:合欢"], ["世纪开元旗舰店:小星", "tb170394291"]]
    users = getList()
    user = BreakList(10, users)
    len(user)
    print("用户数: {}".format(len(user)))
    threads = []
    start = time.time()
    for z in list(zip(lists, user)):
        t = Thread(target=distribution, args=(z[1], z[0]))
        threads.append(t)
    for i in threads:
        i.start()
    for i in threads:
        i.join()
    end = time.time()
    print('进程消耗时间: {:.2f}'.format(end - start))
