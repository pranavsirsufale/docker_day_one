import pytest
from POM.test.test_base import BaseTest
from POM.pages.LoginPage import LoginPage
from POM.conf.conf_test import TestData
# from POM.test.test_login import init_driver  # 👈 add this if fixture is not auto-discovered

# @pytest.mark.usefixtures("init_driver")
class Test_Login(BaseTest):
    # def test_signup_link_visible(self):
    #     self.loginPage = LoginPage(self.driver)
    #     flag = self.loginPage.is_signup_link_exists()
    #     assert flag

    # def test_login_page_title(self):
    #     self.loginPage = LoginPage(self.driver)
    #     title = self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
    #     assert title == TestData.LOGIN_PAGE_TITLE

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME,TestData.PASSWORD)

        
        