from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы главной страницы"""
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/account']")
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")


class ConstructorPageLocators:
    """Локаторы конструктора"""
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    BUNS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab')]//span[text()='Булки']/..")
    SAUCES_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab')]//span[text()='Соусы']/..")
    TOPPINGS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab')]//span[text()='Начинки']/..")
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]/span")
    BUNS_SECTION = (By.XPATH, "//h2[text()='Булки']/..")
    SAUCES_SECTION = (By.XPATH, "//h2[text()='Соусы']/..")
    TOPPINGS_SECTION = (By.XPATH, "//h2[text()='Начинки']/..")


class LoginPageLocators:
    """Локаторы страницы входа"""
    LOGIN_HEADER = (By.XPATH, "//h2[contains(text(), 'Вход')]")
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")


class RegistrationPageLocators:
    """Локаторы страницы регистрации"""
    REGISTRATION_HEADER = (By.XPATH, "//h2[contains(text(), 'Регистрация')]")
    NAME_INPUT = (By.XPATH, "//label[contains(text(), 'Имя')]/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")
    PASSWORD_ERROR = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")


class ForgotPasswordLocators:
    """Локаторы страницы восстановления пароля"""
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
    
class AccountPageLocators:
    """Локаторы страницы личного кабинета"""
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")