from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver, base_url, test_credentials):
    wait = WebDriverWait(driver, 10)  # Ожидание до 10 секунд

    # 1. Переход на страницу входа
    driver.get(f"{base_url}login")

    # 2. Ожидание появления формы входа (проверяем заголовок "Вход")
    wait.until(
        EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']"))
    )

    # 3. Ввод email и пароля
    email_field = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//input[@name='name']"))
    )
    email_field.send_keys(test_credentials["email"])

    password_field = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//input[@type='password']"))
    )
    password_field.send_keys(test_credentials["password"])

    # 4. Клик по кнопке "Войти"
    login_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти']"))
    )
    login_button.click()

    # 5. Ожидание успешного входа (например, появления кнопки "Оформить заказ" на главной)
    wait.until(
        EC.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']"))
    )

    from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators

class LoginHelper:
    @staticmethod
    def perform_login(driver, email, password):
        """Выполняет вход в систему"""
        email_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        email_field.clear()
        email_field.send_keys(email)
        
        password_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.PASSWORD_INPUT)
        )
        password_field.clear()
        password_field.send_keys(password)
        
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
        )
        login_button.click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.ORDER_BUTTON)
        )