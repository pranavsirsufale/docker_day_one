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


@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("---------------------------setup-----------------------------------------------")
    service = Service('/home/pranav/Desktop/task_python/selenium/chromedriver-linux64/chromedriver')
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get('http://www.google.com')

    yield
    print("------------------------tear down ---------------------------------")
    driver.quit()


# def teardown_module(module):
#     driver.quit()


def test_google_title(init_driver):
    assert driver.title == "Google"


def test_google_url(init_driver):
    assert driver.current_url == 'https://www.google.com/'
