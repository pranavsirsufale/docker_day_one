from selenium import webdriver
# from selenium.
# from webdriver_manager.chrome import ChromeDriverManager
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pytest

from selenium.webdriver.support.ui import Select


def test_google():
    service = Service('/home/pranav/Desktop/task_python/selenium/chromedriver-linux64/chromedriver')

    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)

    driver.get('https://www.google.com')
    assert driver.title == 'Google'
    driver.quit()

def test_facebook():
    service = Service('/home/pranav/Desktop/task_python/selenium/chromedriver-linux64/chromedriver')

    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)

    driver.get('https://www.facebook.com')
    assert driver.title == 'Facebook – log in or sign up'
    driver.quit()

def test_gmail():
    service = Service('/home/pranav/Desktop/task_python/selenium/chromedriver-linux64/chromedriver')

    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)

    driver.get('https://www.gmail.com')
    assert driver.title == 'Gmail'
    driver.quit()









