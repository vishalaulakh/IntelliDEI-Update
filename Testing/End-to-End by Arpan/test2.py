from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("https://idea-toolkit.vercel.app/")
    time.sleep(3)

    driver.get("https://idea-toolkit.vercel.app/login")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
    time.sleep(3)

    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )

    email_input.send_keys("arpanarora333@gmail.com")
    password_input.send_keys("12341234")
    time.sleep(3)
    login_button.click()

    WebDriverWait(driver, 10).until(EC.url_contains("/dashboard"))
    time.sleep(3)

    start_assessment_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Start Assessment')]"))
    )
    start_assessment_button.click()
    time.sleep(3)

    for _ in range(4):
        options = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//button[contains(@class, 'p-4')]"))
        )
        options[2].click()
        time.sleep(3)

    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Submit Assessment')]"))
    )
    submit_button.click()
    time.sleep(3)

except Exception as e:
    print(f"An error occurred: {e}")
    print(driver.page_source[:1000])

finally:
    time.sleep(2)
    driver.quit()