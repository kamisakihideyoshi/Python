# coding=utf-8
from os.path import dirname

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 設定開啟的瀏覽器類型:
driver = webdriver.Chrome(
    executable_path=dirname(__file__) + '/chromedriver')

# 開啟 Google 首頁:
driver.get('https://www.google.com.tw/')

# 找到搜尋框並輸入關鍵字:
foo = driver.find_element_by_class_name('gsfi')
foo.send_keys('Cat is liquid')
foo.send_keys(Keys.ENTER)