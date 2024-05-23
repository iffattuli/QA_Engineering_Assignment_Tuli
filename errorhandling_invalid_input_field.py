import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

class TestErrorHandling(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Initialize WebDriver
        self.driver.maximize_window()  # Maximize browser window
        self.driver.get("https://carepro-training.ihmafrica.com/")  # Open login page

    def tearDown(self):
        self.driver.quit()  # Close WebDriver after each test

    def login(self, username, password):
        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "username")))
        username_field.send_keys(username)
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
        password_field.send_keys(password)
        password_field.send_keys(Keys.ENTER)
        time.sleep(3) 

    def select_dropdown_option(self, selector, option_text):
        try:
            dropdown = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
            dropdown.click()
            select = Select(dropdown)
            options = [option.text for option in select.options]
            print(f"Available options: {options}")

            try:
                select.select_by_visible_text(option_text)
                print(f"Option '{option_text}' selected successfully.")
            except NoSuchElementException:
                self.driver.execute_script(f"document.querySelector('{selector}').value = '{option_text}';")
                print(f"Option '{option_text}' selected successfully using JavaScript injection.")
        except TimeoutException:
            print(f"Timeout: Dropdown element with selector '{selector}' not found.")

    def select_province(self, province_name):
        self.select_dropdown_option('select.custom-input[placeholder="Enter Province"]', province_name)
        time.sleep(3) 

    def select_district(self, district_name):
        # Wait a few seconds to ensure the district dropdown is populated after selecting the province
        time.sleep(5)
        self.select_dropdown_option('select.custom-input[placeholder="Enter District"]', district_name)
        time.sleep(3)  

    def select_facility(self, facility_name):
        facility_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Search facility"]'))
        )
        facility_input.send_keys(facility_name)
        time.sleep(2)  

        facility_suggestion = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class, 'cursor-pointer') and text()='{facility_name}']"))
        )
        facility_suggestion.click()

        time.sleep(2)
        entered_facility = facility_input.get_attribute("value")
        print(f"Entered facility: {entered_facility}")

        assert entered_facility == facility_name, f"Facility not entered correctly. Entered: {entered_facility}"
        time.sleep(3) 

    def click_enter_button(self):
        click_enter = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "button"))
        )
        click_enter.click()
        time.sleep(3)

    def click_nrc_button(self):
        nrc_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='NRC']"))
        )
        nrc_button.click()
        time.sleep(3)  

    def test_invalid_nrc_input(self):
        # Login
        self.login("tester", "tester2023!")

        # Select province, district, and facility
        self.select_province("Lusaka")
        self.select_district("Lusaka")
        self.select_facility("Dr. Watson Dental Clinic")

        # Click on Enter button
        self.click_enter_button()

        # Click on NRC button
        self.click_nrc_button()

        # Enter alphabetic characters into NRC value input field
        nrc_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "nrc"))
        )
        nrc_input.send_keys("InvalidNRC", Keys.ENTER)

        # Wait for a brief moment to allow the system to process the input
        time.sleep(2)

        # Check if there is any error message displayed
        error_message = self.driver.find_elements(By.CLASS_NAME, "error-message")

        # Assert that an error message is displayed indicating the invalid input format
        self.assertTrue(error_message, "No error message displayed for invalid NRC input format")

if __name__ == "__main__":
    unittest.main() 