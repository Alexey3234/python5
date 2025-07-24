import pytest
from selenium.webdriver.common.by import By
import time

class TestConstructorNavigation:
    def test_buns_section(self, driver, base_url):
        driver.get(base_url)
        time.sleep(2)
        
        driver.find_element(By.XPATH, "//span[text()='Соусы']").click()
        time.sleep(1)
        
        driver.find_element(By.XPATH, "//span[text()='Булки']").click()
        time.sleep(1)
        
        active_tab = driver.find_element(By.CSS_SELECTOR, ".tab_tab__1SPyG.tab_tab_type_current__2BEPc")
        assert "Булки" in active_tab.text, "Раздел 'Булки' не активирован"

    def test_sauces_section(self, driver, base_url):
        driver.get(base_url)
        time.sleep(2)
        
        driver.find_element(By.XPATH, "//span[text()='Соусы']").click()
        time.sleep(1)
        
        active_tab = driver.find_element(By.CSS_SELECTOR, ".tab_tab__1SPyG.tab_tab_type_current__2BEPc")
        assert "Соусы" in active_tab.text, "Раздел 'Соусы' не активирован"

    def test_toppings_section(self, driver, base_url):
        driver.get(base_url)
        time.sleep(2)
        
        driver.find_element(By.XPATH, "//span[text()='Начинки']").click()
        time.sleep(1)
        
        active_tab = driver.find_element(By.CSS_SELECTOR, ".tab_tab__1SPyG.tab_tab_type_current__2BEPc")
        assert "Начинки" in active_tab.text, "Раздел 'Начинки' не активирован"