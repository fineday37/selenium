from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import logging

logging.basicConfig(level=logging.INFO)


def skipVideo(driver: webdriver.Chrome, episode: int):

    """
    :param driver: 浏览器
    :param episode: 视频源
    :return:
    """

    driver.get(f"https://www.cbh1.cc/p/44741/40/{episode}")

    iframe = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="custom_player_box"]/iframe')))
    driver.switch_to.frame(iframe)

    button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="bofang"]'))
    )
    button.click()

    videoMax = driver.find_element_by_xpath('//*[@id="player"]/div[7]/div[1]/div[2]/div[3]/button[1]')
    videoMax.click()

    video = driver.find_element_by_xpath('//*[@id="lelevideo"]')
    driver.execute_script("arguments[0].currentTime = 190", video)

    # 跳过片尾紧接下一集
    while True:
        current_time = int(driver.execute_script('return arguments[0].currentTime;',
                                                 driver.find_element_by_xpath('//*[@id="lelevideo"]')))
        minutes = int(current_time // 60)
        seconds = int(current_time % 60)
        formatted_time = "{:02}:{:02}".format(minutes, seconds)
        if formatted_time == "45:00":
            return skipVideo(driver, episode + 1)


if __name__ == '__main__':
    currentDriver = webdriver.Chrome(ChromeDriverManager().install())
    skipVideo(currentDriver, 6095563)
