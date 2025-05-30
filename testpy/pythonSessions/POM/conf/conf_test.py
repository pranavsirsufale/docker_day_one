import pytest 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from POM.conf.config import TestData

@pytest.fixture(params=['chrome'],scope='class')
def init_driver(request):
    print('something')
    if request.param == 'chrome':
        
        # service = Service('/home/pranav/Desktop/task_python/selenium/chromedriver-linux64/chromedriver')
        service = Service(TestData.CHROME_EXECUTABLE_PATH)
        web_driver = webdriver.Chrome(service=service)
        
    
    if request.param == 'firefox':
        # service = Service('/home/pranav/Desktop/task_python/driver/geckodriver')
        service = Service(TestData.FIREFOX_EXECUTABLE_PATH)
        web_driver = webdriver.Firefox(service=service)
        
    
    request.cls.driver = web_driver
    # web_driver.implicitly_wait(10)
    yield
    web_driver.close()



