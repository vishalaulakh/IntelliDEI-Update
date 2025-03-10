import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup Selenium WebDriver (using Chrome)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

try:
    # Test Case 1: Home Page UI
    print("Testing Home Page UI...")
    driver.get("https://idea-toolkit.vercel.app/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    nav = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "nav"))
    )
    assert nav.is_displayed(), "Navigation bar not visible on Home Page"
    print("Navigation bar is visible")

    logo = driver.find_element(By.XPATH, "//img[@alt='Logo']")
    assert logo.is_displayed(), "Logo not visible on Home Page"
    print("Logo is visible")

    login_btn = driver.find_element(By.XPATH, "//button[contains(@class, 'bg-blue-700')]")
    assert login_btn.is_displayed() and login_btn.is_enabled(), "Login button not visible or clickable"
    print("Login button is visible and clickable")

    # Test Case 2: Signup Page UI
    print("Testing Signup Page UI...")
    driver.get("https://idea-toolkit.vercel.app/signup")

    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    assert email_input.is_displayed(), "Email input not visible on Signup Page"
    print("Email input is visible")

    password_input = driver.find_element(By.ID, "password")
    assert password_input.is_displayed(), "Password input not visible on Signup Page"
    print("Password input is visible")

    confirm_password_input = driver.find_element(By.ID, "confirmPassword")
    assert confirm_password_input.is_displayed(), "Confirm Password input not visible on Signup Page"
    print("Confirm Password input is visible")

    signup_btn = driver.find_element(By.XPATH, "//button[contains(@class, 'bg-indigo-500')]")
    assert signup_btn.is_displayed() and signup_btn.is_enabled(), "Signup button not clickable"
    print("Signup button is visible and clickable")

    # Fixed Google button check
    google_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'bg-white') and contains(., 'Continue with Google')]"))
    )
    assert google_btn.is_displayed() and google_btn.is_enabled(), "Google sign-in button not clickable"
    print("Google sign-in button is visible and clickable")

    login_link = driver.find_element(By.XPATH, "//a[@href='/login']")
    assert login_link.is_displayed(), "Login link not visible on Signup Page"
    print("Login link is visible")

    # Test Case 3: Login Page UI
    print("Testing Login Page UI...")
    driver.get("https://idea-toolkit.vercel.app/login")

    login_email = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    assert login_email.is_displayed(), "Email input not visible on Login Page"
    print("Email input is visible")

    login_password = driver.find_element(By.ID, "password")
    assert login_password.is_displayed(), "Password input not visible on Login Page"
    print("Password input is visible")

    signin_btn = driver.find_element(By.XPATH, "//button[contains(@class, 'from-indigo-500')]")
    assert signin_btn.is_displayed() and signin_btn.is_enabled(), "Sign-in button not clickable"
    print("Sign-in button is visible and clickable")

    google_login_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'bg-white') and contains(., 'Continue with Google')]"))
    )
    assert google_login_btn.is_displayed() and google_login_btn.is_enabled(), "Google sign-in button not clickable"
    print("Google sign-in button is visible and clickable")

    forgot_pwd = driver.find_element(By.CLASS_NAME, "text-indigo-300")
    assert forgot_pwd.is_displayed(), "Forgot Password button not visible on Login Page"
    print("Forgot Password button is visible")

    signup_link = driver.find_element(By.XPATH, "//a[@href='/signup']")
    assert signup_link.is_displayed(), "Signup link not visible on Login Page"
    print("Signup link is visible")

    print("All UI tests passed!")

except Exception as e:
    print(f"UI Test Failed: {str(e)}")

finally:
    time.sleep(2)
    driver.quit()