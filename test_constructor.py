import pytest
from selenium.webdriver.common.by import By
import time

class TestConstructorNavigation:
    def test_buns_section(self, driver, base_url):
        """Проверка перехода в раздел 'Булки'"""
        driver.get(base_url)
        time.sleep(2)
        
        # Прокручиваем до раздела Соусы и кликаем
        driver.find_element(By.XPATH, "//span[text()='Соусы']").click()
        time.sleep(1)
        
        # Кликаем на раздел Булки
        driver.find_element(By.XPATH, "//span[text()='Булки']").click()
        time.sleep(1)
        
        # Проверяем активность раздела
        active_tab = driver.find_element(By.CSS_SELECTOR, ".tab_tab__1SPyG.tab_tab_type_current__2BEPc")
        assert "Булки" in active_tab.text, "Раздел 'Булки' не активирован"

    def test_sauces_section(self, driver, base_url):
        """Проверка перехода в раздел 'Соусы'"""
        driver.get(base_url)
        time.sleep(2)
        
        # Кликаем на раздел Соусы
        driver.find_element(By.XPATH, "//span[text()='Соусы']").click()
        time.sleep(1)
        
        # Проверяем активность раздела
        active_tab = driver.find_element(By.CSS_SELECTOR, ".tab_tab__1SPyG.tab_tab_type_current__2BEPc")
        assert "Соусы" in active_tab.text, "Раздел 'Соусы' не активирован"

    def test_toppings_section(self, driver, base_url):
        """Проверка перехода в раздел 'Начинки'"""
        driver.get(base_url)
        time.sleep(2)
        
        # Кликаем на раздел Начинки
        driver.find_element(By.XPATH, "//span[text()='Начинки']").click()
        time.sleep(1)
        
        # Проверяем активность раздела
        active_tab = driver.find_element(By.CSS_SELECTOR, ".tab_tab__1SPyG.tab_tab_type_current__2BEPc")
        assert "Начинки" in active_tab.text, "Раздел 'Начинки' не активирован"