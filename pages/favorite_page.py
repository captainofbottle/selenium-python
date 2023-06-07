import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_class import Base
from utilities.logger import Logger


class FavoritePage(Base):

    """This page reads information about the added product"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    item = "a.link"
    price = "//b[@class='price-value']"
    year = "//div[@class='line-val']"
    seller = "mp-img-contacts-user"
    description = "/html/body/div[4]/div/div/div/div[9]/div[2]/div[2]/div[4]/div[4]/div/div/div[2]"
    button_remove_fav = "l472047"

    """Getters
    These functions check the correctness of the locators"""

    def get_item(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.item)))

    def get_price(self):
        return WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.price)))

    def get_year(self):
        return WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.year)))

    def get_seller(self):
        return WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, self.seller)))

    def get_description(self):
        return WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.description)))

    def get_button_remove_fav(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, self.button_remove_fav)))

    """Action
    These functions perform actions with locators from the previous module"""

    def click_item(self):
        self.get_item().click()
        print('Click on item')

    def print_price(self):
        text_price = self.get_price().text
        print(f'Price : {text_price}')

    def print_year(self):
        text_year = self.get_year().text
        print(f'Year : {text_year}')

    def print_seller(self):
        text_seller = self.get_seller().text
        print(f'Seller : {text_seller}')

    def print_description(self):
        text_desc = self.get_description().text
        print(text_desc[0:24])

    def remove_fav(self):
        self.get_button_remove_fav().click()
        print('Remove item from favorite')

    def get_fav_item_info(self):
        with allure.step('Get favorite item information'):
            Logger.add_start_step(method='get item info')
            self.driver.get('https://exkavator.ru/trade/favourites')
            self.click_item()
            self.print_price()
            self.print_year()
            self.print_seller()
            self.print_description()
            self.get_current_url()
            self.screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='get item info')
