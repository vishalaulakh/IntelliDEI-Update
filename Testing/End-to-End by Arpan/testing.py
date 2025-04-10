from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Function to animate scrolling
def smooth_scroll_to(driver, target_position, duration=2):
    current_position = driver.execute_script("return window.pageYOffset;")
    distance = target_position - current_position
    steps = 50  # Number of steps for smooth animation
    step_delay = duration / steps  # Time per step
    step_size = distance / steps  # Pixels per step

    for _ in range(steps):
        current_position += step_size
        driver.execute_script(f"window.scrollTo(0, {current_position});")
        time.sleep(step_delay)

try:
    # Step 1: Open the website
    driver.get("https://idea-toolkit.vercel.app/")
    print("Opened landing page:", driver.title)
    time.sleep(3)  # Initial pause

    # Get the full height of the page
    page_height = driver.execute_script("return document.body.scrollHeight;")

    # Animated scroll down and up on landing page
    smooth_scroll_to(driver, page_height, duration=2)  # Scroll down over 2 seconds
    print("Smoothly scrolled down on landing page")
    time.sleep(3)  # Pause at bottom

    smooth_scroll_to(driver, 0, duration=2)  # Scroll up over 2 seconds
    print("Smoothly scrolled up on landing page")
    time.sleep(3)  # Pause at top

    # Step 2: Navigate to About page
    about_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'About')]"))
    )
    about_link.click()
    print("Navigated to About page:", driver.current_url)
    time.sleep(3)  # Pause

    # Animated scroll on About page
    page_height = driver.execute_script("return document.body.scrollHeight;")
    smooth_scroll_to(driver, page_height, duration=2)
    print("Smoothly scrolled down on About page")
    time.sleep(3)  # Pause

    smooth_scroll_to(driver, 0, duration=2)
    print("Smoothly scrolled up on About page")
    time.sleep(3)  # Pause

    # Step 3: Navigate to DEI page
    driver.get("https://idea-toolkit.vercel.app/")  # Back to home
    dei_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'DEI')]"))
    )
    dei_link.click()
    print("Navigated to DEI page:", driver.current_url)
    time.sleep(3)  # Pause

    # Animated scroll on DEI page
    page_height = driver.execute_script("return document.body.scrollHeight;")
    smooth_scroll_to(driver, page_height, duration=2)
    print("Smoothly scrolled down on DEI page")
    time.sleep(3)  # Pause

    smooth_scroll_to(driver, 0, duration=2)
    print("Smoothly scrolled up on DEI page")
    time.sleep(3)  # Pause

    # Step 4: Navigate to Blog page
    driver.get("https://idea-toolkit.vercel.app/")  # Back to home
    blog_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Blog')]"))
    )
    blog_link.click()
    print("Navigated to Blog page:", driver.current_url)
    time.sleep(3)  # Pause

    # Animated scroll on Blog page
    page_height = driver.execute_script("return document.body.scrollHeight;")
    smooth_scroll_to(driver, page_height, duration=2)
    print("Smoothly scrolled down on Blog page")
    time.sleep(3)  # Pause

    smooth_scroll_to(driver, 0, duration=2)
    print("Smoothly scrolled up on Blog page")
    time.sleep(3)  # Pause

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    time.sleep(2)  # Final pause
    driver.quit()