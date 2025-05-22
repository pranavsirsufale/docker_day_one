from selenium import webdriver
# from selenium.
from webdriver_manager.chrome import ChromeDriverManager
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service



service = Service('/home/pranav/Desktop/task_python/selenium/chromedriver-linux64/chromedriver')


driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)




driver.get('https://www.amezon.in')
print(driver.title)

linklist = driver.find_elements(By.TAG_NAME,'a')

for link in linklist:
    print(link.text)
    print(link.get_attribute('href'))


print(len(linklist))



### get images 

imagelist = driver.find_elements(By.TAG_NAME,'img')
for image in imagelist:
    print(image.get_attribute('src'))