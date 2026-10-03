import os

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def driver_chrome():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture
def driver_edge():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture
def driver_firefox():
    options = Options()

    if os.getenv("CI") == "true":
        options.add_argument("--headless")
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")

    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(10)

    if os.getenv("CI") != "true":
        driver.maximize_window()

    yield driver
    driver.quit()