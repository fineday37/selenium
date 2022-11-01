import json
import random

from flask import Flask, request, abort, jsonify
import date

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1><font size="8" color="red">这是一个mock</font><h1>'


@app.route('/trade/purchase', methods=["post"])
def _mock():
    res = request.json
    # res = json.loads(request.get_data())
    out_trade_no = res['out_trade_no']
    auth_code = res['auth_code']
    data = {'code': '400004', 'msg': 'Business Failed', 'sub_code': 'ACQ.TRADE_HAS_SUCCESS', 'sub_msg': '交易已被支付',
            'trade_no': date.datetime.now().strftime("%Y--%m--%d %H:%M:%S"),
            'out_trade_no': out_trade_no}
    if auth_code != '28763443825664394':
        return {'code': '50000', 'msg': '请求校验码失败'}
    return data


@app.route('/user/<username>')
def show_user_profile(username):
    return "user:{}".format(username)


@app.route('/api/user/reg', methods=["post"])
def reg():
    if not request.json or not "name" in request.json or not "password" in request.json:
        abort(404)
    res = [
        {
            "code": "100",
            "msg": "成功",
            "data": {"name": "Hello",
                     "password": "3274329874"}
        },
        {
            "code": "200",
            "msg": "失败，用户存在",
            "data": {
                "name": "Hello",
                "password": "8738473"
            }
        },
        {
            "code": "300",
            "msg": "添加用户失败",
            "data": {
                "name": "Hello",
                "password": "37634867"
            }
        }
    ]
    return jsonify(random.choice(res))


if __name__ == '__main__':
    app.run("127.0.0.1", 9091)
