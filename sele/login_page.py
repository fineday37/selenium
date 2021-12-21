from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains


def delay(time_):
    time.sleep(time_)


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # 隐性等待
    def waiting(self, seconds):
        self.driver.implicitly_wait(seconds)

    # 获取url
    def open(self, url):
        self.driver.get(url)

    # 输入文本
    def input(self, loc, txt):
        self.lacator(loc).send_keys(txt)

    # 点击
    def click(self, loc):
        self.lacator(loc).click()

    # 关闭
    def quit(self):
        self.driver.quit()

    # 全选文本
    def clear(self, loc):
        self.lacator(loc).send_keys(Keys.CONTROL, "a")

    # 删除文本
    def clear1(self, loc):
        self.lacator(loc).send_keys(Keys.BACKSPACE)

    # 定位元素
    def lacator(self, loc):
        return self.driver.find_element(*loc)

    # 复数定位
    def plural(self, elements, i):
        return self.driver.find_elements_by_css_selector(elements)[i]

    # 全屏
    def max(self):
        self.driver.maximize_window()

    # 刷新页面
    def re(self):
        self.driver.refresh()

    # 双击事件
    def double(self, loc):
        ActionChains(self.driver).double_click(self.lacator(loc)).perform()
