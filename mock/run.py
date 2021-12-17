import requests
import pprint
data = {
    'out_trade_no': '20150320010101001',
    'auth_code': '28763443825664394',
    'buyer_id': '2088202954065786',
    'seller_id': '2088102146225135',
    'subject': 'Iphone6',
    'total_amount': '88.88',
}
res = requests.post("http://127.0.0.1:9091/trade/purchase", json=data)
print(type(res.json()))
pprint.pprint(res.json())
