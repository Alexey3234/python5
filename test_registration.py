import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import BASE_URL
from locators import RegistrationPageLocators, LoginPageLocators


class TestRegistration:
    """Тесты регистрации пользователя"""

    def test_successful_registration(self, driver, user_credentials):
        """Тест успешной регистрации нового пользователя"""
        # Переходим на страницу регистрации
        driver.get(f"{BASE_URL}register")

        # Ожидаем загрузку страницы
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.REGISTRATION_HEADER)
        )

        # Заполняем форму регистрации
        name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RegistrationPageLocators.NAME_INPUT)
        )
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RegistrationPageLocators.EMAIL_INPUT)
        )
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RegistrationPageLocators.PASSWORD_INPUT)
        )

        name_input.send_keys(user_credentials["name"])
        email_input.send_keys(user_credentials["email"])
        password_input.send_keys(user_credentials["password"])

        # Отправляем форму
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(RegistrationPageLocators.SUBMIT_BUTTON)
        ).click()

        # Проверяем успешную регистрацию (редирект на страницу входа)
        WebDriverWait(driver, 10).until(
            EC.url_contains("login")
        )
        assert "login" in driver.current_url, "После регистрации должен быть редирект на страницу входа"

        # Проверяем наличие заголовка "Вход"
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_HEADER)
        ).is_displayed(), "Заголовок страницы входа не отображается"

    def test_invalid_password_registration(self, driver):
        """Тест регистрации с некорректным паролем"""
        # Переходим на страницу регистрации
        driver.get(f"{BASE_URL}register")

        # Ожидаем загрузку страницы
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.REGISTRATION_HEADER)
        )

        # Заполняем форму с некорректным паролем
        name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RegistrationPageLocators.NAME_INPUT)
        )
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RegistrationPageLocators.EMAIL_INPUT)
        )
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RegistrationPageLocators.PASSWORD_INPUT)
        )

        name_input.send_keys("Тестовое Имя")
        email_input.send_keys(f"test{int(time.time())}@example.com")
        password_input.send_keys("12345")

        # Отправляем форму
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(RegistrationPageLocators.SUBMIT_BUTTON)
        ).click()

        # Проверяем сообщение об ошибке
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.PASSWORD_ERROR)
        )
        assert error_message.is_displayed(), "Сообщение об ошибке не отображается"
        assert "register" in driver.current_url, "При ошибке регистрации не должно быть редиректа"

