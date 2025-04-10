# File: login_test.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browsers = {"Chrome": webdriver.Chrome, "Firefox": webdriver.Firefox, "Edge": webdriver.Edge}
base_url = "https://idea-toolkit.vercel.app/"

def test_login(browser_name, driver):
    driver.get(f"{base_url}login")
    time.sleep(2)
    try:
        email_input = driver.find_element(By.NAME, "email")
        password_input = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
        
        email_input.send_keys("testuser@example.com")
        password_input.send_keys("password123")
        login_button.click()
        
        time.sleep(3)
        print(f"Login test on {browser_name}: SUCCESS")
    except Exception as e:
        print(f"Login test on {browser_name}: FAILED - {e}")

for browser_name, browser in browsers.items():
    driver = browser()
    test_login(browser_name, driver)
    driver.quit()
print("Login Testing complete.")
