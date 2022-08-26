import pytest

from request import res
import allure
import os
from log.logs import loggings
from request import mysql
from sele.read_yaml import Readyaml
case = Readyaml("../sele/api.yaml").read_yaml()
log1 = loggings()


@pytest.fixture()
def test1():
    ll = mysql.datas()
    return ll


class Testpage:
    @allure.feature("登陆成功")
    @pytest.mark.parametrize("arg", case)
    def test_001(self, test1, arg):
        url = arg["url"]
        method = arg["method"]
        data = arg["name"]
        stores = arg["stores"]
        text = res.Request.requets(url, method, data)
        txt = text["userData"]["userInfo"]["realName"]
        try:
            assert txt == stores
            log1.info("登录账号是{}".format(txt))
            print(test1)
        except Exception as e:
            log1.error(e)

    # @allure.feature("查询成功")
    # def test_002(self):
    #     text = res.Request.query(self)
    #     realprice = text["userData"]["orderList"][1]["realPrice"]
    #     saleprice = text["userData"]["orderList"][1]["salePrice"]
    #     discountPrice = text["userData"]["orderList"][1]["discountPrice"]
    #     try:
    #         c = int(saleprice) - int(realprice)
    #         assert int(discountPrice) == c
    #         log1.info("原价为{}，折价为{}，现价为{}".format(saleprice, realprice, discountPrice))
    #     except Exception as e:
    #         log1.error(e)


if __name__ == '__main__':
    pytest.main(["-vs"])
