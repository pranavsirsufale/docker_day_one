from POM.pages.BasePage import BasePage
# from test.test_login import TestData
from selenium.webdriver.common.by import By
import time

class LoginPage(BasePage):
    EMAIL = (By.ID ,"username")
    PASSWORD = (By.ID,'password')
    LOGIN_BUTTON = (By.ID,"kc-login")
    SIGNUP_LINK = (By.LINK_TEXT,"Sign up")
    SATELLITE_TAB = (By.ID,'satellites_label')
    # SATELLITE_TAB = (By.ID,'left-tabs-example-tab-Satellites')
    # SATELLITE_TAB = (By.ID,'left-tabs-example-tab-Satellites')
    SATELLITE_CARD = (By.ID,'maha_weather_obser')
    SEQUENCED_CLASS = (By.CLASS_NAME,'common-card-footer')
    SEQUENCE_PARENT_DIV = (By.CLASS_NAME,"profile_contents")
    SEQUENCE_CHILD_DIV = (By.CLASS_NAME,"common-card-footer")
    
    """Constructor of the page class"""
    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get("https://id-testing1.antaris-staging.cloud/realms/ATMOS/protocol/openid-connect/auth?client_id=ATMOS-UI-CLIENT&redirect_uri=https%3A%2F%2Fapp-testing1.antaris-staging.cloud%2Fvishal%2520testing2%2F49c5147c-66b4-4b32-8e49-c5c76be39976%2Fstation_provider%2FISP%2520Jalna%2F2fb7005d-9d45-4de2-9826-1152df92a56d%2FStation&state=17488c5c-18cf-4d53-b11b-ce0a30c3a642&response_mode=fragment&response_type=code&scope=openid&nonce=6faf6e26-7e47-4f4a-81fc-b28613d22472&code_challenge=TTnQrxoBmrdLddPDv6KVi9f7Zwe9PHIeghMz2hu2tQk&code_challenge_method=S256")


    """Page actions"""
    def get_login_page_title(self,title):
        return self.get_title(title)
    
    def is_signup_link_exists(self):
        return self.is_visible(self.SIGNUP_LINK)
    

    def do_login(self,username,password):
        self.do_send_keys(self.EMAIL,username)
        self.do_send_keys(self.PASSWORD,password)
        self.do_click(self.LOGIN_BUTTON)
        self.do_click(self.SATELLITE_TAB)
        self.do_click(self.SATELLITE_CARD)
        self.do_multiple_click(self.SEQUENCE_PARENT_DIV, self.SEQUENCE_CHILD_DIV)


        time.sleep(50000)