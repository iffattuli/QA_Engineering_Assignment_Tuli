# Automated Testing for SmartCare Pro
c,
## Description
This project aims to automate testing for a healthcare management system named SmartCare Pro using Selenium WebDriver and Python. The automated tests cover functionalities like user authentication, patient data manipulation, file import and error handling scenarios.

## Technologies Used
- Selenium WebDriver
- Python
- unittest framework
## How to Run
1. Clone this repository to your local machine.
2. Install Python if you haven't already.
3. Install the selenium if you haven't already.
4. Run automatedataupload.py, testuserauthentication.py, datamanipulation_change_surname.py, errorhandling_invalid_input_field.py, fileformats.py separately.
   
## Automated Testing:
1. Automated Data Upload:
   This Selenium test script named ‘automatedataupload.py’ automates the process of logging into a web application, selecting a province, district, and facility, entering patient details, and uploading a sample 
   medical dataset.
   -Prerequisites: Python installed
                  Selenium library (‘pip install selenium’)
                  Chromedriver installed and added to path
  
   -Usage: Please run the script from the terminal: python automatedataupload.py
  
   -Script Structure:
    initialize_driver(): Initialize WebDriver for Chrome.
    login(driver, username, password): Log in to the web application.
    select_province(driver, province_name): Select a province from the dropdown.
    select_district(driver, district_name): Select a district from the dropdown.
    select_facility(driver, facility_name): Select a facility from the dropdown.
    click_enter_button(driver): Click the "Enter" button.
    click_nrc_button(driver): Click the "NRC" button.
    enter_nrc_value(driver, nrc_value): Enter NRC value.
    click_attend_to_patient_button(driver): Click "Attend to Patient" button.
    click_image_element(driver): Click on an image element.
    vital_button(driver): Click on the "Vital" button.
    addvital_button(driver): Click on the "Add Vital" button.
    upload_sample_dataset(driver, dataset_path): Upload a sample medical dataset.

2. Test User Authentication:
   This Selenium test suite named ‘testuserauthentication.py’  verifies user authentication functionality on a web application. It includes test cases for valid and invalid login scenarios.

   -Usage: Please run the script from the terminal: python ‘testuserauthentication.py

   -Test Cases:
       test_valid_login:
          - This test case verifies successful login with valid credentials.
       test_invalid_username:
          - This test case verifies login failure with an invalid username.
          - It enters an invalid username and a correct password, then checks for the error   message.
       test_invalid_password:
          - This test case verifies login failure with an invalid password.
          - It enters a valid username and an invalid password, then checks for the error message.
       test_invalid_usernamepassword:
          - This test case verifies login failure with both an invalid username and password.
          - It enters invalid credentials and checks for the error message.

3. Data Manipulation:
   This Selenium test suite ‘datamanipulation_change_surname.py’  automates the process of editing a patient’s profile on the SmartCarePro web application. It includes methods to handle login, dropdown 
   selections, and form submissions, with a primary test case to verify profile data manipulation. It changes the surname of the person from ‘Don’ to ‘Donut’.

   -Usage: Please run the script from the terminal: python datamanipulation_change_surname.py

   -Test Case:
         test_edit_patient_profile:
            - Logs in with valid credentials.
            - Selects the province, district, and facility from dropdown menus.
            - Navigates to the patient's profile, edits the surname, and submits the changes.
            - Asserts that the profile is updated successfully by checking for a success message.

    -Test Flow:
             Login: The test logs in using valid credentials.
             Select Location: The test selects the province, district, and facility from dropdown menus.
             Edit Profile: The test navigates to the patient's profile, edits the surname field, and submits the form.
             Verify Update: The test checks for a success message to verify that the profile was updated successfully.
   
4. Invalid Input Field Error Handling:
   This is designed to automate error handling for invalid NRC inputs on the SmartCarePro web application. It also includes methods for logging in, selecting dropdown options. It simply checks whether the NRC 
   input field allows any input with a length of less than 9. It also checks for an error message indicating the invalid input format. There was no error message for any invalid input in this field.

## File Import with Form Field Testing:
1. Testing the functionality of file import for patient records, ensuring compatibility with various file formats:
   The fileformats.py focuses on testing the functionality of file import for patient records and validating form fields. Here, I tested it with a ‘.xlxs’ file, and the test result is that the web app doesn’t 
   support a ‘.xlxs’ file for filling out the forms. So the error message “Error adding vital” was displayed. The ‘.xlxs’ file is attached to the github file named ‘testfileformat.xlxs’. However, the web app is 
   perfect for the ‘.csv’ file format, which is already tested. Otherwise, the data could not be uploaded from the ‘Sample Dataset.csv’ file.



   [QA Engineering Assignment Documentation by Khandaker Iffat Jahan Tuli_updated.pdf](https://github.com/iffattuli/QA_Engineering_Assignment_Tuli/files/15458773/QA.Engineering.Assignment.Documentation.by.Khandaker.Iffat.Jahan.Tuli_updated.pdf)






## Test Coverage
- User Authentication
- Patient Data Manipulation
- Error Handling
- File import with form field testing

## Future Work
- Add additional test cases to increase coverage.
- Enhance error handling scenarios.
- Proceed with performance and security testing.
