import pytest
from selenium.webdriver.common.by import By

class TestPersonalAccount:
    def test_personal_account_click(self, driver, base_url):
        driver.get(base_url)
        
        account_button = driver.find_element(By.XPATH, "//a[@href='/account']")
        
        account_button.click()
        
        assert driver.current_url == f"{base_url}login", \
            f"Ожидался переход на {base_url}login, но открыт {driver.current_url}"
        
        login_title = driver.find_element(By.XPATH, "//h2[text()='Вход']")
        assert login_title.is_displayed(), "Заголовок 'Вход' не отображается"