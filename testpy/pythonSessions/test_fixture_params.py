from selenium import webdriver
# from selenium.
from webdriver_manager.chrome import ChromeDriverManager
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.support.ui import Select
import pytest

# driver.get('https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/#google_vignette')
# driver = None


# @pytest.fixture(scope='class')
# def init_chrome_driver(request):
    
#     print("---------------------------setup-----------------------------------------------")
#     service = Service('/home/pranav/Desktop/task_python/selenium/chromedriver-linux64/chromedriver')
#     ch_driver = webdriver.Chrome(service=service)
#     request.cls.driver = ch_driver
#     # ch_driver = webdriver.Chrome(ChromeDriverManager().install())
#     # request.cls.driver = ch_driver
#     yield
#     ch_driver.close()


@pytest.fixture(params=['Chrome','firefox'],scope='class')
def init__driver(request):
    print("---------------------------setup-----------------------------------------------")
    if request.param == 'Chrome':
        service = Service('/home/pranav/Desktop/task_python/selenium/chromedriver-linux64/chromedriver')
        web_driver = webdriver.Chrome(service=service)
        # request.cls.driver = ch_driver

    # if request.param == 'firefox':
    #     assert request.param == 'firefox'
    request.cls.driver = web_driver

    yield
    web_driver.close()


@pytest.mark.usefixtures(init__driver)
class BaseTest:
    pass 


class Test_Google(BaseTest):
    def test_google_title(self):
        self.driver.get('http://www.google.com')
        assert self.driver.title == "Google"