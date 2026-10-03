from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class CoworkingPage:
    def __init__(self, driver):
        self.driver = driver

        # Коворкинг
        self.coworking = (
            By.CSS_SELECTOR,
            "#app > div > div.home-content > div > div > div.container.container_mobile > "
            "div > div.home-eduV2__reminders > div.home-eduV2__reminders-block > "
            "div:nth-child(1) > div.flex.aic.jcsb.mb10 > div > svg"
        )

        # Кнопка "Записаться"
        self.book_button = (
            By.CSS_SELECTOR,
            "#app > div > div.coworking > div > button"
        )

        # Checkbox "Я ознакомился с правилами"
        self.rules_checkbox = (
            By.CSS_SELECTOR,
            "#dialog > div > div > div.material-dialog__window-container > "
            "div.material-dialog__window-body > "
            "div.coworking__page-dialog-rules-check > label > button"
        )

        # Кнопка "Далее"
        self.next_button = (
            By.CSS_SELECTOR,
            "#dialog > div > div > div.material-dialog__window-actions > "
            "button:nth-child(2)"
        )

        # Филиал "Ойбек 1"
        self.oybek = (
            By.XPATH,
            "//div[contains(@class, "
            "'coworking__page-dialog-follow-branch-item-list')]"
            "[.//*[contains(normalize-space(), 'Ойбек 1')]]"
        )

        # Кнопка "Выбрать филиал"
        self.select_branch_button = (
            By.CSS_SELECTOR,
            "#dialog > div.material-dialog.coworking__branch-dialog > div > "
            "div.material-dialog__window-actions > button:nth-child(2)"
        )

        # Дата
        self.date = (
            By.CSS_SELECTOR,
            "#dialog > div > div > div.material-dialog__window-container > "
            "div.material-dialog__window-body > div.stepper-body > div > div > div > "
            "div.coworking__page-dialog-follow-date > div > div:nth-child(5) > button"
        )

        # Выбор группы
        # Кликаем по реальному текстовому элементу,
        # а не по родительскому div
        self.group = (
            By.CSS_SELECTOR,
            "#dialog > div > div > div.material-dialog__window-container > "
            "div.material-dialog__window-body > div.stepper-body > div > div > div > "
            "div.list-tile.coworking__page-dialog-follow-list"
        )


        # Радиокнопка группы
        self.group_circle = (
            By.CSS_SELECTOR,
            "#dialog > div:nth-child(2) > div > "
            "div.material-dialog__window-container > "
            "div.material-dialog__window-body > div > div > div > "
            "div.list-tile__trailing > button"
        )

        # Кнопка "Выбрать группу"
        self.select_group_button = (
            By.CSS_SELECTOR,
            "#dialog > div:nth-child(2) > div > "
            "div.material-dialog__window-actions > button:nth-child(2)"
        )

        # Поле выбора времени
        self.time = (
            By.CSS_SELECTOR,
            "#dialog > div > div > div.material-dialog__window-container > "
            "div.material-dialog__window-body > div.stepper-body > div > div > div > "
            "div.coworking__page-dialog-follow-timeseat > div:nth-child(1) > "
            "label > span.material-input__icon"
        )

        # Поле/ячейка времени
        self.time_cell = (
            By.CSS_SELECTOR,
            "#dialog > div.material-dialog.timepicker > div > "
            "div.material-dialog__window-container > "
            "div.material-dialog__window-body > div > label:nth-child(1)"
        )

        # Кнопка "Выбрать время"
        self.select_time_button = (
            By.CSS_SELECTOR,
            "#dialog > div.material-dialog.timepicker > div > "
            "div.material-dialog__window-actions > button:nth-child(2)"
        )

        # Поле "Выбрать место"
        self.place = (
            By.CSS_SELECTOR,
            "#dialog > div > div > "
            "div.material-dialog__window-container > "
            "div.material-dialog__window-body > div.stepper-body > "
            "div > div > div > "
            "div.coworking__page-dialog-follow-timeseat > div:nth-child(2) > div"
        )

        # Конкретное место в списке
        self.place_cell = (
            By.CSS_SELECTOR,
            "#dialog > div:nth-child(2) > div > "
            "div.material-dialog__window-container > "
            "div.material-dialog__window-body > div.md3-list > "
            "div:nth-child(1) > div.list-tile__trailing > button"
        )

        # Кнопка "Подтвердить" после выбора места
        self.confirm_place_button = (
            By.CSS_SELECTOR,
            "#dialog > div:nth-child(2) > div > div.material-dialog__window-actions > button:nth-child(2)"
        )

        # Финальная кнопка "Записаться"
        self.final_book_button = (
             By.CSS_SELECTOR,
            "#dialog > div > div > div.material-dialog__window-actions > button:nth-child(2)"
        )


    # ---------------------------------------------------------
    # Коворкинг
    # ---------------------------------------------------------

    def click_coworking(self):
        wait = WebDriverWait(self.driver, 10)

        wait.until(
            EC.element_to_be_clickable(self.coworking)
        ).click()

    # ---------------------------------------------------------
    # Начало записи
    # ---------------------------------------------------------

    def click_book(self):
        wait = WebDriverWait(self.driver, 10)

        wait.until(
            EC.element_to_be_clickable(self.book_button)
        ).click()

    # ---------------------------------------------------------
    # Правила
    # ---------------------------------------------------------

    def check_rules_and_next(self):
        wait = WebDriverWait(self.driver, 5)

        try:
            wait.until(
                EC.element_to_be_clickable(self.rules_checkbox)
            ).click()

        except TimeoutException:
            pass

        # "Далее" нажимаем только один раз
        wait.until(
            EC.element_to_be_clickable(self.next_button)
        ).click()

    # ---------------------------------------------------------
    # Филиал
    # ---------------------------------------------------------

    def select_oybek(self):
        wait = WebDriverWait(self.driver, 10)

        wait.until(
            EC.element_to_be_clickable(self.oybek)
        ).click()

    def click_select_branch(self):
        wait = WebDriverWait(self.driver, 10)

        wait.until(
            EC.element_to_be_clickable(self.select_branch_button)
        ).click()

    # ---------------------------------------------------------
    # Дата
    # ---------------------------------------------------------

    def select_date(self):
        wait = WebDriverWait(self.driver, 10)

        element = wait.until(
            EC.presence_of_element_located(self.date)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    # ---------------------------------------------------------
    # Группа
    # ---------------------------------------------------------

    def select_group(self):
        wait = WebDriverWait(self.driver, 10)

        element = wait.until(
            EC.presence_of_element_located(self.group)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    def select_group_circle(self):
        wait = WebDriverWait(self.driver, 10)

        wait.until(
            EC.element_to_be_clickable(self.group_circle)
        ).click()

    def click_select_group(self):
        wait = WebDriverWait(self.driver, 10)

        wait.until(
            EC.element_to_be_clickable(self.select_group_button)
        ).click()

    # ---------------------------------------------------------
    # Время
    # ---------------------------------------------------------

    def select_time(self):
        wait = WebDriverWait(self.driver, 10)

        element = wait.until(
            EC.presence_of_element_located(self.time)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    def select_time_cell(self, time_value):
        wait = WebDriverWait(self.driver, 10)

        time_cell = wait.until(
            EC.presence_of_element_located(self.time_cell)
        )

        time_cell.click()

        active_element = self.driver.switch_to.active_element

        active_element.click()

        ActionChains(self.driver) \
            .key_down(Keys.CONTROL) \
            .send_keys("a") \
            .key_up(Keys.CONTROL) \
            .send_keys(Keys.BACKSPACE) \
            .send_keys(str(time_value)) \
            .perform()

    def click_select_time(self):
        wait = WebDriverWait(self.driver, 10)

        element = wait.until(
            EC.presence_of_element_located(self.select_time_button)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )


    # ---------------------------------------------------------
    # Место
    # ---------------------------------------------------------

    def select_place(self):
        wait = WebDriverWait(self.driver, 10)

        element = wait.until(
            EC.presence_of_element_located(self.place)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    def select_place_cell(self):
        wait = WebDriverWait(self.driver, 10)

        wait.until(
            EC.element_to_be_clickable(self.place_cell)
        ).click()

    def click_confirm_place(self):
        wait = WebDriverWait(self.driver, 10)

        wait.until(
            EC.element_to_be_clickable(self.confirm_place_button)
        ).click()


    # ---------------------------------------------------------
    # Финальная запись
    # ---------------------------------------------------------

    def click_final_book(self):
        wait = WebDriverWait(self.driver, 10)

        wait.until(
            EC.element_to_be_clickable(self.final_book_button)
        ).click()