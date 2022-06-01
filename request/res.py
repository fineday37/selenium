import json

import requests
from request import basis
import pprint
from sele.read_yaml import Readyaml

case = Readyaml("../sele/api.yaml").read_yaml()


class Request:
    s = {}

    # 登录并获取cookie
    def requets(self, urls, method, data):
        url = "http://" + urls
        res = basis.reCSV(method, url, data)
        print(res.status_code)
        # print(type(res.json()))
        pprint.pprint(res.json())
        cookies = res.cookies
        cookie = requests.utils.dict_from_cookiejar(cookies)
        Request.s["Cookie"] = cookie
        print(type(data))
        pprint.pprint(Request.s)
        return res.json()

    # 订单查询
    def query(self):
        method = "post"
        url = "http://10.168.20.17:8081/odr/order/sheet/queryOrderList.do"
        headers = {"Content-Type": "application/json"}
        body = {
            "startTime": "2021-09-28T16:00:00.000Z", "stopTime": "2021-09-29T15:59:59.999Z", "startTimeAchv": None,
            "stopTimeAchv": None, "sheetCode": "", "assistSheetCode": "", "achvState": "", "achvStateAlias": "00",
            "processNodeCode": "", "processNodeCodeAlias": ["00"], "memberName": "17852170964",
            "memberContactPhone": "",
            "memberContactName": "", "goodsCategoryCode": "", "goodsCategoryCodeAlias": "00", "goodsClassCode": "",
            "goodsClassCodeAlias": "00", "payStateCode": "", "payStateCodeAlias": "00", "createUserCode": "",
            "createUserCodeAlias": "00", "sellUserCode": "", "sellUserCodeAlias": "00", "orderTask": "",
            "orderTaskAlias": "全部", "orderClass": "", "orderClassAlias": "全部", "orderLabel": "",
            "orderLabelAlias": "全部",
            "orderDeliveryMethod": "", "orderDeliveryMethodAlias": "全部", "valid": "1", "tenantCode": "", "pageNum": 1,
            "pageSize": 10, "queryTimeType": "00", "performanceUserList": [], "strId": "", "lockOrderS": "0",
            "userList": "", "source": "", "processUserCode": "0", "operCode": "a385203b-b713-4e8e-9a5d-df5e51c9ac52"
        }
        data = json.dumps(body)
        res = requests.request(method=method, url=url, data=data, headers=headers, cookies=Request.s["Cookie"])
        print(res.status_code)
        print(type(res))
        pprint.pprint(res.json())
        return res.json()
        # ll = res.json()
        # print(ll["userData"]["orderList"][1]["realPrice"])


if __name__ == '__main__':
    date = {
        "userName": "kaiyuan_shanda",
        "passwd": "981abd4f4a49b37c79243e2da3cf95f0"
    }
    Request().requets("10.168.20.17:8081/logon/doLogin.do", "post", date)
    # Request().query()
    # print(Request().s)
