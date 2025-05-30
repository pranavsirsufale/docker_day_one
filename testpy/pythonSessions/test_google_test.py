from selenium import webdriver
# from selenium.
# from webdriver_manager.chrome import ChromeDriverManager
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import Select
import pytest

# driver.get('https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/#google_vignette')
driver = None

def setup_module():

    service = Service('/home/pranav/Desktop/task_python/selenium/chromedriver-linux64/chromedriver')
    global driver
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get('http://www.google.com')


def teardown_module(module):
    driver.quit()


def test_google_title():
    assert driver.title == "Google"


def test_google_url():
    assert driver.current_url == 'https://www.google.com/?gws_rd=ssl'

# print(driver.title)




#py.test -s -v test_google_test.py --html=google_test_rep