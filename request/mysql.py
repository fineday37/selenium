import pprint

import pymysql
import psycopg2

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


psyconn = psycopg2.connect(
    database='20200212store',
    user='postgres',
    password='postgres',
    host='10.168.20.16',
    port='5432'
)
curs = psyconn.cursor()
curs.execute(
    "select c.code, d.add_way_code from mbr_member_decrypt c left join mbr_member d on c.member_code = d.member_code where c.mobile = '17852170964';")
row = curs.fetchall()
print(row)

psyconn.close()
if __name__ == '__main__':
    data = datas()
    pprint.pprint(data)
