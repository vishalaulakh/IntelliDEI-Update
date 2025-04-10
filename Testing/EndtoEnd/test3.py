from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Let's get started with our browser
driver = webdriver.Chrome()
driver.maximize_window()

# Handy function to make scrolling look smooth and natural
def smooth_scroll_to(driver, target_position, duration=2):
    current_position = driver.execute_script("return window.pageYOffset;")
    distance = target_position - current_position
    steps = 50  
    step_delay = duration / steps  
    step_size = distance / steps  
    for _ in range(steps):
        current_position += step_size
        driver.execute_script(f"window.scrollTo(0, {current_position});")
        time.sleep(step_delay)

try:
    # Alright, let's hit the homepage first
    driver.get("https://idea-toolkit.vercel.app/")
    print("Hey, we just landed on the homepage! Title is:", driver.title)
    time.sleep(3)  

    # Time to scroll down and up like a curious visitor
    page_height = driver.execute_script("return document.body.scrollHeight;")
    smooth_scroll_to(driver, page_height, duration=2)
    print("Smoothly scrolled all the way down the homepage")
    time.sleep(3)  

    smooth_scroll_to(driver, 0, duration=2)
    print("And now we’re back at the top of the homepage")
    time.sleep(3)

    # Let’s check out some pages: About, DEI, and Blog
    for page in ["About", "DEI", "Blog"]:
        link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//a[contains(text(), '{page}')]"))
        )
        link.click()
        print(f"Cool, we clicked '{page}' and landed here:", driver.current_url)
        time.sleep(3)

        page_height = driver.execute_script("return document.body.scrollHeight;")
        smooth_scroll_to(driver, page_height, duration=2)
        print(f"Scrolled down the {page} page nice and easy")
        time.sleep(3)

        smooth_scroll_to(driver, 0, duration=2)
        print(f"Scrolled back up on {page}, all good")
        time.sleep(3)

    # Now let’s log in and do some real stuff
    driver.get("https://idea-toolkit.vercel.app/login")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
    print("We’re on the login page now:", driver.current_url)
    time.sleep(3)

    # Filling in the login details
    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )

    email_input.send_keys("arpanarora333@gmail.com")
    password_input.send_keys("12341234")
    print("Just typed in the email and password")
    time.sleep(3)

    login_button.click()
    print("Clicked 'Sign In'—fingers crossed!")
    WebDriverWait(driver, 10).until(EC.url_contains("/dashboard"))
    print("Sweet, we’re on the Dashboard now:", driver.current_url)
    time.sleep(3)

    # Time to start the assessment
    start_assessment_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Start Assessment')]"))
    )
    start_assessment_button.click()
    print("Clicked 'Start Assessment', let’s do this!")
    time.sleep(3)

    # Answering all 4 questions—picking the third option each time
    for i in range(4):
        options = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//button[contains(@class, 'p-4')]"))
        )
        options[2].click()
        print(f"Answered question {i+1} with option 3")
        time.sleep(3)

    # Submitting the assessment
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Submit Assessment')]"))
    )
    submit_button.click()
    print("Submitted the assessment—done and dusted!")
    time.sleep(3)

except Exception as e:
    print(f"Oops, something went wrong: {e}")
    print("Here’s a peek at the page source to figure it out:")
    print(driver.page_source[:1000])

finally:
    # Wrapping up, closing the browser
    print("All done, closing the browser now!")
    time.sleep(2)
    driver.quit()