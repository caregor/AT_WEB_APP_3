import logging

from selenium.webdriver.common.by import By

from src.BaseApp import BasePage


class TestSearchLocators:
    LOCATOR_CONTACT_US_BTN = (By.CSS_SELECTOR, 'button')
    LOCATOR_CONTENT_FIELD = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_EMAIL_FIELD = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_NAME_FIELD = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, 'button')
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_CONTACT_LINK = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")


class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f'Send {word} to element')
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f'Send {word} to element')
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        logging.info('Click login button')
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=2)
        text = error_field.text
        logging.info(f'We find text: {text}')
        return text

    def click_contact_link(self):
        logging.info('Click contact link')
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_LINK).click()

    def enter_name(self, name):
        logging.info(f'Send {name} to element')
        login_field = self.find_element(TestSearchLocators.LOCATOR_NAME_FIELD)
        login_field.clear()
        login_field.send_keys(name)

    def enter_email(self, email):
        logging.info(f'Send {email} to element')
        login_field = self.find_element(TestSearchLocators.LOCATOR_EMAIL_FIELD)
        login_field.clear()
        login_field.send_keys(email)
    
    def enter_content(self, content):
        logging.info(f'Send {content} to element')
        login_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT_FIELD)
        login_field.clear()
        login_field.send_keys(content)
        
    def click_contact_us_button(self):
        logging.info('Click contact Us button')
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BTN).click()

