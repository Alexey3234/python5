import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


def test_successful_registration(driver, base_url, test_credentials):
    """Тест успешной регистрации"""
    driver.get(base_url)
    
    # Нажимаем кнопку "Войти в аккаунт"
    login_button = driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']")
    login_button.click()
    
    # Ждем появления формы входа
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))
    
    # Нажимаем кнопку "Зарегистрироваться"
    register_button = driver.find_element(By.XPATH, "//a[text()='Зарегистрироваться']")
    register_button.click()
    
    # Ждем появления формы регистрации
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Регистрация']")))
    
    # Заполняем форму регистрации
    name_input = driver.find_element(By.XPATH, "//fieldset[1]//input")
    email_input = driver.find_element(By.XPATH, "//fieldset[2]//input")
    password_input = driver.find_element(By.XPATH, "//fieldset[3]//input")
    
    test_name = "Алексей"
    name_input.send_keys(test_name)
    email_input.send_keys(test_credentials["email"])
    password_input.send_keys(test_credentials["password"])
    
    # Дополнительные проверки перед отправкой
    assert name_input.get_attribute("value") == test_name, "Имя должно быть заполнено"
    assert "@" in test_credentials["email"], "Email должен содержать @"
    assert "." in test_credentials["email"].split("@")[1], "Email должен содержать домен"
    assert len(test_credentials["password"]) >= 6, "Пароль должен быть ≥6 символов"
    
    # Нажимаем кнопку "Зарегистрироваться"
    submit_button = driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']")
    submit_button.click()
    
    # Проверяем, что произошел переход на страницу входа
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))


def test_invalid_password_registration(driver, base_url):
    """Тест ошибки при некорректном пароле (менее 6 символов)"""
    driver.get(base_url)
    
    # Нажимаем кнопку "Войти в аккаунт"
    login_button = driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']")
    login_button.click()
    
    # Ждем появления формы входа
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))
    
    # Нажимаем кнопку "Зарегистрироваться"
    register_button = driver.find_element(By.XPATH, "//a[text()='Зарегистрироваться']")
    register_button.click()
    
    # Ждем появления формы регистрации
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Регистрация']")))
    
    # Заполняем форму регистрации с некорректным паролем
    name_input = driver.find_element(By.XPATH, "//fieldset[1]//input")
    email_input = driver.find_element(By.XPATH, "//fieldset[2]//input")
    password_input = driver.find_element(By.XPATH, "//fieldset[3]//input")
    
    name_input.send_keys("Тестовое Имя")
    email_input.send_keys(f"test{int(time.time())}@example.com")  # Уникальный email
    password_input.send_keys("12345")  # Пароль менее 6 символов
    
    # Проверяем длину пароля
    assert len("12345") < 6, "Пароль должен быть <6 символов для этого теста"
    
    # Нажимаем кнопку "Зарегистрироваться"
    submit_button = driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']")
    submit_button.click()
    
    # Проверяем, что появилось сообщение об ошибке
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")))
    assert error_message.is_displayed()