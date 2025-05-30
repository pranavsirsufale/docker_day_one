from selenium import webdriver
# from selenium.
from webdriver_manager.chrome import ChromeDriverManager
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service



service = Service('/home/pranav/Desktop/task_python/selenium/chromedriver-linux64/chromedriver')


driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
driver.get('https://www.orangehrm.com/en/30-day-free-trial')
print(driver.title)



username_url = driver.find_element(By.ID, 'Form_getForm_subdomain').send_keys("sirsufalePranav")
name = driver.find_element(By.ID,"Form_getForm_Name").send_keys('pratik sirsta')
email = driver.find_element(By.ID , "Form_getForm_Email")
contact = driver.find_element(By.ID,"Form_getForm_Contact")
# company = driver.find_element(By.LINK_TEXT,'Company')


# email.send_keys('somethin@somehing.com')
# contact.send_keys("+9498486484")

# company.click()
# career = driver.find_element(By.LINK_TEXT,'Careers')

# career.click()



# job = driver.find_element(By.LINK_TEXT,'Job Application - Technical Support Engineer (Night Shift - Roster)')
# job.click()


# job_form = driver.find_element(By.CLASS_NAME,'btn action-btn applyButtonLink')


# job_form.click()







# time.sleep(500000)





# driver.quite()





