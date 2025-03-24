import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestIdeaToolkitResponsive(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.base_url = "https://idea-toolkit.vercel.app/"
        self.wait = WebDriverWait(self.driver, 15)
        self.sizes = {
            "mobile": (375, 667),
            "tablet": (768, 1024),
            "desktop": (1920, 1080)
        }

    def scroll_and_check_elements(self, elements, device, skip_hamburger=False):
        driver = self.driver
        failures = []
        for name, locator in elements.items():
            if skip_hamburger and name == "Hamburger Menu (mobile)":
                continue
            try:
                element = self.wait.until(EC.presence_of_element_located(locator))
                driver.execute_script("arguments[0].scrollIntoView(true);", element)
                time.sleep(0.5)
                is_visible = element.is_displayed()
                print(f"{device} - {name}: {is_visible}")
                if not is_visible:
                    failures.append(f"{name} not visible on {device}")
            except Exception as e:
                print(f"{device} - {name} Error: {e}")
                failures.append(f"{name} failed on {device}: {e}")
        if failures:
            raise AssertionError("\n".join(failures))

    def test_home_page_responsive(self):
        driver = self.driver
        driver.get(self.base_url + "home")

        elements = {
            "Hamburger Menu (mobile)": (By.XPATH, "//button[contains(@class, 'md:hidden')]"),
            "Nav Home Link": (By.XPATH, "//a[contains(@class, 'text-black') and contains(., 'Home')]"),
            "Hero Title": (By.XPATH, "//h1[contains(., 'Welcome')]"),
            "Explore More Button": (By.XPATH, "//button[contains(., 'Explore More')]"),
            "Features Heading": (By.XPATH, "//h2[contains(., 'Key Features')]"),
            "Reflection Process Card": (By.XPATH, "//h3[contains(., 'Reflection Process')]"),
            "Assessment Tools Card": (By.XPATH, "//h3[contains(., 'Assessment Tools')]"),
            "Annual Reporting Card": (By.XPATH, "//h3[contains(., 'Annual Reporting')]"),
            "Stats Section": (By.XPATH, "//div[contains(., 'Staff Members Engaged')]"),
            "CTA Button": (By.XPATH, "//button[contains(., 'Get Started Today')]")
        }

        for device, (width, height) in self.sizes.items():
            print(f"\nTesting Home page on {device} ({width}x{height})")
            driver.set_window_size(width, height)
            time.sleep(1)
            if device == "mobile":
                hamburger = self.wait.until(EC.element_to_be_clickable(elements["Hamburger Menu (mobile)"]))
                hamburger.click()
                time.sleep(1)
                self.scroll_and_check_elements(elements, device)
            else:
                self.scroll_and_check_elements(elements, device, skip_hamburger=True)

    def test_login_page_responsive(self):
        driver = self.driver
        driver.get(self.base_url + "login")

        elements = {
            "Hamburger Menu (mobile)": (By.XPATH, "//button[contains(@class, 'md:hidden')]"),
            "Nav Home Link": (By.XPATH, "//a[contains(@class, 'text-black') and contains(., 'Home')]"),
            "Welcome Back Title": (By.XPATH, "//h2[contains(., 'Welcome Back')]"),
            "Email Input": (By.ID, "email"),
            "Password Input": (By.ID, "password"),
            "Sign In Button": (By.XPATH, "//button[contains(@class, 'from-indigo-500') and contains(., 'Sign In')]"),
            "Forgot Password Link": (By.CLASS_NAME, "text-indigo-300"),
            "Google Sign In Button": (By.XPATH, "//button[contains(., 'Continue with Google')]"),
            "Sign Up Link": (By.XPATH, "//a[@href='/signup']")
        }

        for device, (width, height) in self.sizes.items():
            print(f"\nTesting Login page on {device} ({width}x{height})")
            driver.set_window_size(width, height)
            time.sleep(1)
            if device == "mobile":
                hamburger = self.wait.until(EC.element_to_be_clickable(elements["Hamburger Menu (mobile)"]))
                hamburger.click()
                time.sleep(1)
                self.scroll_and_check_elements(elements, device)
            else:
                self.scroll_and_check_elements(elements, device, skip_hamburger=True)

    def test_dei_page_responsive(self):
        driver = self.driver
        driver.get(self.base_url + "dei")

        elements = {
            "Hamburger Menu (mobile)": (By.XPATH, "//button[contains(@class, 'md:hidden')]"),
            "Nav DEI Link": (By.XPATH, "//a[contains(@class, 'text-black') and contains(., 'DEI')]"),
            "DEI Title": (By.XPATH, "//h1[contains(., 'Diversity')]"),
            "inclusion Section": (By.XPATH, "//h3[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'inclusion')]"),
            "Diversity Section": (By.XPATH, "//h3[contains(., 'Diversity')]"),
            "Equity Section": (By.XPATH, "//h3[contains(., 'Equity')]"),
            "Accessibility Section": (By.XPATH, "//h3[contains(., 'Accessibility')]"),
            "inclusion Framework": (By.XPATH, "//h3[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'inclusion framework')]"),  # Case-insensitive
            "Assessment Tools Framework": (By.XPATH, "//h3[contains(., 'Assessment Tools')]"),
            "Staff Support Framework": (By.XPATH, "//h3[contains(., 'Staff Support')]"),
            "CTA Button": (By.XPATH, "//button[contains(., 'Get Started with IDEA')]")
        }

        for device, (width, height) in self.sizes.items():
            print(f"\nTesting DEI page on {device} ({width}x{height})")
            driver.set_window_size(width, height)
            time.sleep(1)
            if device == "mobile":
                hamburger = self.wait.until(EC.element_to_be_clickable(elements["Hamburger Menu (mobile)"]))
                hamburger.click()
                time.sleep(1)
                self.scroll_and_check_elements(elements, device)
            else:
                self.scroll_and_check_elements(elements, device, skip_hamburger=True)

    def test_blog_page_responsive(self):
        driver = self.driver
        driver.get(self.base_url + "blog")

        elements = {
            "Hamburger Menu (mobile)": (By.XPATH, "//button[contains(@class, 'md:hidden')]"),
            "Nav Blog Link": (By.XPATH, "//a[contains(@class, 'text-black') and contains(., 'Blog')]"),
            "Blog Title": (By.XPATH, "//h1[contains(., 'Our Blog')]"),
            "Category All Button": (By.XPATH, "//button[contains(., 'All')]"),
            "Category Local Button": (By.XPATH, "//button[contains(., 'Local')]"),
            "Blog Post Title": (By.XPATH, "//h2[contains(., 'Discovering Peterborough')]"),
            "Read More Button": (By.XPATH, "//button[contains(., 'Read More')]"),
            "Newsletter Heading": (By.XPATH, "//h2[contains(., 'Stay Updated')]"),
            "Subscribe Input": (By.XPATH, "//input[@placeholder='Enter your email']"),
            "Subscribe Button": (By.XPATH, "//button[contains(., 'Subscribe')]")
        }

        for device, (width, height) in self.sizes.items():
            print(f"\nTesting Blog page on {device} ({width}x{height})")
            driver.set_window_size(width, height)
            time.sleep(1)
            if device == "mobile":
                hamburger = self.wait.until(EC.element_to_be_clickable(elements["Hamburger Menu (mobile)"]))
                hamburger.click()
                time.sleep(1)
                self.scroll_and_check_elements(elements, device)
            else:
                self.scroll_and_check_elements(elements, device, skip_hamburger=True)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()