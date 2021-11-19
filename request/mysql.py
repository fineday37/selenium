import pymysql

conn = pymysql.connect(
    host="192.168.108.128",
    user="root",
    password="123456",
    database="zhuxian",
    charset="utf8"
)
cur = conn.cursor()

cur.execute('select * from qingyun')
print(cur.fetchmany(2))
