import time
import datetime
import time

import pika
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from data_construct.mysql import Postgre
from data_construct.snowflake import IdWorker
from logs import Format
from concurrent.futures import ThreadPoolExecutor

logger = Format()


def GetList():
    driver = webdriver.Chrome()

    driver.get("https://work.taobao.com/")
    driver.find_element_by_xpath('//*[@id="ice-container"]/div/div[1]/div/a/button').click()
    time.sleep(1)
    handles = driver.window_handles
    driver.switch_to.window(handles[-1])
    driver.switch_to.frame('alibaba-login-box')
    time.sleep(3)
    driver.find_element_by_css_selector('[name="fm-login-id"]').send_keys("世纪开元旗舰店:李虎")
    driver.find_element_by_css_selector('[name="fm-login-password"]').send_keys("sjky36588")
    driver.find_element_by_css_selector('[type="submit"]').click()
    time.sleep(2)
    # driver.switch_to.frame('baxia-dialog-content')
    # slider = driver.find_element_by_css_selector("#nocaptcha #nc_1_n1z")
    #
    # print(slider.size["width"])
    # print(slider.size["height"])
    #
    # slider_areas = driver.find_elements_by_css_selector('.sm-pop-inner.nc-container')
    # slider_area = slider_areas[0]
    # # driver.switch_to.default_content()
    # time.sleep(1)
    # print(slider_area.size["width"])
    # print(slider_area.size["height"])
    # ActionChains(driver).click_and_hold(slider).perform()
    # time.sleep(1)
    # ActionChains(driver).move_to_element_with_offset(slider, slider_area.size["width"],
    #                                                  slider_area.size["height"]).perform()
    # time.sleep(3)
    cookies = driver.get_cookies()
    ls = webdriver.Chrome()
    print(cookies)

    ls.get("https://market.m.taobao.com/app/qn/im-history-search/index.html?spm=a21dfk.22864181.0.0.61cc74c8B4r8FE#/")
    ls.delete_all_cookies()
    for cookie in cookies:
        ls.add_cookie(
            {
                "domain": ".taobao.com",
                "name": cookie["name"],
                "value": cookie["value"],
                "path": "/",
                "expires": None
            }
        )
    ls.get("https://market.m.taobao.com/app/qn/im-history-search/index.html?spm=a21dfk.22864181.0.0.61cc74c8B4r8FE#/")
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    ls.find_element_by_css_selector('[placeholder="起始日期"]').click()
    ls.find_elements_by_css_selector('[placeholder="YYYY-MM-DD"]')[0].send_keys(Keys.CONTROL, "a")
    ls.find_elements_by_css_selector('[placeholder="YYYY-MM-DD"]')[0].send_keys(Keys.BACKSPACE)
    ls.find_elements_by_css_selector('[placeholder="YYYY-MM-DD"]')[0].send_keys(str(yesterday))
    ls.find_elements_by_css_selector('[placeholder="YYYY-MM-DD"]')[1].click()
    ls.find_elements_by_css_selector('[placeholder="YYYY-MM-DD"]')[1].send_keys(str(yesterday))
    ls.find_elements_by_css_selector('[placeholder="YYYY-MM-DD"]')[0].click()
    time.sleep(1)
    ls.find_element_by_xpath('/html/body/div[2]/div/div[3]/button/span').click()
    ls.find_element_by_css_selector('.next-btn.next-medium.next-btn-normal.button').click()
    time.sleep(2)
    element = ls.find_elements_by_css_selector(".results-list")
    print(len(element))
    users = []
    for i in range(len(element)):
        user = element[i].text
        users.append(user)
    time.sleep(2)
    ls.quit()
    driver.quit()
    return users


def BreakList(N, names):
    n = int(len(names) / N)
    l = len(names) % N
    if l == 0:
        name = [names[i:i + n] for i in range(0, len(names), n)]
    else:
        name = [names[i:i + n] for i in range(0, len(names), n)]
        for j in name[N]:
            name[N - 1].append(j)
        del name[N]
    return name


def getList():
    res = requests.get(url="http://10.1.20.74:8080/member/getYesterdayNotifyMemberList?shopName=益好旗舰店")
    return res.json()["data"]


def Pick(data):
    try:
        credentials = pika.PlainCredentials('admin', 'admin')
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='10.168.20.90', port=5672, virtual_host='/', credentials=credentials))
        channel = connection.channel()
        # channel.exchange_declare(exchange='kaiyuan-helper-exchange', durable=True, exchange_type='topic')
        channel.queue_declare(queue='kaiyuan-helper-queue-test')
        channel.basic_publish(exchange='', routing_key='kaiyuan-helper-queue', body=data)
        connection.close()
        print("发送")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # GetList()
    # lists = getList()
    # # l = BreakList(130, lists)[:2][0]
    # print(len(lists))
    # lists = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # ls = BreakList(4, lists)
    # print(ls)
    # testv = {"name": "ls"}
    # print(str(testv))
    # file = os.path.join(os.path.dirname(__file__), 'kaiyuan.log')
    # with open(file, 'r', encoding='utf-8') as read_file:
    #     for data in read_file.read().splitlines():
    #         Pick(data)
    threapool = ThreadPoolExecutor(10)
    for i in Postgre():
        data = {"buyerOpenUid": IdWorker(1, 2, 0).get_id(), "custCareWangwang": "益好旗舰店:999345324234",
                "memberWangwang": i[0],
                "sign": "7464F1BA645FB3F3EE3A52A387548388", "timeStamp": "2023-02-16 09:39:50"}
        threapool.submit(Pick, str(data).encode('utf-8'))
        print(data)
        # Pick(json.dumps(data, ensure_ascii=False))

    # logger.error("name")
