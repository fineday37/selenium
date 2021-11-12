from selenium import webdriver
from sele.login_page import BasePage
from selenium.webdriver.common.by import By
import time


# wb = webserver.Chrome(r'C:\chromedriver.exe')
# wb.get("http://www.baidu.com")
class Loginpage(BasePage):
    url = "http://10.168.20.17:8081/"
    user = (By.XPATH, '//*[@id="app"]/div/form/div/div[2]/div[2]/div/div[1]/div/input')
    but = (By.XPATH, '//*[@id="app"]/div/form/div/div[2]/div[5]/div/div/div/input')
    clack = (By.XPATH, '//*[@id="app"]/div/form/div/div[2]/button')
    txt = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/div[2]/div[1]/div/div')
    text = (By.XPATH, '/html/body/div[2]/div/div/div[1]/div/span')
    ll = (By.XPATH, '//*[@id="app"]/div/div[2]/ul/div[1]/i')
    goods = (By.XPATH, '//*[@id="app"]/div/div[1]/div/div[1]/ul/div/li[1]/ul/a[4]')
    business = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[1]/div/div[1]/form/div[1]/div/div[1]/div['
                          '3]/div/button')
    an = (By.XPATH, '//*[@id="app"]/div/div[1]/div/div[1]/ul/div/li[1]/div/i[2]')
    new = (By.CSS_SELECTOR, '.ivu-modal-content [placeholder="请输入关键字搜索"]')
    classification = (By.CSS_SELECTOR, '.search-btn.ivu-btn.ivu-btn-primary.ivu-btn-icon-only')
    product = (By.CSS_SELECTOR, '.ivu-table-body .ivu-table-row .ivu-table-cell')
    newss = (
        By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[1]/div/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/span')
    nc = (By.CSS_SELECTOR, '.ky-modal-menu-wrap .ivu-menu-item.ivu-menu-item-active.ivu-menu-item-selected ')
    banner = (By.CSS_SELECTOR, '.ky-modal-goods.ivu-menu.ivu-menu-light.ivu-menu-vertical li')
    speci = (By.XPATH, '.ivu-menu-item .ivu-btn.ivu-btn-dashed.ivu-btn-small')
    tt = ".ivu-menu-item .ivu-btn.ivu-btn-dashed.ivu-btn-small"

    def login(self, user, passwd):
        self.Waiting(10)
        self.open(self.url)
        self.input(self.user, user)
        self.input(self.but, passwd)
        self.click(self.clack)
        time.sleep(2)
        self.max()
        self.re()
        time.sleep(2)
        text = self.lacator(self.txt).text
        return text

    def logins(self, user, passwd):
        self.Waiting(10)
        self.open(self.url)
        self.max()
        if user is not None:
            self.input(self.user, user)
        if passwd is not None:
            self.input(self.but, passwd)
        self.click(self.clack)
        time.sleep(1)
        txt = self.lacator(self.text)
        self.quit()
        return txt

    def news(self):
        self.click(self.ll)
        self.click(self.an)
        self.click(self.goods)
        self.click(self.business)
        time.sleep(1)
        self.input(self.new, "17852170964")
        time.sleep(1)
        self.click(self.classification)
        self.click(self.product)
        self.click(self.newss)
        self.click(self.nc)
        self.click(self.banner)
        time.sleep(1)
        self.plural(self.tt, 6).click()
        # self.driver.find_elements_by_css_selector('.ivu-menu-item .ivu-btn.ivu-btn-dashed.ivu-btn-small')[6].click()
        self.plural(self.tt, 1).click()
        # self.driver.find_elements_by_css_selector('.ivu-menu-item .ivu-btn.ivu-btn-dashed.ivu-btn-small')[1].click()
        time.sleep(1)
        self.plural(self.tt, 3).click()
        # self.driver.find_elements_by_css_selector('.ivu-menu-item .ivu-btn.ivu-btn-dashed.ivu-btn-small')[3].click()
        self.driver.find_elements_by_css_selector('.ivu-btn.ivu-btn-primary')[14].click()
        txt = self.driver.find_elements_by_css_selector('.ivu-table-column-center .ivu-table-cell div span')[0].text
        return txt


if __name__ == '__main__':
    lp = Loginpage(webdriver.Chrome())
    lp.login("suchangzhou", "sjky2018")
