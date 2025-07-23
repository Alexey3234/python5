import pytest
from selenium.webdriver.common.by import By
import time

class TestNavigationFromAccount:
    def login(self, driver, base_url, test_credentials):
        """Вспомогательный метод для авторизации"""
        driver.get(f"{base_url}login")
        time.sleep(2)
        
        driver.find_element(By.XPATH, "//input[@name='name']").send_keys(test_credentials["email"])
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(test_credentials["password"])
        time.sleep(1)
        
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        time.sleep(2)

    def test_navigate_to_constructor_via_button(self, driver, base_url, test_credentials):
        """Проверка перехода в конструктор через кнопку 'Конструктор'"""
        # Авторизуемся и переходим в личный кабинет
        self.login(driver, base_url, test_credentials)
        driver.get(f"{base_url}account")
        time.sleep(2)
        
        # Кликаем на "Конструктор"
        driver.find_element(By.XPATH, "//p[text()='Конструктор']").click()
        time.sleep(2)
        
        # Проверяем переход на главную страницу
        assert driver.current_url == base_url, \
            f"После клика на 'Конструктор' ожидался переход на {base_url}, но открыт {driver.current_url}"

    def test_navigate_to_constructor_via_logo(self, driver, base_url, test_credentials):
        """Проверка перехода в конструктор через логотип"""
        # Авторизуемся и переходим в личный кабинет
        self.login(driver, base_url, test_credentials)
        driver.get(f"{base_url}account")
        time.sleep(2)
        
        # Кликаем на логотип
        driver.find_element(By.CLASS_NAME, "AppHeader_header__logo__2D0X2").click()
        time.sleep(2)
        
        # Проверяем переход на главную страницу
        assert driver.current_url == base_url, \
            f"После клика на логотип ожидался переход на {base_url}, но открыт {driver.current_url}"