from selenium import webdriver
from sele.login_page import BasePage
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

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
    goods = (By.XPATH, '//*[@id="app"]/div/div[1]/div/div[1]/ul/div/li[1]/ul/a[4]/span')
    business = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[1]/div/div[1]/form/div[1]/div/div[1]/div['
                          '3]/div/button')
    an = (By.XPATH, '//*[@id="app"]/div/div[1]/div/div[1]/ul/div/li[1]/div/i[2]')
    new = (By.CSS_SELECTOR, '.ivu-select-selection [placeholder="请输入关键字进行搜索"]')
    classification = (By.CSS_SELECTOR, '.ivu-modal-header .ivu-select-dropdown .ivu-select-dropdown-list')
    product = (By.CSS_SELECTOR, '.ivu-table-body .ivu-table-row .ivu-table-column-center .ivu-table-cell')
    newss = (
        By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[1]/div/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/span')
    culture = '.ky-modal-menu-wrap.ivu-menu.ivu-menu-light.ivu-menu-vertical li'
    banner = '.ky-modal-goods.ivu-menu.ivu-menu-light.ivu-menu-vertical .ivu-menu-submenu'
    speci = (By.XPATH, '.ivu-menu-item .ivu-btn.ivu-btn-dashed.ivu-btn-small')
    tt = ".ivu-btn.ivu-btn-dashed.ivu-btn-small"
    save = (By.CSS_SELECTOR, '.ky-wrap-foot .ivu-btn.ivu-btn-primary')
    stores = ".vue-scroller-bars-content .ivu-menu-submenu .ivu-menu .ivu-menu-item"
    coding = {}
    search = '.ky-form-split .ivu-form-item-content [type="text"]'
    Query_button = '.ky-form-split .ivu-form-item-content [type="button"]'
    Verification_code = ".ivu-table-row .ivu-table-column-center .ivu-table-cell"
    Serial = {}

    # 登录

    def login(self, user, passwd):
        self.waiting(10)
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

    # 登录无效等价类

    def logins(self, user, passwd):
        self.waiting(10)
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

    # 门店订单查询

    def query(self):
        self.waiting(10)
        self.plural(self.stores, 4).click()
        time.sleep(2)
        self.plural(self.search, 0).send_keys(Keys.CONTROL, "v")
        self.plural(self.Query_button, 0).click()
        time.sleep(2)
        text = self.plural(self.Verification_code, 7).text
        self.Serial["jean"] = self.plural(self.Verification_code, 3).text
        return text

    # 新增门店订单

    def news(self):
        self.waiting(10)
        self.click(self.ll)
        self.click(self.an)
        self.click(self.goods)
        self.click(self.business)
        time.sleep(1)
        self.input(self.new, "17852170964")
        time.sleep(2)
        self.click(self.classification)
        time.sleep(2)
        # 鼠标双击
        self.double(self.product)
        time.sleep(1)
        self.click(self.newss)
        time.sleep(1)
        self.plural(self.culture, 1).click()
        time.sleep(1)
        self.plural(self.banner, 7).click()
        time.sleep(1)
        # self.plural(self.tt, 12).click()
        # time.sleep(1)
        self.driver.find_elements_by_css_selector('.ivu-btn.ivu-btn-primary')[14].click()
        time.sleep(2)
        txt = self.driver.find_elements_by_css_selector('.ivu-table-column-center .ivu-table-cell div span')[0].text
        self.click(self.save)
        time.sleep(3)
        self.coding["cod"] = self.plural('.ivu-table-column-center .ivu-table-cell div span', 0).text
        self.plural('.ivu-form-item-content [type="button"]', 0).click()
        return txt


if __name__ == '__main__':
    lp = Loginpage(webdriver.Chrome())
    lp.login("suchangzhou", "sjky2018")
