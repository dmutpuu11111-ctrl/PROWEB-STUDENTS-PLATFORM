import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture
def driver_chrome():
    options = ChromeOptions()

    if os.getenv("CI") == "true":
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    if os.getenv("CI") != "true":
        driver.maximize_window()

    yield driver
    driver.quit()


@pytest.fixture
def driver_edge():
    options = EdgeOptions()
    options.page_load_strategy = "eager"

    if os.getenv("CI") == "true":
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

    driver = webdriver.Edge(options=options)
    driver.implicitly_wait(10)

    if os.getenv("CI") != "true":
        driver.maximize_window()

    yield driver
    driver.quit()


@pytest.fixture
def driver_firefox():
    options = FirefoxOptions()

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