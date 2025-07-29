# conftest.py
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import BASE_URL

@pytest.fixture(scope="function")
def driver():
    """Фикстура для инициализации и завершения работы драйвера"""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def user_credentials():
    """Генерирует уникальные учетные данные пользователя"""
    timestamp = int(time.time() * 1000)
    return {
        "name": f"TestUser{timestamp}",
        "email": f"test{timestamp}@example.com",
        "password": f"Password{timestamp % 10000}"
    }

@pytest.fixture
def registered_user(driver, user_credentials):
    """Фикстура регистрации нового пользователя"""
    driver.get(f"{BASE_URL}register")
    
    # Ожидаем загрузку формы регистрации
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[text()='Регистрация']"))
    )
    
    # Используем более надежные локаторы
    name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Имя')]/following-sibling::input"))
    )
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input"))
    )
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='password']"))
    )
    
    # Заполнение формы
    name_input.send_keys(user_credentials["name"])
    email_input.send_keys(user_credentials["email"])
    password_input.send_keys(user_credentials["password"])
    
    # Отправка формы
    driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()
    
    # Ожидание перехода на страницу входа
    WebDriverWait(driver, 15).until(EC.url_contains("login"))
    return user_credentials

@pytest.fixture
def login(driver, registered_user):
    """Фикстура для выполнения входа зарегистрированного пользователя"""
    def _login():
        driver.get(f"{BASE_URL}login")
        
        # Ожидаем загрузку формы входа
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']"))
        )
        
        # Находим поля с более надежными локаторами
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='text' and contains(@name, 'name')]"))
        )
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='password']"))
        )
        
        # Заполняем поля
        email_field.clear()
        email_field.send_keys(registered_user["email"])
        password_field.clear()
        password_field.send_keys(registered_user["password"])
        
        # Кликаем кнопку входа
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти']"))
        )
        login_button.click()
        
        # Ожидаем успешного входа
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']"))
        )
    return _login

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get('driver')
        if driver is not None:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            driver.save_screenshot(f"failure_{item.name}_{timestamp}.png")
