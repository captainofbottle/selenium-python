import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_class import Base
from utilities.logger import Logger


class ProfilePage(Base):

    """On this page, information about the company and its type of activity is filled in."""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    profile_company = "//li[@data-point='company']"
    company_name = "companyName"
    company_intro = "companyIntro"
    company_logo = "input#addNewPhotoFile"
    company_street = "companyStreet"
    company_house = "companyHouse"
    company_office = "companyOffice"
    work_time = "//label[@for='customSwitchSuccess247']"
    specialization = "//label[@for='serviceCheck263']"
    service = "//label[@for='serviceCheck341']"
    service_description = "//*[@id='serviceDescription341']/div[2]/textarea"
    save_button = "profileSubmit"

    """Getters
    These functions check the correctness of the locators"""

    def get_profile_company(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.profile_company)))

    def get_company_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.company_name)))

    def get_company_intro(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.company_intro)))

    def get_company_logo(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.company_logo)))

    def get_company_street(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.company_street)))

    def get_company_house(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.company_house)))

    def get_company_office(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.company_office)))

    def get_work_time(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.work_time)))

    def get_specialization(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.specialization)))

    def get_service(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.service)))

    def get_service_description(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.service_description)))

    def get_save_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.save_button)))

    """Action
    These functions perform actions with locators from the previous module"""

    @allure.step('Go to editing profile')
    def click_profile_company(self):
        self.get_profile_company().click()
        print("Go to editing profile")

    @allure.step('Input company name')
    def input_company_name(self, name):
        self.get_company_name().send_keys(name)
        print("Input company name")

    @allure.step('Input company intro')
    def input_company_intro(self, intro):
        self.get_company_intro().send_keys(intro)
        print("Input company intro")

    @allure.step('Input company street')
    def input_company_street(self, street):
        self.get_company_street().send_keys(street)
        print("Input company street")

    @allure.step('Input company house')
    def input_company_house(self, house):
        self.get_company_house().send_keys(house)
        print("Input company house")

    @allure.step('Input company office')
    def input_company_office(self, office):
        self.get_company_office().send_keys(office)
        print("Input company office")

    @allure.step('Select work time')
    def select_work_time(self):
        self.get_work_time().click()
        print("Select work time")

    @allure.step('Select specialization')
    def select_specialization(self):
        self.get_specialization().click()
        print("Select specialization")

    @allure.step('Select service')
    def select_service(self):
        self.get_service().click()
        print("Select service")

    @allure.step('Input service description')
    def input_service_description(self, description):
        self.get_service_description().send_keys(description)
        print("Input service description")

    @allure.step('Click save button')
    def click_save_button(self):
        self.get_save_button().click()
        print("Click save button")

    def editing_profile(self):
        with allure.step('Editing profile'):
            Logger.add_start_step(method='editing profile')
            self.click_profile_company()
            self.input_company_name("ООО 'Над головой'")
            self.input_company_intro("Безопасность прежде всего")
            self.upload_image(self.get_company_logo(), 'logo.png')
            self.input_company_street("Пушкина")
            self.input_company_house("Колотушкина")
            self.input_company_office("7Б")
            self.select_work_time()
            self.scroll_page(self.get_specialization())
            self.select_specialization()
            self.scroll_page(self.get_service())
            self.select_service()
            self.input_service_description("Покупка мостовых кранов и комплектующих")
            # self.click_save_button()
            self.get_current_url()
            Logger.add_end_step(url=self.driver.current_url, method='editing profile')
