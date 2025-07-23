import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def base_url():
    return "https://stellarburgers.nomoreparties.site/"

import time
import random

@pytest.fixture
def test_credentials():
    random_part = int(time.time() * 1000)  
    return {
        "name": f"Тестовый Пользователь {random_part}",
        "email": f"user_{random_part}@example.com",
        "password": f"Pass{random_part % 10000}"  
    }