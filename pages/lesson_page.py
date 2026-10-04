import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class LessonPage:
    def __init__(self, driver):
        self.driver = driver

        self.home = (
            By.CSS_SELECTOR,
            "#app > div > div.layout > div > div > div > ul > li:nth-child(1)"
        )

        self.my_groups = (
            By.CSS_SELECTOR,
            "#app > div > div.home-content > div > div > div.container.container_mobile > div > div.home-eduV2__groups > div.home-eduV2__groups-cards > div > div.home-eduV2__groups-cards-card-bot > div.flex.jcsb.aic.gap15 > div.go-btn > svg"
        )

        self.lessons = (
            By.CSS_SELECTOR,
            "#tabbar > div > div.tab-header > div.tab-header__wrapper > div:nth-child(2) > span"
        )

        self.lesson_video = (
            By.CSS_SELECTOR,
            "#app > div > div.container.container_mobile.subscription-top-padding > div > div > div.new-lessons_content > div > div:nth-child(5) > div.flex.gap20 > div:nth-child(7) > div.lesson-card > div > div > div.lesson-card-left_actions > button"
        )

        self.play_button = (
            By.CSS_SELECTOR,
            "#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(2) > div.hidden > div > div.video-player-proweb__wrapper > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-left > button"
        )

        self.fullscreen_button = (
            By.CSS_SELECTOR,
            "#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(2) > div.hidden > div > div.video-player-proweb__wrapper > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-right > button:nth-child(3)"
        )

        self.video = (
            By.CSS_SELECTOR,
            "#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(2) > div.hidden > div > div.video-player-proweb__wrapper > video"
        )

        self.rating_5 = (
            By.CSS_SELECTOR,
            "#app > div > div.videolesson > div > div:nth-child(2) > div > div.videolesson__general-footer-rating.mt10 > div > div > div > div > span:nth-child(5)"
        )

    def click_home(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            EC.element_to_be_clickable(self.home)
        ).click()


    def click_my_groups(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            EC.element_to_be_clickable(self.my_groups)
        ).click()

    def click_lessons(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            EC.element_to_be_clickable(self.lessons)
        ).click()

    def click_lesson_video(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            EC.element_to_be_clickable(self.lesson_video)
        ).click()

    def click_play(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            EC.element_to_be_clickable(self.play_button)
        ).click()

    def click_fullscreen(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            EC.element_to_be_clickable(self.fullscreen_button)
        ).click()

    def watch_video_100_seconds(self):
        end_time = time.time() + 5

        while time.time() < end_time:
            video = self.driver.find_element(*self.video)

            is_paused = self.driver.execute_script(
                "return arguments[0].paused;",
                video)

            if is_paused:
                self.driver.execute_script(
                    "arguments[0].play();",
                    video)

            time.sleep(1)

    def click_exit_fullscreen(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            EC.element_to_be_clickable(self.fullscreen_button)
        ).click()

    def rate_lesson(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(
                EC.element_to_be_clickable(self.rating_5)
            ).click()
        except (TimeoutException, NoSuchElementException):
            pass