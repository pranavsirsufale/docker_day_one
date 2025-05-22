import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service('/home/pranav/Desktop/task_python/selenium/chromedriver-linux64/chromedriver')

driver = webdriver.Chrome(service=service)

# driver.implicitly_wait(5000000000000000000000000000000000000000000000000000000000)
driver.get('https://www.google.com')


# time.sleep(90000000)
print(driver.title)



driver.find_element(By.NAME,'q').send_keys('naveen automationlabs')
optionsList = driver.find_element(By.CSS_SELECTOR,'ul .erkvQe li span')

print(len(optionsList))

for ele in optionsList:
    print(ele.text)
    if ele.text == 'naveen automationlabs youtube':
        ele.click()
        break




# driver.quit()
