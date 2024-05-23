import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUserAuthentication(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Initialize WebDriver
        self.driver.maximize_window()  # Maximize browser window
        self.driver.get("https://carepro-training.ihmafrica.com/")  # Open login page

    def tearDown(self):
        self.driver.quit()  # Close WebDriver after each test

    def test_valid_login(self):
        # Enter valid username and pass
        self.login("tester", "tester2023!")
        # Assert that successful login redirects to the dashboard
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Dashboard')]")))

    def test_invalid_username(self):
        # Enter invalid username and correct pass
        self.login("xyz", "tester2023!")
        error_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "error-message"))).text
        self.assertIn("Invalid username", error_message)

    def test_invalid_password(self):
        # Enter valid username and invalid password and attempt login
        self.login("tester", "12345")
        error_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "error-message"))).text
        self.assertIn("Invalid password", error_message)

    def test_account_lockout(self):
        # Attempt login with invalid credentials multiple times 
        for _ in range(5):
            self.login("fenkj", "fekj")
        error_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "error-message"))).text
        self.assertIn("Account locked", error_message)

    def login(self, username, password):
        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "username")))
        username_field.send_keys(username)
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
        password_field.send_keys(password)
        password_field.send_keys(Keys.ENTER)

if __name__ == "__main__":
    unittest.main()
