from selenium import webdriver
import allure

from pages.base_class import Base
from pages.login_page import LoginPage
from pages.main_page import MainPage


class Test_select_categories():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=chrome_options)

    login = LoginPage(driver)
    main = MainPage(driver)
    base = Base(driver)

    @allure.title('Select categories')
    @allure.description('This is test of select categories')
    def test_select_categories(self):
        self.login.authorization()
        self.main.select_params()
        self.base.screenshot()
