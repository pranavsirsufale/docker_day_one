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
driver = None


@pytest.fixture(scope='class')
def init_chrome_driver(request):
    
    print("---------------------------setup-----------------------------------------------")
    service = Service('/home/pranav/Desktop/task_python/selenium/chromedriver-linux64/chromedriver')
    ch_driver = webdriver.Chrome(service=service)
    request.cls.driver = ch_driver
    # ch_driver = webdriver.Chrome(ChromeDriverManager().install())
    # request.cls.driver = ch_driver
    yield
    ch_driver.close()


@pytest.fixture(scope='class')
def init_ff_driver(request):
    ff_driver = webdriver.Firefox(GeckoDriverManager().install())
    yield
    ff_driver.close()


@pytest.mark.usefixtures("init_chrome_driver")
class Base_chrome_test:
    pass



# @pytest.mark.usefixtures("init_ff_driver")
# class Base_ff_test:
#     pass

class Test_google_chrome(Base_chrome_test):
    def test_google_title_chrome(self):
        self.driver.get('http://www.google.com')
        assert self.driver.title == 'Google'