import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import BASE_URL
from locators import ConstructorPageLocators


class TestConstructorNavigation:
    """Тесты навигации между разделами конструктора"""
    
    def test_buns_section_by_default(self, driver):
        """Проверка, что по умолчанию активна вкладка 'Булки'"""
        driver.get(BASE_URL)
        
        active_tab = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ConstructorPageLocators.ACTIVE_TAB)
        )
        assert active_tab.text == "Булки", f"Ожидалась активная вкладка 'Булки', но получили '{active_tab.text}'"
    
    def test_switch_between_buns_and_sauces(self, driver):
        """Тест переключения между разделами 'Булки' и 'Соусы'"""
        driver.get(BASE_URL)
        
        # Ожидаем загрузки конструктора
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(ConstructorPageLocators.BUNS_SECTION)
        )
        
        # Проверяем начальное состояние
        active_tab = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ConstructorPageLocators.ACTIVE_TAB)
        )
        assert active_tab.text == "Булки", "По умолчанию должна быть активна вкладка 'Булки'"
        
        # Переключаемся на соусы
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorPageLocators.SAUCES_TAB)
        ).click()
        
        # Ждем активации вкладки "Соусы"
        WebDriverWait(driver, 15).until(
            EC.text_to_be_present_in_element(ConstructorPageLocators.ACTIVE_TAB, "Соусы")
        )
        
        # Возвращаемся на булки
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorPageLocators.BUNS_TAB)
        ).click()
        
        # Ждем активации вкладки "Булки" с увеличенным таймаутом
        WebDriverWait(driver, 15).until(
            EC.text_to_be_present_in_element(ConstructorPageLocators.ACTIVE_TAB, "Булки")
        )
        
        # Дополнительная проверка видимости раздела
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ConstructorPageLocators.BUNS_SECTION)
        )    

    def test_switch_to_toppings_section(self, driver):
        """Тест переключения на раздел 'Начинки'"""
        driver.get(BASE_URL)
        
        toppings_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorPageLocators.TOPPINGS_TAB)
        )
        toppings_tab.click()
        
        # Ждем появления раздела начинок
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ConstructorPageLocators.TOPPINGS_SECTION)
        )
        
        active_tab = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ConstructorPageLocators.ACTIVE_TAB)
        )
        assert active_tab.text == "Начинки", f"Ожидалась активная вкладка 'Начинки', но получили '{active_tab.text}'"