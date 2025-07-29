import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import BASE_URL
from locators import (
    MainPageLocators,
    ConstructorPageLocators,
    LoginPageLocators,
    AccountPageLocators
)


class TestAccountLogout:
    """Тесты выхода из аккаунта"""
    
    def test_logout_from_account(self, driver, login):
        """Тест выхода из личного кабинета"""
        login()  
        
        # Переходим в личный кабинет
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.ACCOUNT_BUTTON)
        ).click()
        
        # Выходим из аккаунта
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(AccountPageLocators.LOGOUT_BUTTON)
        ).click()
        
        # Проверяем, что произошел выход
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        )
        
        assert not driver.current_url.endswith("/account"), "После выхода не должно быть доступа к личному кабинету"


class TestNavigationFromAccount:
    """Тесты навигации из личного кабинета"""
    
    def test_navigate_to_constructor_via_button(self, driver, login):
        """Тест перехода в конструктор через кнопку"""
        login()
        driver.get(f"{BASE_URL}account")
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorPageLocators.CONSTRUCTOR_BUTTON)
        ).click()
        
        assert driver.current_url == BASE_URL, \
            f"После клика на 'Конструктор' ожидался переход на {BASE_URL}"

    def test_navigate_to_constructor_via_logo(self, driver, login):
        """Тест перехода в конструктор через логотип"""
        login()
        driver.get(f"{BASE_URL}account")
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGO)
        ).click()
        
        assert driver.current_url == BASE_URL, \
            f"После клика на логотип ожидался переход на {BASE_URL}"


class TestPersonalAccount:
    """Тесты личного кабинета"""
    
    def test_personal_account_click(self, driver):
        """Тест перехода в личный кабинет без авторизации"""
        driver.get(BASE_URL)
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.ACCOUNT_BUTTON)
        ).click()
        
        assert driver.current_url == f"{BASE_URL}login", \
            f"Ожидался переход на страницу входа"
        
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_HEADER)
        ).is_displayed(), "Заголовок 'Вход' не отображается"