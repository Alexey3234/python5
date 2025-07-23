import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_logout_from_account(driver, base_url, test_credentials):
    """Тест выхода из аккаунта через личный кабинет."""
    try:
        # 1. Регистрация нового пользователя
        driver.get(f"{base_url}register")
        
        # Ожидаем загрузки формы регистрации
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Регистрация')]"))
        )

        # Заполняем форму регистрации
        name_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Имя')]/following-sibling::input"))
        )
        name_field.send_keys(test_credentials["name"])

        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input"))
        )
        email_field.send_keys(test_credentials["email"])

        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='password']"))
        )
        password_field.send_keys(test_credentials["password"])

        register_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]"))
        )
        register_button.click()

        # 2. Авторизация нового пользователя
        WebDriverWait(driver, 10).until(
            EC.url_contains("login")
        )

        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='text']"))
        )
        email_input.send_keys(test_credentials["email"])

        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='password']"))
        )
        password_input.send_keys(test_credentials["password"])

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Войти')]"))
        )
        login_button.click()

        # 3. Переход в личный кабинет
        account_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/account')]"))
        )
        account_link.click()

        # 4. Выход из аккаунта
        logout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Выход')]"))
        )
        logout_button.click()

        # 5. Проверка успешного выхода
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Войти')]"))
        )
        
        # Ожидаем либо главную страницу, либо страницу логина (в зависимости от поведения системы)
        WebDriverWait(driver, 10).until(
            lambda d: d.current_url == base_url or d.current_url == f"{base_url}login"
        )
        
        # Проверяем, что мы НЕ находимся в личном кабинете
        assert not driver.current_url.endswith("/account"), "После выхода не должно быть доступа к личному кабинету"
        
        # Проверяем наличие кнопки "Войти"
        assert WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Войти')]"))
        ), "Кнопка 'Войти' должна отображаться после выхода"

        print("\nТест успешен: выход выполнен, кнопка 'Войти' отображается")

    except Exception as e:
        driver.save_screenshot("logout_error.png")
        pytest.fail(f"Тест упал с ошибкой: {str(e)}\nСкриншот сохранен как logout_error.png")