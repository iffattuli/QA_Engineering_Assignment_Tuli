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

class TestPatientDataManipulation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Initialize WebDriver
        self.driver.maximize_window()  # Maximize browser window
        self.driver.get("https://carepro-training.ihmafrica.com/")  # Open login page

    def tearDown(self):
        self.driver.quit()  # Close WebDriver after each test

    def login(self, username, password):
        # Find and fill username and password fields, then submit login form
        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "username")))
        username_field.send_keys(username)
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
        password_field.send_keys(password)
        password_field.send_keys(Keys.ENTER)
        time.sleep(3)  # Add delay to observe the login process

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
        time.sleep(3)  # Add delay to observe the selection

    def select_district(self, district_name):
        # Wait a few seconds to ensure the district dropdown is populated after selecting the province
        time.sleep(5)
        self.select_dropdown_option('select.custom-input[placeholder="Enter District"]', district_name)
        time.sleep(3)  # Add delay to observe the selection

    def select_facility(self, facility_name):
        # Wait for the facility input to be visible
        facility_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Search facility"]'))
        )
        facility_input.send_keys(facility_name)
        time.sleep(2)  # Wait for suggestions to appear

        # Locate the suggestion using XPath and click on it
        facility_suggestion = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class, 'cursor-pointer') and text()='{facility_name}']"))
        )
        facility_suggestion.click()

        # Verify the entered facility
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

    def enter_nrc_value(self, nrc_value):
        nrc_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "nrc"))
        )
        nrc_input.send_keys(nrc_value, Keys.ENTER)
        time.sleep(3)  

    def click_editprofile_button(self):
        editprofile_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div[3]/div/div/div/div[2]/div[2]/a'))
        )
        editprofile_button.click()
        time.sleep(3)  

    def click_edit_button(self):
        edit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[2]/div[3]/div[3]/div/div[2]/div[1]/button'))
        )
        edit_button.click()
        time.sleep(3)  

    def test_edit_patient_profile(self):
        # Login
        self.login("tester", "tester2023!")
        
        # Select province, district, and facility
        self.select_province("Lusaka")
        self.select_district("Lusaka")
        self.select_facility("Dr. Watson Dental Clinic")
        
        self.click_enter_button()
        self.click_nrc_button()
        self.enter_nrc_value("111111/11/1")
        self.click_editprofile_button()
        self.click_edit_button()
        
        # data manipulation: Update surname
        surname_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "surname")))
        surname_field.clear()
        surname_field.send_keys("Donut")
        time.sleep(3)  # Add delay to observe the data manipulation
        
        # Scroll to Next button
        next_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div[2]/form/div[3]/div/button[2]'))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
        next_button.click()
        # Scroll to Next button for next page
        next_button1 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div[2]/form/div[2]/div/button[2]'))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", next_button1)
        next_button1.click()

        # Scroll to Next button for next page
        next_button2 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div[2]/form/div[4]/div/button[2]'))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", next_button2)
        next_button2.click()

        submit = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div[2]/form/div[2]/div/button[2]'))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit)
        submit.click()

     # Assert that profile is updated successfully
        success_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "success-message"))).text
        self.assertIn("Profile updated successfully", success_message)

if __name__ == "__main__":
    unittest.main()

