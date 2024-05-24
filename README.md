# Automated Testing for SmartCare Pro
c,
## Description
This project aims to automate testing for a healthcare management system named SmartCare Pro using Selenium WebDriver and Python. The automated tests cover functionalities like user authentication, patient data manipulation, and error handling scenarios.

## Technologies Used
- Selenium WebDriver
- Python
- unittest framework
## How to Run
1. Clone this repository to your local machine.
2. Install Python if you haven't already.
3. Install the selenium if you haven't already.
4. Run automatedataupload.py, testuserauthentication.py, datamanipulation_change_surname.py, errorhandling_invalid_input_field.py separately.
5. automatedataupload.py: Step1: username: tester, password: tester2023!, province: Lusaka, district: Lusaka, Facility: Dr. Watson Dental Clinic
                          Step2: Click on NRC, NRC number: 111111/11/1, Click on Attend to patient, Click on Vital, Click on Add Vital
                          Step3: All the fields will be uploaded automatically by fetching the information from the Sample Dataset.csv file.

## Test Coverage
- User Authentication
- Patient Data Manipulation
- Error Handling

## Future Work
- Add additional test cases to increase coverage.
- Enhance error handling scenarios.
