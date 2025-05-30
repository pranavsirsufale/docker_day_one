from POM.pages.BasePage import BasePage
# from test.test_login import TestData
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    EMAIL = (By.ID ,"username")
    PASSWORD = (By.ID,'password')
    LOGIN_BUTTON = (By.ID,"loginbtn")
    SIGNUP_LINK = (By.LINK_TEXT,"Sign up")
    
    """Constructor of the page class"""
    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get('https://app.hubspot.com/login/legacy')


    """Page actions"""
    def get_login_page_title(self,title):
        return self.get_title(title)
    
    def is_signup_link_exists(self):
        return self.is_visible(self.SIGNUP_LINK)
    
    def do_login(self,username,password):
        self.do_send_keys(self.EMAIL,username)
        self.do_send_keys(self.PASSWORD,password)
        self.do_click(self.LOGIN_BUTTON)