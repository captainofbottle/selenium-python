from selenium import webdriver
import allure

from pages.base_class import Base
from pages.login_page import LoginPage


class Test_authorization:
    driver = webdriver.Chrome()
    login = LoginPage(driver)
    base = Base(driver)

    @allure.title('Authorization with valid data')
    @allure.description('This is test of login with valid data')
    def test_auth_valid_data(self):
        self.login.authorization()
        self.base.screenshot()
        self.login.logout_acc()

    @allure.title('Authorization with invalid data')
    @allure.description('This is test of login with invalid email')
    def test_auth_invalid_email(self):
        self.login.input_mail('123')
        self.login.input_password('e!f3BWaBVPaYtjg')
        self.login.click_login_button()
        self.base.screenshot()
        self.login.clear_input()


    @allure.title('Authorization with invalid data')
    @allure.description('This is test of login with invalid password')
    def test_auth_invalid_password(self):
        self.login.input_mail('kostukovmihail48@gmail.com')
        self.login.input_password('aezakmi')
        self.login.click_login_button()
        self.base.screenshot()
        self.login.clear_input()

    @allure.title('Authorization with empty data')
    @allure.description('This is test of login with empty email')
    def test_auth_empty_email(self):
        self.login.input_mail('')
        self.login.input_password('aezakmi')
        self.login.click_login_button()
        self.base.screenshot()
        self.login.clear_input()

    @allure.title('Authorization with empty data')
    @allure.description('This is test of login with empty password')
    def test_auth_empty_password(self):
        self.login.input_mail('kostukovmihail48@gmail.com')
        self.login.input_password('')
        self.login.click_login_button()
        self.base.screenshot()
        self.login.clear_input()


    @allure.title('Authorization with empty data')
    @allure.description('This is test of login with empty email and password')
    def test_auth_empty_data(self):
        self.login.input_mail('')
        self.login.input_password('')
        self.login.click_login_button()
        self.base.screenshot()
        self.login.clear_input()

