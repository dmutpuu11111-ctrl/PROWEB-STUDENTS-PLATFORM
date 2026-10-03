

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.profile_icon = (By.CSS_SELECTOR, ".header__avatar")
        self.logout_btn = (By.CSS_SELECTOR, "#app > div > div.user-container > div > div > div.relative.w100p > div.flex.column.gap15.w100p.relative > div:nth-child(6)")
        self.exit_confirm = (By.XPATH, "//div[@id='dialog']//div[contains(@class, 'material-dialog__window-actions')]//button[normalize-space()='Выйти']")

    def click_profile_icon(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.profile_icon)).click()

    def click_logout_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.logout_btn)).click()

    def click_exit_confirm(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.exit_confirm)).click()




