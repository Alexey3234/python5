from selenium.webdriver.common.by import By


class ConstructorPageLocators:
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
    TOPPINGS_TAB = (By.XPATH, "//span[text()='Начинки']")
    ACTIVE_TAB = (By.CSS_SELECTOR, ".tab_tab__1SPyG.tab_tab_type_current__2BEPc")