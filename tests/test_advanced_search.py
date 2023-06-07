from selenium import webdriver
import allure

from pages.base_class import Base
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.search_page import AdvancedSearchPage


class Test_advanced_search():
    driver = webdriver.Chrome()

    login = LoginPage(driver)
    main = MainPage(driver)
    advanced = AdvancedSearchPage(driver)
    base = Base(driver)

    @allure.title('Advanced Search')
    @allure.description('This is test of advanced search for the specified categories')
    def test_advances_search(self):
        self.login.authorization()
        self.main.select_params()
        self.advanced.advanced_search()
        self.base.screenshot()
