import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import BASE_URL
from locators import MainPageLocators, ConstructorPageLocators, LoginPageLocators


class TestNavigationFromAccount:
    """Тесты навигации из личного кабинета"""
    
    def test_navigate_to_constructor_via_button(self, driver, login):
        """Тест перехода в конструктор через кнопку"""
        login()  
        
        # Переходим в личный кабинет
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.ACCOUNT_BUTTON)
        ).click()
        
        # Кликаем на кнопку "Конструктор"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorPageLocators.CONSTRUCTOR_BUTTON)
        ).click()
        
        # Проверяем переход на главную страницу
        WebDriverWait(driver, 10).until(
            EC.url_to_be(BASE_URL)
        )
        assert driver.current_url == BASE_URL, \
            f"После клика на 'Конструктор' ожидался переход на {BASE_URL}"

    def test_navigate_to_constructor_via_logo(self, driver, login):
        """Тест перехода в конструктор через логотип"""
        login() 
        
        # Переходим в личный кабинет
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.ACCOUNT_BUTTON)
        ).click()
        
        # Кликаем на логотип
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGO)
        ).click()
        
        # Проверяем переход на главную страницу
        WebDriverWait(driver, 10).until(
            EC.url_to_be(BASE_URL)
        )
        assert driver.current_url == BASE_URL, \
            f"После клика на логотип ожидался переход на {BASE_URL}"