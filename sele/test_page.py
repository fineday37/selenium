from sele.automatic import Loginpage
import pytest
from sele.read import Readyaml
from selenium import webdriver
from log.logs import loggings

lg = loggings()
r = Readyaml('../sele/api.yaml').read_yaml()
t = Readyaml('../sele/login.yaml').read_yaml()


class Test_page:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.lp = Loginpage(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize("arg", r)
    def test_001(self, arg):
        try:
            text = arg["name"]["xing"]
            passwd = arg["name"]["ming"]
            # lp = Logging(webserver.Chrome(r'C:\chromedriver.exe'))
            txt = self.lp.login(text, passwd)
            assert txt == "Hi~高新体验店欢迎你！"
            lg.info("登陆成功，账号是{}，密码是{}".format(text, passwd))
        except Exception as e:
            lg.error(e)

    def test_003(self):
        try:
            txt = self.lp.news()
            assert txt == "测试规格"
            lg.info("新建商品成功,商品名称为{}".format(txt))
        except Exception as e:
            lg.error(e)


class Test_page01:
    def setup_class(self):
        self.driver = webdriver.Chrome(r'C:\chromedriver.exe')
        self.lp = Loginpage(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize("grep", t)
    def test_002(self, grep):
        text = grep["name"]["xing"]
        passwd = grep["name"]["ming"]
        txt = self.lp.logins(text, passwd)
        assert txt == "账号或密码不对"


if __name__ == '__main__':
    pytest.main("-vs ")
