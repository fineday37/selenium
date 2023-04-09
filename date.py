import os
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
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
driver.switch_to.frame('baxia-dialog-content')
slider = driver.find_element_by_css_selector("#nocaptcha #nc_1_n1z")

print(slider.size["width"])
print(slider.size["height"])

slider_areas = driver.find_elements_by_css_selector('.sm-pop-inner.nc-container')
slider_area = slider_areas[0]
# driver.switch_to.default_content()
time.sleep(1)
print(slider_area.size["width"])
print(slider_area.size["height"])
ActionChains(driver).click_and_hold(slider).perform()
time.sleep(1)
ActionChains(driver).move_to_element_with_offset(slider, slider_area.size["width"],
                                                 slider_area.size["height"]).perform()
time.sleep(3)
cookies = driver.get_cookies()

chrome_options = webdriver.ChromeOptions()
prefs = {
    'download.default_directory': os.getenv('OS_LOG_PATH')
}
chrome_options.add_experimental_option('prefs', prefs)
caps = DesiredCapabilities.CHROME
caps['goog:loggingPrefs'] = {'performance': 'ALL'}
ls = webdriver.Chrome(desired_capabilities=caps, options=chrome_options)

time.sleep(3)
ls.get("https://market.m.taobao.com/app/qn/im-history-search/index.html?spm=a21dfk.22864181.0.0.61cc74c8B4r8FE#/")
time.sleep(4)
request_log = driver.get_log('performance')
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
time.sleep(3)
print(request_log)
