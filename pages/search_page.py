import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_class import Base
from utilities.logger import Logger


class AdvancedSearchPage(Base):

    """This page performs an advanced search and add products to favorites"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    location = "find-location-input-string"
    all_params = "div.all-params-show.goalButtons"
    carrying_capacity_min = "param-input-2072-min"
    carrying_capacity_max = "param-input-2072-max"
    construction = "param-select-2073-styler"
    crane = "param-select-2074-styler"
    construction_type = "//*[@id='param-select-2073-styler']/div[2]/ul/li[2]"
    crane_type = "//*[@id='param-select-2074-styler']/div[2]/ul/li[4]"
    price_min = "Price_begin"
    price_max = "Price_end"
    year_min = "Year_begin"
    year_max = "Year_end"
    button_with_only_price = "NoPrice"
    button_with_only_img = "haveimg"
    submit = "submit-button-input"
    button_add_to_fav = "l472047"
    button_fav = "//a[@title='Избранное']"

    """Getters
    These functions check the correctness of the locators"""

    def get_location(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.NAME, self.location)))

    def get_all_params(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.all_params)))

    def get_carrying_capacity_min(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.ID, self.carrying_capacity_min)))

    def get_carrying_capacity_max(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.ID, self.carrying_capacity_max)))

    def get_construction(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.ID, self.construction)))

    def get_crane(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.ID, self.crane)))

    def get_construction_type(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.construction_type)))

    def get_crane_type(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.crane_type)))

    def get_price_min(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.NAME, self.price_min)))

    def get_price_max(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.NAME, self.price_max)))

    def get_year_min(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.NAME, self.year_min)))

    def get_year_max(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.NAME, self.year_max)))

    def get_button_with_only_price(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.NAME, self.button_with_only_price)))

    def get_button_with_only_img(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.NAME, self.button_with_only_img)))

    def get_submit(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.ID, self.submit)))

    def get_button_add_to_fav(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.ID, self.button_add_to_fav)))

    def get_button_fav(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.button_fav)))

    """Action
    These functions perform actions with locators from the previous module"""

    def enter_location(self, location):
        self.get_location().send_keys(location)
        print('Enter location')

    def click_all_params(self):
        self.get_all_params().click()
        print('Click button all parameters')

    def select_min_carrying_capacity(self, ton_min):
        self.get_carrying_capacity_min().send_keys(ton_min)
        print('Select min carrying capacity')

    def select_max_carrying_capacity(self, ton_max):
        self.get_carrying_capacity_max().send_keys(ton_max)
        print('Select max carrying capacity')

    def select_construction_type(self):
        self.get_construction().click()
        self.get_construction_type().click()
        print('Select type construction')

    def select_crane_type(self):
        self.get_crane().click()
        self.get_crane_type().click()
        print('Select type crane')

    def select_min_price(self, price_min):
        self.get_price_min().send_keys(price_min)
        print('Select min price')

    def select_max_price(self, price_max):
        self.get_price_max().send_keys(price_max)
        print('Select max price')

    def select_min_year(self, year_min):
        self.get_year_min().send_keys(year_min)
        print('Select min year')

    def select_max_year(self, year_max):
        self.get_year_max().send_keys(year_max)
        print('Select max year')

    def click_button_with_only_price(self):
        self.get_button_with_only_price().click()
        print('Click checkbox only with price')

    def click_button_with_only_img(self):
        self.get_button_with_only_img().click()
        print('Click checkbox only with image')

    def click_submit(self):
        self.get_submit().click()
        print('Show results search')

    def click_button_add_to_fav(self):
        self.get_button_add_to_fav().click()
        print('Add item to favorite')

    def click_button_fav(self):
        self.get_button_fav().click()
        print('Go to favorite page')

    def advanced_search(self):
        with allure.step('Advanced search'):
            Logger.add_start_step(method='advanced search')
            self.enter_location('Россия')
            self.click_all_params()
            self.select_min_carrying_capacity('25')
            self.select_max_carrying_capacity('100')
            self.select_construction_type()
            self.select_crane_type()
            self.select_min_price('3000000')
            self.select_max_price('10000000')
            self.select_min_year('1985')
            self.select_max_year('2015')
            self.click_button_with_only_price()
            self.click_button_with_only_img()
            self.click_submit()
            self.scroll_page(self.get_button_add_to_fav())
            self.click_button_add_to_fav()
            self.click_button_fav()
            self.screenshot()
            self.screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='advanced search')

