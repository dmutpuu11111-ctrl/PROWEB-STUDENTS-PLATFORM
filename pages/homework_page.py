from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class HomeworkPage:
    def __init__(self, driver):
        self.driver = driver

        self.home = (
            By.CSS_SELECTOR,
            "#app > div > div.layout > div > div > div > ul > li:nth-child(1)"
        )

        self.homework = (
            By.CSS_SELECTOR,
            "#tabbar > div > div > div.tab-header__wrapper > div:nth-child(2) > span"
        )

        self.lesson = (
            By.CSS_SELECTOR,
            "#app > div > div.home-content > div > div > div.lazyscroll.h100 > div > div.home-homeworkV2__content-months > div:nth-child(1) > div.home-homeworkV2__content-months-month-works.md3-list > a"
        )

        self.comments = (
            By.CSS_SELECTOR,
            "#tabbar > div > div > div.tab-header__wrapper > div:nth-child(3) > span"
        )

        self.input_comment = (
            By.CSS_SELECTOR,
            r"#\32 263 > div.homework-comments__bottom > div.homework-comments__bottom-input > div > div.list-tile__leading-box.grow > div > label > textarea"
        )

        self.send_button = (
            By.CSS_SELECTOR,
            r"#\32 263 > div.homework-comments__bottom > div.homework-comments__bottom-input > button"
        )

    def click_homework(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            EC.element_to_be_clickable(self.homework)
        ).click()

    def click_lesson(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            EC.element_to_be_clickable(self.lesson)
        ).click()

    def click_comments(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            EC.element_to_be_clickable(self.comments)
        ).click()

    def enter_input_comment(self, input_comment):
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            EC.presence_of_element_located(self.input_comment)
        ).send_keys(input_comment)

    def send_comment(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            EC.element_to_be_clickable(self.send_button)
        ).click()