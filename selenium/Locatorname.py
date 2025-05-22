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
driver.get('https://ui.cogmento.com/')
print(driver.title)


# username = driver.find_element(By.NAME , 'txtUserName')
# password = driver.find_element(By.NAME , 'txtPassword')
username = driver.find_element(By.NAME,'Email')
password = driver.find_element(By.NAME,"Password")

# login = driver.find_element(By.XPATH,"//input[@value='Sign In']")
# login = driver.find_element(By.LINK_TEXT,"Login")

# username.send_keys("D21AC0239484")
# password.send_keys("Pooja@123")
# login.click()

username.send_keys('pradiprane85@gmail.com')
password.send_keys('Pass@123')
login = driver.find_element(By.XPATH,"//input[@value='Login']")

# time.sleep(500000)





