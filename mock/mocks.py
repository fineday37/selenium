import json

from flask import Flask, request
import datetime

app = Flask(__name__)


@app.route('/')
def hello():
    return "<h1>这是一个mock<h2>"


@app.route('/trade/purchase', methods=["post"])
def _mock():
    res = json.loads(request.get_data())
    out_trade_no = res['out_trade_no']
    auth_code = res['auth_code']
    data = {'code': '400004', 'msg': 'Business Failed', 'sub_code': 'ACQ.TRADE_HAS_SUCCESS', 'sub_msg': '交易已被支付',
            'trade_no': datetime.datetime.now().strftime("%Y--%m--%d %H:%M:%S"),
            'out_trade_no': out_trade_no}
    if auth_code != '28763443825664394':
        return {'code': '50000', 'msg': '请求校验码失败'}
    return data


if __name__ == '__main__':
    app.run("127.0.0.1", 9091)
