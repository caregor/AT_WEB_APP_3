import logging
import time

from selenium.common import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://test-stand.gb.ru"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f'Cant find '
                                                                                                       f'element by '
                                                                                                       f'locator '
                                                                                                       f'{locator}')

    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        return element.value_of_css_property(property)

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def get_text_dialog_windows(self):
        try:
            alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present(), message='cant find alert :(')
            dialog_text = alert.text
            logging.info(f"Текст в диалоговом окне: {dialog_text}")
            alert.accept()
        except NoAlertPresentException:
            print("Диалоговое окно отсутствует на странице")
        return dialog_text