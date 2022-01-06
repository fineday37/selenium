import json

import pymysql
import pprint
conn = pymysql.connect(
    host="10.168.20.47",
    user="root",
    password="mysql",
    database="dayu-dwd",
    charset="utf8"
)
cur = conn.cursor()


def datas():
    cur.execute('select * from dwd_ord_di_after_sales_d')
    return cur.fetchone()[3]


if __name__ == '__main__':
    data = datas()
    pprint.pprint(data)
