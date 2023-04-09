import psycopg2
import time
from concurrent.futures import ThreadPoolExecutor


def Postgre():
    conn = psycopg2.connect(
        port=5432,
        host='10.168.20.16',
        user='postgres',
        password='postgres',
        database='swechat',
        # charset='utf8mb4'
    )
    cursor = conn.cursor()

    cursor.execute("select distinct remark from staff_member where remark = 'Ad 陈🛻'")
    return cursor.fetchall()


# threapool = ThreadPoolExecutor(10)
if __name__ == '__main__':
    # for i in Postgre():
    #     print(i[0])
    data = {"buyerOpenUid": "123", "custCareWangwang": "益好旗舰店:999345324234",
            "memberWangwang": Postgre()[0][0],
            "sign": "7464F1BA645FB3F3EE3A52A387548388", "timeStamp": "2023-02-16 09:39:50"}
    print(Postgre()[0][0])
    print(data)
