# test_login.py
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import BASE_URL

class TestLogin:
    """Тесты авторизации пользователя"""
    
    def perform_login(self, driver, email, password):
        """Вспомогательный метод для выполнения входа"""
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='name']"))
        )
        email_field.clear()
        email_field.send_keys(email)
        
        password_field = driver.find_element(By.XPATH, "//input[@type='password']")
        password_field.clear()
        password_field.send_keys(password)
        
        login_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
        login_button.click()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Оформить заказ']"))
        )

    def test_login_from_main_page_button(self, driver, registered_user):
        """Тест входа через кнопку на главной странице"""
        driver.get(BASE_URL)
        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
        self.perform_login(driver, registered_user["email"], registered_user["password"])
        assert BASE_URL in driver.current_url

    def test_login_from_personal_account_button(self, driver, registered_user):
        """Тест входа через кнопку личного кабинета"""
        driver.get(BASE_URL)
        driver.find_element(By.XPATH, "//a[@href='/account']").click()
        self.perform_login(driver, registered_user["email"], registered_user["password"])
        assert BASE_URL in driver.current_url

    def test_login_from_registration_form(self, driver, registered_user):
        """Тест входа через форму регистрации"""
        driver.get(f"{BASE_URL}register")
        driver.find_element(By.XPATH, "//a[text()='Войти']").click()
        self.perform_login(driver, registered_user["email"], registered_user["password"])
        assert BASE_URL in driver.current_url

    def test_login_from_forgot_password_form(self, driver, registered_user):
        """Тест входа через форму восстановления пароля"""
        driver.get(f"{BASE_URL}forgot-password")
        driver.find_element(By.XPATH, "//a[text()='Войти']").click()
        self.perform_login(driver, registered_user["email"], registered_user["password"])
        assert BASE_URL in driver.current_url