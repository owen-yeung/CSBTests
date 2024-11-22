from playwright.sync_api import sync_playwright
import pandas as pd
import unittest
# import run from src.autofill
from src.autofill import run

APPLICATION_LINK = 'https://csboa2.csb.gov.hk/csboa/jve/JVE_002_popupCheckList.action?languageType=2&extractDto.selectNo=47155&extractDto.onlineGF340=Y'

USER_INPUTS = {
    "HKID": ["A", "123456", "7"],
    "PASSPORT": "AB1112233",
    "EMAIL": "anuajiwo@email1.io",
    "PIN": "TEST1234",
    "PIN_REMINDER": "This is a test PIN reminder",
    "ENGLISH_SURNAME": "CHAN",
    "ENGLISH_GIVEN_NAME": "TAK MING",
    "DOB_DAY": "01",
    "DOB_MONTH": "01",
    "DOB_YEAR": "1990",
    "PASSPORT_ISSUING_AUTHORITY": "HKSAR",
    "GENDER": "M",
    "PLACE_OF_BIRTH": "Hong Kong", #Dropdown
    "PERMANENT_RESIDENT": "Y",
    "RESIDENTIAL_ADDRESS": "123, Test Street, Test City, Test Country",
    "RESIDENTIAL_ADDRESS_DISTRICT": "Central and Western", #Dropdown
    "RESIDENTIAL_ADDRESS_COUNTRY": "Hong Kong", #Dropdown
    "MOBILE_NUMBER": "12345678",
    "GUILTY_OF_OFFENCE": "N",
    
}



# define columns
columns = ["EMPLOYER", "JOB_TITLE", "DUTIES", "START_DATE", "END_DATE", "FULL_TIME", "PART_TIME"]


JOB_1 = {
   "EMPLOYER": "Test Employer 1",
   "JOB_TITLE": "Test Job Title 1",
   "DUTIES": "Test Duties 1",
   "START_DATE": "01/01/2020",
   "END_DATE": "01/01/2022",
   "FULL_TIME": "N",
   "PART_TIME": "Y",
}


JOB_2 = {
   "EMPLOYER": "Test Employer 2",
   "JOB_TITLE": "Test Job Title 2",
   "DUTIES": "Test Duties 2",
   "START_DATE": "01/01/2021",
   "END_DATE": "01/01/2022",
   "FULL_TIME": "N",
   "PART_TIME": "Y",
}


        
class TestCSB(unittest.TestCase):
    def test_base(self):
        # create empty dataframe
        EMPLOYMENT_HISTORY = pd.DataFrame(columns=columns)
        # add rows
        EMPLOYMENT_HISTORY = EMPLOYMENT_HISTORY._append(JOB_1, ignore_index=True)
        EMPLOYMENT_HISTORY = EMPLOYMENT_HISTORY._append(JOB_2, ignore_index=True)
        with sync_playwright() as playwright:
            run(playwright, EMPLOYMENT_HISTORY, APPLICATION_LINK, USER_INPUTS)

if __name__ == '__main__':
    unittest.main()
