import pytest
from selenium.webdriver.common.by import By

class TestPersonalAccount:
    def test_personal_account_click(self, driver, base_url):
        """Проверка перехода в личный кабинет"""
        # 1. Открываем главную страницу
        driver.get(base_url)
        
        # 2. Находим кнопку "Личный кабинет"
        account_button = driver.find_element(By.XPATH, "//a[@href='/account']")
        
        # 3. Кликаем по кнопке
        account_button.click()
        
        # 4. Проверяем переход на страницу входа
        assert driver.current_url == f"{base_url}login", \
            f"Ожидался переход на {base_url}login, но открыт {driver.current_url}"
        
        # 5. Проверяем наличие заголовка "Вход"
        login_title = driver.find_element(By.XPATH, "//h2[text()='Вход']")
        assert login_title.is_displayed(), "Заголовок 'Вход' не отображается"