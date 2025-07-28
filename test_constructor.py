import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import BASE_URL
from locators import ConstructorPageLocators

class TestConstructorNavigation:
    """Тесты навигации между разделами конструктора"""
    
    def test_buns_section(self, driver):
        """Тест переключения между разделами 'Булки' и 'Соусы'"""
        driver.get(BASE_URL)
        
        # Проверка активной вкладки "Булки" по умолчанию
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(ConstructorPageLocators.ACTIVE_TAB, "Булки")
        )
        
        # Переключение на вкладку "Соусы"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorPageLocators.SAUCES_TAB)
        ).click()
        
        # Проверка активной вкладки "Соусы"
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(ConstructorPageLocators.ACTIVE_TAB, "Соусы")
        )
        
        # Возврат на вкладку "Булки"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorPageLocators.BUNS_TAB)
        ).click()
        
        # Финальная проверка активной вкладки "Булки"
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(ConstructorPageLocators.ACTIVE_TAB, "Булки")
        )

    def test_sauces_section(self, driver):
        """Тест переключения на раздел 'Соусы'"""
        driver.get(BASE_URL)
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorPageLocators.SAUCES_TAB)
        ).click()
        
        active_tab = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ConstructorPageLocators.ACTIVE_TAB)
        )
        assert "Соусы" in active_tab.text, "Раздел 'Соусы' не активирован"

    def test_toppings_section(self, driver):
        """Тест переключения на раздел 'Начинки'"""
        driver.get(BASE_URL)
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorPageLocators.TOPPINGS_TAB)
        ).click()
        
        active_tab = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ConstructorPageLocators.ACTIVE_TAB)
        )
        assert "Начинки" in active_tab.text, "Раздел 'Начинки' не активирован"