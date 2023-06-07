import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from pages.base_class import Base
from utilities.logger import Logger


class LoginPage(Base):

    """This class contains locators and methods for testing authorization"""

    url = 'https://my.exkavator.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    mail = "email"
    password = "password"
    login_button = "buttonLogin"
    profile_button = "span.ml-1.mr-2.nav-user-name.hidden-sm"
    logout_button = "/html/body/div[1]/div[2]/div[1]/nav/ul[1]/li[2]/div/a"

    """Getters
    These functions check the correctness of the locators"""

    def get_mail(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.NAME, self.mail)))

    def get_password(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.NAME, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.ID, self.login_button)))

    def get_profile_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.profile_button)))

    def get_logout_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.logout_button)))

    """Action
    These functions perform actions with locators from the previous module"""

    @allure.step('Input mail')
    def input_mail(self, value_mail):
        self.get_mail().send_keys(value_mail)
        print('Input mail')

    @allure.step('Input password')
    def input_password(self, value_password):
        self.get_password().send_keys(value_password)
        print('Input password')

    @allure.step('Click login button')
    def click_login_button(self):
        self.get_login_button().click()
        print('Click login button')

    @allure.step('Click profile button')
    def click_profile_button(self):
        self.get_profile_button().click()
        print('Click profile button')

    @allure.step('logout account')
    def logout_acc(self):
        self.get_profile_button().click()
        self.get_logout_button().click()
        print('logout account')

    @allure.step('Clear email and password')
    def clear_input(self):
        self.get_mail().clear()
        self.get_password().clear()
        print('Clear email and password')

    def authorization(self):
        with allure.step('Authorization'):
            Logger.add_start_step(method='authorization')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.input_mail('kostukovmihail48@gmail.com')
            self.input_password('e!f3BWaBVPaYtjg')
            self.click_login_button()
            self.get_current_url()
            Logger.add_end_step(url=self.driver.current_url, method='authorization')
