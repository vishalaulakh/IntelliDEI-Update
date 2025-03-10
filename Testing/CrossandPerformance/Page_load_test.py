from selenium import webdriver
import time

# Browsers to test
browsers = {
    "Chrome": webdriver.Chrome,
    "Firefox": webdriver.Firefox,
    "Edge": webdriver.Edge
}

# Base URL of the site and pages to test
base_url = "https://idea-toolkit.vercel.app/"
pages = ["home", "about", "DEI", "blog", "login"]  # Only testing Home, About DEI, Blog, and Login pages

def test_page_load(browser_name, driver):
    """Test page load time for each page."""
    print(f"Testing on {browser_name}...")
    for page in pages:
        url = f"{base_url}{page}"
        start_time = time.time()  # Start timer
        driver.get(url)  # Load the page
        time_taken = time.time() - start_time  # Calculate time taken
        print(f"{url} loaded in {time_taken:.2f} seconds")
        time.sleep(2)  # Wait before loading the next page

def run_tests():
    """Run the page load test on all browsers."""
    for browser_name, browser in browsers.items():
        print(f"Starting tests on {browser_name}...")
        driver = browser()  # Initialize the browser driver
        test_page_load(browser_name, driver)  # Run the page load test
        driver.quit()  # Close the browser after testing

    print("Page Load Testing complete.")

# Run the tests
if __name__ == "__main__":
    run_tests()
