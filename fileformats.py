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

def initialize_driver():
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver

def login(driver, username, password):
    driver.get("https://carepro-training.ihmafrica.com/")
    wait = WebDriverWait(driver, 30)
    username_login = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
    username_login.send_keys(username)
    password_login = driver.find_element(By.NAME, "password")
    password_login.send_keys(password, Keys.ENTER)

def select_dropdown_option(driver, selector, option_text):
    try:
        dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))  #dropdown menu should be clicked
        dropdown.click()
        select = Select(dropdown)
        options = [option.text for option in select.options]
        print(f"Available options: {options}")

        try:
            select.select_by_visible_text(option_text)
            print(f"Option '{option_text}' selected successfully.")
        except NoSuchElementException:
            driver.execute_script(f"document.querySelector('{selector}').value = '{option_text}';")
            print(f"Option '{option_text}' selected successfully using JavaScript injection.")
    except TimeoutException:
        print(f"Timeout: Dropdown element with selector '{selector}' not found.")

def select_province(driver, province_name):
    select_dropdown_option(driver, 'select.custom-input[placeholder="Enter Province"]', province_name)

def select_district(driver, district_name):
    # Wait for 5 seconds to ensure the district dropdown is populated after selecting the province
    time.sleep(5)
    select_dropdown_option(driver, 'select.custom-input[placeholder="Enter District"]', district_name)

def select_facility(driver, facility_name):
    # Wait for the facility input to be visible on the screen
    facility_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Search facility"]'))
    )
    facility_input.send_keys(facility_name)
    time.sleep(2)  

    
    facility_suggestion = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class, 'cursor-pointer') and text()='{facility_name}']"))
    )
    facility_suggestion.click()

    # Verify the entered facility
    time.sleep(2)
    entered_facility = facility_input.get_attribute("value")
    print(f"Entered facility: {entered_facility}")

    assert entered_facility == facility_name, f"Facility not entered correctly. Entered: {entered_facility}"

def click_enter_button(driver):
    click_enter = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "button"))
    )
    click_enter.click()
    time.sleep(3)

def click_nrc_button(driver):
    nrc_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='NRC']"))
    )
    nrc_button.click()

def enter_nrc_value(driver, nrc_value):
    nrc_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "nrc"))
    )
    nrc_input.send_keys(nrc_value, Keys.ENTER)

def click_attend_to_patient_button(driver):
    attend_to_patient_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Attend to Patient']"))
    )
    attend_to_patient_button.click()

def click_image_element(driver):
    time.sleep(5)
    image_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='flex flex-col rounded-lg justify-center items-center gap-3 border !border-primaryColor h-[80px] w-[80px] 2xl:h-[120px] 2xl:w-[120px] hover:bg-primaryColor group transition-all duration-300 ']/img"))
    )
    image_element.click()

def vital_button(driver):
    vital = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Vital')]"))
    )
    vital.click()

def addvital_button(driver):
    addvital = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Add Vital')]"))
    )
    addvital.click()

def read_file_data(file_path):
    try:
        if file_path.endswith('.csv'):
            data = pd.read_csv(file_path)
        elif file_path.endswith('.xlsx'):
            data = pd.read_excel(file_path)
        else:
            raise ValueError("Unsupported file format")
        return data
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def fill_form_fields(driver, data):
    for index, row in data.iterrows():
        try:
            weight_input = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.NAME, "weight"))
            )
            height_input = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.NAME, "height"))
            )
            temperature_input = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.NAME, "temperature"))
            )
            systolic_input = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.NAME, "systolic"))
            )
            diastolic_input = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.NAME, "diastolic"))
            )
            pulserate_input = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.NAME, "pulseRate"))
            )
            respiratoryrate_input = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.NAME, "respiratoryRate"))
            )
            oxygensaturation_input = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.NAME, "oxygenSaturation"))
            )

            height_input.click()
            height_input.send_keys(Keys.BACKSPACE * 6)

            weight_input.clear()
            height_input.clear()
            temperature_input.clear()
            systolic_input.clear()
            diastolic_input.clear()
            pulserate_input.clear()
            respiratoryrate_input.clear()
            oxygensaturation_input.clear()

            weight_input.send_keys(str(row["Weight"]))
            height_input.send_keys(str(row["Height"]))
            temperature_input.send_keys(str(row["Temperature"]))
            systolic_input.send_keys(str(row["Systolic"]))
            diastolic_input.send_keys(str(row["Diastolic"]))
            pulserate_input.send_keys(str(row["Pulse Rate"]))
            respiratoryrate_input.send_keys(str(row["Respiratory Rate"]))
            oxygensaturation_input.send_keys(str(row["Oxygen Saturation"]))

            actions = ActionChains(driver)
            hover = driver.find_element(By.XPATH, "//h3[contains(text(),'Patient Information')]")
            actions.move_to_element(hover).perform()
            time.sleep(3)

            click_anywhere = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//h3[contains(text(),'Patient Information')]"))
            )

            scrolling = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div/form/div[2]/div/button[2]")
            driver.execute_script("arguments[0].scrollIntoView();", scrolling)

            save_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div/form/div[2]/div/button[2]'))
            )
            save_button.click()
            print("Save button clicked successfully.")
            time.sleep(2)
        except Exception as e:
            print(f"Error filling form fields: {e}")

def validate_form_fields(driver, expected_data):
    try:
        weight_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "weight"))
        )
        height_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "height"))
        )
        temperature_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "temperature"))
        )
        systolic_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "systolic"))
        )
        diastolic_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "diastolic"))
        )
        pulserate_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "pulseRate"))
        )
        respiratoryrate_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "respiratoryRate"))
        )
        oxygensaturation_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "oxygenSaturation"))
        )

        assert weight_input.get_attribute("value") == str(expected_data["Weight"])
        assert height_input.get_attribute("value") == str(expected_data["Height"])
        assert temperature_input.get_attribute("value") == str(expected_data["Temperature"])
        assert systolic_input.get_attribute("value") == str(expected_data["Systolic"])
        assert diastolic_input.get_attribute("value") == str(expected_data["Diastolic"])
        assert pulserate_input.get_attribute("value") == str(expected_data["Pulse Rate"])
        assert respiratoryrate_input.get_attribute("value") == str(expected_data["Respiratory Rate"])
        assert oxygensaturation_input.get_attribute("value") == str(expected_data["Oxygen Saturation"])

        print("Validation successful: Form fields populated correctly.")

    except AssertionError as e:
        print(f"Validation failed: {e}")

    except Exception as e:
        print(f"Error validating form fields: {e}")

def main():
    driver = initialize_driver()
    try:
        username = "tester"
        password = "tester2023!"
        login(driver, username, password)
        
        select_province(driver, "Lusaka")
        select_district(driver, "Lusaka")
        select_facility(driver, "Dr. Watson Dental Clinic")
        click_enter_button(driver)
        click_nrc_button(driver)
        enter_nrc_value(driver, "111111/11/1")
        click_attend_to_patient_button(driver)
        click_image_element(driver)
        vital_button(driver)
        addvital_button(driver)

        file_path = "testfileformat.xlsx"  # Adjust the path to your file
        data = read_file_data(file_path)

        if data is not None:
            fill_form_fields(driver, data)
            validate_form_fields(driver, data.iloc[0])  # Assuming you want to validate against the first row
        else:
            print("No data to process due to file read error.")

    finally:
        time.sleep(5)
        driver.quit()

if __name__ == "__main__":
    main()
