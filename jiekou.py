import requests

res = requests.get("http://10.168.20.17:8081/logon/doLogin.do")
print(res.status_code)