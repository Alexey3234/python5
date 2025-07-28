import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import BASE_URL  # Импортируем BASE_URL из отдельного модуля

class TestPersonalAccount:
    """Тесты для проверки личного кабинета"""
    
    def test_personal_account_click(self, driver):
        """Тест перехода в личный кабинет без авторизации"""
        # Переходим на главную страницу
        driver.get(BASE_URL)
        
        # Ожидаем и кликаем на кнопку личного кабинета
        account_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/account']"))
        )
        account_button.click()
        
        # Проверяем редирект на страницу входа
        WebDriverWait(driver, 10).until(
            EC.url_contains("login")
        )
        assert driver.current_url == f"{BASE_URL}login", \
            f"Ожидался переход на {BASE_URL}login, получен {driver.current_url}"
        
        # Проверяем отображение заголовка страницы входа
        login_title = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']"))
        )
        assert login_title.is_displayed(), "Заголовок 'Вход' не отображается"