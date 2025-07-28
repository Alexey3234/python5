import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import BASE_URL  # Используем BASE_URL из отдельного модуля

class TestRegistration:
    """Тесты регистрации пользователя"""
    
    @pytest.fixture
    def temp_credentials(self):
        """Генерация уникальных учетных данных для теста"""
        timestamp = int(time.time() * 1000)
        return {
            "name": f"User{timestamp}",
            "email": f"user{timestamp}@example.com",
            "password": f"Pass{timestamp % 10000}"
        }

    def test_successful_registration(self, driver, temp_credentials):
        """Тест успешной регистрации нового пользователя"""
        # Переходим на страницу регистрации
        driver.get(f"{BASE_URL}register")
        
        # Ожидаем загрузку страницы
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Регистрация')]"))
        )
        
        # Заполняем форму регистрации с явными ожиданиями
        name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Имя')]/following-sibling::input"))
        )
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input"))
        )
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='password']"))
        )
        
        name_input.send_keys(temp_credentials["name"])
        email_input.send_keys(temp_credentials["email"])
        password_input.send_keys(temp_credentials["password"])
        
        # Отправляем форму
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]"))
        ).click()
        
        # Проверяем успешную регистрацию (редирект на страницу входа)
        WebDriverWait(driver, 10).until(
            EC.url_contains("login")
        )
        assert "login" in driver.current_url, "После регистрации должен быть редирект на страницу входа"
        
        # Проверяем наличие заголовка "Вход"
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Вход')]"))
        ).is_displayed(), "Заголовок страницы входа не отображается"

    def test_invalid_password_registration(self, driver):
        """Тест регистрации с некорректным паролем"""
        # Переходим на страницу регистрации
        driver.get(f"{BASE_URL}register")
        
        # Ожидаем загрузку страницы
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Регистрация')]"))
        )
        
        # Заполняем форму с некорректным паролем
        name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Имя')]/following-sibling::input"))
        )
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input"))
        )
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='password']"))
        )
        
        name_input.send_keys("Тестовое Имя")
        email_input.send_keys(f"test{int(time.time())}@example.com")
        password_input.send_keys("12345")  # Пароль короче 6 символов
        
        # Отправляем форму
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]"))
        ).click()
        
        # Проверяем сообщение об ошибке
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Некорректный пароль')]"))
        )
        assert error_message.is_displayed(), "Сообщение об ошибке не отображается"
        assert "register" in driver.current_url, "При ошибке регистрации не должно быть редиректа"