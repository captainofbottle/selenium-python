from selenium import webdriver
import allure

from pages.base_class import Base
from pages.favorite_page import FavoritePage
from pages.login_page import LoginPage
from pages.main_page import MainPage


class Test_favorites():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=chrome_options)

    login = LoginPage(driver)
    main = MainPage(driver)
    fav = FavoritePage(driver)
    base = Base(driver)

    @allure.title('Getting information about a selected product')
    @allure.description('This is test of getting information about a selected product')
    def test_fav(self):
        self.login.authorization()
        self.main.select_params()
        self.fav.get_fav_item_info()
        self.base.screenshot()
