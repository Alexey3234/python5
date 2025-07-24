import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


def test_successful_registration(driver, base_url, test_credentials):
    driver.get(base_url)
    
    login_button = driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']")
    login_button.click()
    
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))
    
    register_button = driver.find_element(By.XPATH, "//a[text()='Зарегистрироваться']")
    register_button.click()
    
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Регистрация']")))
    
    name_input = driver.find_element(By.XPATH, "//fieldset[1]//input")
    email_input = driver.find_element(By.XPATH, "//fieldset[2]//input")
    password_input = driver.find_element(By.XPATH, "//fieldset[3]//input")
    
    test_name = "Алексей"
    name_input.send_keys(test_name)
    email_input.send_keys(test_credentials["email"])
    password_input.send_keys(test_credentials["password"])
    
    assert name_input.get_attribute("value") == test_name, "Имя должно быть заполнено"
    assert "@" in test_credentials["email"], "Email должен содержать @"
    assert "." in test_credentials["email"].split("@")[1], "Email должен содержать домен"
    assert len(test_credentials["password"]) >= 6, "Пароль должен быть ≥6 символов"
    
    submit_button = driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']")
    submit_button.click()
    
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))


def test_invalid_password_registration(driver, base_url):
    driver.get(base_url)
    
    login_button = driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']")
    login_button.click()
    
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))
    
    register_button = driver.find_element(By.XPATH, "//a[text()='Зарегистрироваться']")
    register_button.click()
    
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Регистрация']")))
    
    name_input = driver.find_element(By.XPATH, "//fieldset[1]//input")
    email_input = driver.find_element(By.XPATH, "//fieldset[2]//input")
    password_input = driver.find_element(By.XPATH, "//fieldset[3]//input")
    
    name_input.send_keys("Тестовое Имя")
    email_input.send_keys(f"test{int(time.time())}@example.com")  
    password_input.send_keys("12345")  
    
    assert len("12345") < 6, "Пароль должен быть <6 символов для этого теста"
    
    submit_button = driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']")
    submit_button.click()
    
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")))
    assert error_message.is_displayed()