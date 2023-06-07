import datetime
import os
from selenium.webdriver import ActionChains


class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Current url {get_url}')

    """Method screenshot"""

    def screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:/Users/misha/PycharmProjects/stepik/screen/' + name_screenshot)
        print('Made screenshot')

    """Method scroll page"""

    def scroll_page(self, locator):
        action = ActionChains(self.driver)
        action.move_to_element(locator).perform()
        print(f"Scroll page")

    """Method upload image"""
    @staticmethod
    def upload_image(locator, file_name):
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, file_name)
        locator.send_keys(file_path)
        print("Upload image")


