import time

from sele.automatic import Loginpage
import pytest
from sele.read import Readyaml
from selenium import webdriver
from log.logs import loggings
from request import mysql
import allure

lg = loggings()
r = Readyaml('../sele/api.yaml').read_yaml()
t = Readyaml('../sele/login.yaml').read_yaml()


@pytest.fixture()
def test1():
    ll = mysql.datas()
    return ll


@pytest.fixture()
def test2():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://10.168.20.17:8081/")
    driver.find_element_by_xpath('//*[@id="app"]/div/form/div/div[2]/div[2]/div/div[1]/div/input').send_keys(
        "suchangzhou")
    driver.find_element_by_xpath('//*[@id="app"]/div/form/div/div[2]/div[5]/div/div/div/input').send_keys("sjky2018")
    driver.find_element_by_xpath('//*[@id="app"]/div/form/div/div[2]/button').click()
    driver.maximize_window()
    time.sleep(1)
    driver.refresh()
    return driver


class TestPage:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.lp = Loginpage(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @allure.feature("登录成功")
    @pytest.mark.parametrize("arg", r)
    def test_001(self, arg, test1):
        try:
            text = arg["name"]["xing"]
            passwd = arg["name"]["ming"]
            # lp = Logging(webserver.Chrome(r'C:\chromedriver.exe'))
            txt = self.lp.login(text, passwd)
            assert txt == "Hi~高新体验店欢迎你！"
            lg.info("登陆成功，账号是{}，密码是{}".format(text, passwd))
            print(test1)
        except Exception as e:
            lg.error(e)

    @allure.feature("添加商品成功")
    def test_003(self):
        try:
            txt = self.lp.news()
            assert txt == "工厂名片"
            lg.info("新建商品成功,商品名称为{}".format(txt))
        except Exception as e:
            lg.error(e)

    @allure.feature("查询")
    def test_oo4(self):
        try:
            assert self.lp.query() == Loginpage.coding["cod"]
            lg.info("查询成功，订单号是{},商品是{}".format(Loginpage.Serial["jean"], Loginpage.coding["cod"]))
        except Exception as e:
            lg.error(e)


class TestPage01:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.lp = Loginpage(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize("grep", t)
    def test_002(self, grep):
        text = grep["name"]["xing"]
        passwd = grep["name"]["ming"]
        txt = self.lp.logins(text, passwd)
        assert txt == "账号或密码不对"


class TestPage02:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.lp = Loginpage(self.driver)

    def teardown_class(self):
        self.driver.quit()

    def test_003(self, test2):
        assert 3 == 3


if __name__ == '__main__':
    pytest.main("-vs ")
