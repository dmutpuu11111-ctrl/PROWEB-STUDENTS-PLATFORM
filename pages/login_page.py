

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class LoginPage:
    def __init__(self, driver):
         self.driver = driver
         self.lang_ru = (By.CSS_SELECTOR, "#app > div > div > div > div.log-in__container > div > div.log-in__newContent-right > div > div.log-in__newContent-right-block-bot-langs > div:nth-child(1)")
         self.input_login = (By.CSS_SELECTOR, ".log-in__newContent-right-block-center-input input")
         # "#app > div > div > div > div.log-in__container > div > div.log-in__newContent-right > div > div.log-in__newContent-right-block-wrap > form > div.log-in__newContent-right-block-center > div > label"
         self.btn_enter = (By.CSS_SELECTOR, "#app > div > div > div > div.log-in__container > div > div.log-in__newContent-right > div > div.log-in__newContent-right-block-wrap > form > div.log-in__newContent-right-block-bot > button")
         self.input_password = (By.CSS_SELECTOR, ".log-in__newContent-right-block-center-input input")
         ##app > div > div > div > div.log-in__container > div > div.log-in__newContent-right > div > div.log-in__newContent-right-block-wrap > form > div.log-in__newContent-right-block-center.log-in__newContent-right-block-center-checkpass > div.log-in__newContent-right-block-center-inp > label
         self.btn_login = (By.CSS_SELECTOR, "#app > div > div > div > div.log-in__container > div > div.log-in__newContent-right > div > div.log-in__newContent-right-block-wrap > form > div.log-in__newContent-right-block-bot > button")
         self.device_1 = (By.CSS_SELECTOR, "#dialog > div > div > div > div.material-dialog__window-body.material-dialog__window-body_modify > div > div:nth-child(2)")
         self.finish_1 = (By.CSS_SELECTOR, "#dialog > div > div > div > div.material-dialog__window-body.material-dialog__window-body_modify > div > div:nth-child(2) > div.drop-down-component__content > div.sessions__item-content > button")

    def change_lang_ru(self):
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.element_to_be_clickable(self.lang_ru)).click()

    def enter_input_login(self, input_login):
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_element_located(self.input_login)).send_keys(input_login)

    def click_btn_enter(self):
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.element_to_be_clickable(self.btn_enter)).click()

    def enter_input_password(self, input_password):
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_element_located(self.input_password)).send_keys(input_password)

    def click_btn_login(self):
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.element_to_be_clickable(self.btn_login)).click()

    def click_device_1(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.device_1)).click()

    def click_finish_1(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.finish_1)).click()