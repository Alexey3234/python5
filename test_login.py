import pytest
from selenium.webdriver.common.by import By

class TestLogin:
    def perform_login(self, driver, email, password, base_url):
        """Выполняет вход в систему"""
        try:
            # Поиск полей ввода
            email_field = driver.find_element(By.XPATH, "//input[@name='name']")
            email_field.clear()
            email_field.send_keys(email)
            
            password_field = driver.find_element(By.XPATH, "//input[@type='password']")
            password_field.clear()
            password_field.send_keys(password)
            
            # Нажатие кнопки входа
            login_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
            login_button.click()
            
            # Проверка успешного входа
            assert base_url in driver.current_url
            return True
        except Exception as e:
            print(f"Ошибка при входе: {str(e)}")
            return False

    def test_login_from_main_page_button(self, driver, base_url, test_credentials):
        """Вход через кнопку 'Войти в аккаунт' на главной"""
        driver.get(base_url)
        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
        assert self.perform_login(driver, test_credentials["email"], test_credentials["password"], base_url), "Вход не выполнен"
        assert base_url in driver.current_url

    def test_login_from_personal_account_button(self, driver, base_url, test_credentials):
        """Вход через кнопку 'Личный кабинет'"""
        driver.get(base_url)
        driver.find_element(By.XPATH, "//a[@href='/account']").click()
        assert self.perform_login(driver, test_credentials["email"], test_credentials["password"], base_url), "Вход не выполнен"
        assert base_url in driver.current_url

    def test_login_from_registration_form(self, driver, base_url, test_credentials):
        """Вход через кнопку в форме регистрации"""
        driver.get(f"{base_url}register")
        driver.find_element(By.XPATH, "//a[text()='Войти']").click()
        assert self.perform_login(driver, test_credentials["email"], test_credentials["password"], base_url), "Вход не выполнен"
        assert base_url in driver.current_url

    def test_login_from_forgot_password_form(self, driver, base_url, test_credentials):
        """Вход через кнопку в форме восстановления пароля"""
        driver.get(f"{base_url}forgot-password")
        driver.find_element(By.XPATH, "//a[text()='Войти']").click()
        assert self.perform_login(driver, test_credentials["email"], test_credentials["password"], base_url), "Вход не выполнен"
        assert base_url in driver.current_url