import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import BASE_URL
from locators import (MainPageLocators, RegistrationPageLocators, ForgotPasswordLocators)
from helpers import LoginHelper

class TestLogin:
    """Тесты авторизации пользователя"""
    
    def test_login_from_main_page_button(self, driver, registered_user):
        """Тест входа через кнопку на главной странице"""
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)
        ).click()
        
        LoginHelper.perform_login(driver, registered_user["email"], registered_user["password"])
        assert BASE_URL == driver.current_url

    def test_login_from_personal_account_button(self, driver, registered_user):
        """Тест входа через кнопку личного кабинета"""
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.ACCOUNT_BUTTON)
        ).click()
        
        LoginHelper.perform_login(driver, registered_user["email"], registered_user["password"])
        assert BASE_URL == driver.current_url

    def test_login_from_registration_form(self, driver, registered_user):
        """Тест входа через форму регистрации"""
        driver.get(f"{BASE_URL}register")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(RegistrationPageLocators.LOGIN_LINK)
        ).click()
        
        LoginHelper.perform_login(driver, registered_user["email"], registered_user["password"])
        assert BASE_URL == driver.current_url

    def test_login_from_forgot_password_form(self, driver, registered_user):
        """Тест входа через форму восстановления пароля"""
        driver.get(f"{BASE_URL}forgot-password")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ForgotPasswordLocators.LOGIN_LINK)
        ).click()
        
        LoginHelper.perform_login(driver, registered_user["email"], registered_user["password"])
        assert BASE_URL == driver.current_url