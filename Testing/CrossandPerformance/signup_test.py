from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.alert import Alert
import time

# Initialize WebDriver for Chrome and Firefox
def init_driver(browser="chrome"):
    if browser == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode (optional)
        driver = webdriver.Chrome(service=Service("path/to/chromedriver"), options=chrome_options)
    elif browser == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--headless")  # Run in headless mode (optional)
        driver = webdriver.Firefox(service=FirefoxService("path/to/geckodriver"), options=firefox_options)
    else:
        raise ValueError("Unsupported browser")
    return driver

# Function to test signup
def test_signup(driver, email, password, weak_password=False):
    driver.get("http://localhost:3000/signup")  # Replace with the correct URL

    # Wait for the page to load
    time.sleep(3)

    # Find form elements
    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")
    confirm_password_input = driver.find_element(By.ID, "confirmPassword")
    signup_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    # Fill in email and password
    email_input.send_keys(email)
    password_input.send_keys(password)
    confirm_password_input.send_keys(password)

    # Click signup button
    signup_button.click()

    # Wait for the form submission and page to load
    time.sleep(3)

    try:
        # Check for success or error message
        alert = Alert(driver)
        alert_message = alert.text
        print(f"Alert message: {alert_message}")
        alert.accept()

        # Check if signup is successful or not
        if "Verification email sent" in alert_message or "Account created" in alert_message:
            print("Signup successful!")
        else:
            print("Signup failed!")

    except Exception as e:
        print(f"Error: {e}")
        print("No alert found, checking for error message on the page.")

        # Check for error messages directly in the page
        error_message = driver.find_element(By.CLASS_NAME, "text-red-500")
        print(f"Error message on the page: {error_message.text}")

# Test with a valid password
print("Testing signup with valid password")
valid_email = "vishalsingh@trentu.ca"
valid_password = "123@Vishal"
driver = init_driver("chrome")  # You can change "chrome" to "firefox"
test_signup(driver, valid_email, valid_password)

# Test with a weak password
print("\nTesting signup with weak password")
weak_password = "123"
test_signup(driver, valid_email, weak_password)

# Close the browser
driver.quit()
