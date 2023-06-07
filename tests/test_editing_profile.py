from selenium import webdriver
import allure
from pages.login_page import LoginPage
from pages.base_class import Base
from pages.profile_page import ProfilePage


class Test_editing_profile():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=chrome_options)

    login = LoginPage(driver)
    base = Base(driver)
    profile = ProfilePage(driver)

    @allure.title('Editing profile')
    @allure.description('This is test of editing profile')
    def test_editing_profile(self):
        self.login.authorization()
        self.profile.editing_profile()
        self.base.screenshot()
