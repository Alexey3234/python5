from selenium.webdriver.common.by import By
import time

def login(driver, base_url, test_credentials):
    driver.get(f"{base_url}login")
    time.sleep(2)
    
    driver.find_element(By.XPATH, "//input[@name='name']").send_keys(test_credentials["email"])
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys(test_credentials["password"])
    time.sleep(1)
    
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()
    time.sleep(2)