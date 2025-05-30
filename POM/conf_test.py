import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from POM.conf.config import TestData  # Adjust import if needed
print('conftest loaded')

@pytest.fixture(params=["chrome"], scope="class")
def init_driver(request):
    print("conftest loaded.")
    if request.param == "chrome":
        service = Service(TestData.CHROME_EXECUTABLE_PATH)
        driver = webdriver.Chrome(service=service)
    elif request.param == "firefox":
        service = Service(TestData.FIREFOX_EXECUTABLE_PATH)
        driver = webdriver.Firefox(service=service)

    request.cls.driver = driver
    yield
    driver.quit()
