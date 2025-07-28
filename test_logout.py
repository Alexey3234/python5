import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import BASE_URL

class TestAccountLogout:
    """Тесты выхода из аккаунта"""
    
    def test_logout_from_account(self, driver, login):
        """Тест выхода из личного кабинета"""
        login()  # Выполняем вход через фикстуру
        
        # Переходим в личный кабинет
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/account')]"))
        ).click()
        
        # Выходим из аккаунта
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Выход')]"))
        ).click()
        
        # Проверяем, что произошел выход
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Войти')]"))
        )
        
        assert not driver.current_url.endswith("/account"), "После выхода не должно быть доступа к личному кабинету"

class TestNavigationFromAccount:
    """Тесты навигации из личного кабинета"""
    
    def test_navigate_to_constructor_via_button(self, driver, login):
        """Тест перехода в конструктор через кнопку"""
        login()
        driver.get(f"{BASE_URL}account")
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//p[text()='Конструктор']"))
        ).click()
        
        assert driver.current_url == BASE_URL, \
            f"После клика на 'Конструктор' ожидался переход на {BASE_URL}"

    def test_navigate_to_constructor_via_logo(self, driver, login):
        """Тест перехода в конструктор через логотип"""
        login()
        driver.get(f"{BASE_URL}account")
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "AppHeader_header__logo__2D0X2"))
        ).click()
        
        assert driver.current_url == BASE_URL, \
            f"После клика на логотип ожидался переход на {BASE_URL}"

class TestPersonalAccount:
    """Тесты личного кабинета"""
    
    def test_personal_account_click(self, driver):
        """Тест перехода в личный кабинет без авторизации"""
        driver.get(BASE_URL)
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/account']"))
        ).click()
        
        assert driver.current_url == f"{BASE_URL}login", \
            f"Ожидался переход на страницу входа"
        
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']"))
        ).is_displayed(), "Заголовок 'Вход' не отображается"