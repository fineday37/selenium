import json

import requests
import pprint
import os
import date
import xlwings


def send(method, urls, datas, **kwargs):
    if method == "get":
        re = requests.request(method=method, url=urls, params=datas, **kwargs)
    if method == "post":
        dates = json.dumps(data)
        re = requests.request(method=method, url=urls, data=dates, **kwargs)
    else:
        print("405")
    return re


url = "http://10.168.20.48:9000/api/auth/login/account"
data = {
    "account": "220311379",
    "password": "sjky220311379"
}
headers = {
    "Content-Type": "application/json"
}
res = send("post", url, data, headers=headers)
pprint.pprint(res.content)
print(str(res.json()))
with open('yello.txt', "a+") as f:
    f.write(str(res.json()))
f.close()
print(date.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
