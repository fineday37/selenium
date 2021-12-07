import json

import pymysql

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
    return cur.fetchone()


if __name__ == '__main__':
    data = datas()
    print(data)
