from selenium import webdriver
import allure

from pages.base_class import Base
from pages.favorite_page import FavoritePage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.search_page import AdvancedSearchPage


class Test_all_pages:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=chrome_options)

    login = LoginPage(driver)
    profile = ProfilePage(driver)
    main = MainPage(driver)
    search = AdvancedSearchPage(driver)
    fav = FavoritePage(driver)
    base = Base(driver)

    @allure.title('Smoke')
    @allure.description('This is test of complete business path')
    def test_smoke(self):
        self.login.authorization()
        self.base.screenshot()
        self.profile.editing_profile()
        self.base.screenshot()
        self.main.select_params()
        self.base.screenshot()
        self.search.advanced_search()
        self.base.screenshot()
        self.fav.get_fav_item_info()
        self.base.screenshot()
