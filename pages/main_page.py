import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_class import Base
from utilities.logger import Logger


class MainPage(Base):

    """This page selects categories for further search."""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    main_button = "div.brand"
    list_machine_type = "/html/body/div[4]/div/div/div[3]/div[6]/div[2]/div[2]/div/div[1]/div/form/div[1]/div[2]/div/div"
    machine_type = "//li[@title='Краны мостовые']"
    button_used_equipment = "//label[@for='form-index-used-used']"
    submit = "input.inp-submit"

    """Getters
    These functions check the correctness of the locators"""

    def get_main_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.main_button)))

    def get_list_machine_type(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.list_machine_type)))

    def get_machine_type(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.machine_type)))

    def get_button_used_equipment(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.button_used_equipment)))

    def get_submit(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.submit)))

    """Action
    These functions perform actions with locators from the previous module"""

    def switch_to_main_menu(self):
        self.get_main_button().click()
        time.sleep(5)
        print('Click main button')

    def open_list_machine_type(self):
        self.get_list_machine_type().click()
        print('Click dropdown list of machine types')

    def select_machine_type(self):
        self.get_machine_type().click()
        print('Select machine type')

    def click_used_equipment(self):
        self.get_button_used_equipment().click()
        print('Click button used equipment for machine')

    def click_submit(self):
        self.get_submit().click()
        print('Click pick up button')

    def select_params(self):
        with allure.step('Search'):
            Logger.add_start_step(method='search')
            self.switch_to_main_menu()
            self.open_list_machine_type()
            self.select_machine_type()
            self.click_used_equipment()
            self.click_submit()
            self.get_current_url()
            self.screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='search')