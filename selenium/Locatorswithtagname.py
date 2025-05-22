from selenium import webdriver
# from selenium.
from webdriver_manager.chrome import ChromeDriverManager
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service



service = Service('/home/pranav/Desktop/task_python/selenium/chromedriver-linux64/chromedriver')


driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
# driver.get('https://bamuaapp.digitaluniversity.ac/StudentLogin.aspx')
driver.get('https://www.freshworks.com/')
print(driver.title)


header_element = driver.find_element(By.TAG_NAME,'h1')
header_elem = driver.find_element(By.TAG_NAME,'h2')
header_thre = driver.find_elements(By.TAG_NAME,'h3')
print(header_element.text)
print(header_elem.text)
for i in header_thre:
    print(i.text)
# print(header_thre.text)





##?? CApture total link
#?? tag name : total no of links 

#########################


driver.get('https://www.amezon.in')
print(driver.title)

linklist = driver.find_elements(By.TAG_NAME,'a')

print(len(linklist))

