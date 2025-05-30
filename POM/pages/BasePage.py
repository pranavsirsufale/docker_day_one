# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select , WebDriverWait
# import pytest
# from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC

# driver.get('https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/#google_vignette')
# driver = None


"""This class is the parent of all pages"""
"""it contains all the generic methods and utilities for all pages"""


class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def do_click(self,by_locator):
        WebDriverWait(self.driver,10 ).until(EC.visibility_of_element_located(by_locator)).click()


    def do_send_keys(self,by_locator,text):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)


    def get_element_text(self,by_locator):
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        return element.text
    
    def is_visible(self,by_locator):
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)
    
    def get_title(self,title):
        WebDriverWait(self.driver,10).until(EC.title_is(title))
        return self.driver.title
    

    

