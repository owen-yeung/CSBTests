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

JOB_3 = {
    "EMPLOYER": "Test Employer 3",
    "JOB_TITLE": "Test Job Title 3",
    "DUTIES": "Test Duties 3",
    "START_DATE": "01/01/2020",
    "END_DATE": "01/01/2023",
    "FULL_TIME": "N",
    "PART_TIME": "Y",
}
        
class TestCSB(unittest.TestCase):
    def test_three_2(self):
        new_job_1_dates = {
            "START_DATE": "01/01/2021",
            "END_DATE": "01/01/2023",
        }
        new_job_2_dates = {
            "START_DATE": "01/01/2020",
            "END_DATE": "01/01/2022",
        }
        
        new_job_3_dates = {
            "START_DATE": "01/01/2019",
            "END_DATE": "01/01/2021",
        }
        
        # update job_1 dates
        NEW_JOB_1 = {**JOB_1, **new_job_1_dates}
        # update job_2 dates
        NEW_JOB_2 = {**JOB_2, **new_job_2_dates}
        # update job_3 dates
        NEW_JOB_3 = {**JOB_3, **new_job_3_dates}
        
        # create empty dataframe
        EMPLOYMENT_HISTORY = pd.DataFrame(columns=columns)
        # add rows
        EMPLOYMENT_HISTORY = EMPLOYMENT_HISTORY._append(NEW_JOB_1, ignore_index=True)
        EMPLOYMENT_HISTORY = EMPLOYMENT_HISTORY._append(NEW_JOB_2, ignore_index=True)
        EMPLOYMENT_HISTORY = EMPLOYMENT_HISTORY._append(NEW_JOB_3, ignore_index=True)
        with sync_playwright() as playwright:
            run(playwright, EMPLOYMENT_HISTORY, APPLICATION_LINK, USER_INPUTS, 
                wait=200000
                )
            
    def test_three_3(self):
        new_job_1_dates = {
            "START_DATE": "01/01/2019",
            "END_DATE": "01/01/2021",
        }
        new_job_2_dates = {
            "START_DATE": "01/01/2020",
            "END_DATE": "01/01/2022",
        }
        
        new_job_3_dates = {
            "START_DATE": "01/01/2021",
            "END_DATE": "01/01/2023",
        }
        
        # update job_1 dates
        NEW_JOB_1 = {**JOB_1, **new_job_1_dates}
        # update job_2 dates
        NEW_JOB_2 = {**JOB_2, **new_job_2_dates}
        # update job_3 dates
        NEW_JOB_3 = {**JOB_3, **new_job_3_dates}
        
        # create empty dataframe
        EMPLOYMENT_HISTORY = pd.DataFrame(columns=columns)
        # add rows
        EMPLOYMENT_HISTORY = EMPLOYMENT_HISTORY._append(NEW_JOB_1, ignore_index=True)
        EMPLOYMENT_HISTORY = EMPLOYMENT_HISTORY._append(NEW_JOB_2, ignore_index=True)
        EMPLOYMENT_HISTORY = EMPLOYMENT_HISTORY._append(NEW_JOB_3, ignore_index=True)
        with sync_playwright() as playwright:
            run(playwright, EMPLOYMENT_HISTORY, APPLICATION_LINK, USER_INPUTS, 
                wait=200000
                )
    
    def test_two_1(self):
        new_job_1_dates = {
            "START_DATE": "01/01/2020",
            "END_DATE": "01/01/2021",
        }
        new_job_2_dates = {
            "START_DATE": "01/01/2020",
            "END_DATE": "01/01/2022",
        }
        
        # update job_1 dates
        NEW_JOB_1 = {**JOB_1, **new_job_1_dates}
        # update job_2 dates
        NEW_JOB_2 = {**JOB_2, **new_job_2_dates}
        
        # create empty dataframe
        EMPLOYMENT_HISTORY = pd.DataFrame(columns=columns)
        # add rows
        EMPLOYMENT_HISTORY = EMPLOYMENT_HISTORY._append(NEW_JOB_1, ignore_index=True)
        EMPLOYMENT_HISTORY = EMPLOYMENT_HISTORY._append(NEW_JOB_2, ignore_index=True)
        with sync_playwright() as playwright:
            run(playwright, EMPLOYMENT_HISTORY, APPLICATION_LINK, USER_INPUTS,
                wait=200000
                )
            
    def test_two_2(self):
        new_job_1_dates = {
            "START_DATE": "01/01/2020",
            "END_DATE": "01/01/2022",
        }
        new_job_2_dates = {
            "START_DATE": "01/01/2020",
            "END_DATE": "01/01/2021",
        }
        
        # update job_1 dates
        NEW_JOB_1 = {**JOB_1, **new_job_1_dates}
        # update job_2 dates
        NEW_JOB_2 = {**JOB_2, **new_job_2_dates}
        
        # create empty dataframe
        EMPLOYMENT_HISTORY = pd.DataFrame(columns=columns)
        # add rows
        EMPLOYMENT_HISTORY = EMPLOYMENT_HISTORY._append(NEW_JOB_1, ignore_index=True)
        EMPLOYMENT_HISTORY = EMPLOYMENT_HISTORY._append(NEW_JOB_2, ignore_index=True)
        with sync_playwright() as playwright:
            run(playwright, EMPLOYMENT_HISTORY, APPLICATION_LINK, USER_INPUTS, 
                wait=200000
                )
            
    def test_one_future(self):
        new_job_1_dates = {
            "START_DATE": "01/01/2020",
            "END_DATE": "01/01/2030",
        }
        
        # update job_1 dates
        NEW_JOB_1 = {**JOB_1, **new_job_1_dates}
        
        # create empty dataframe
        EMPLOYMENT_HISTORY = pd.DataFrame(columns=columns)
        # add rows
        EMPLOYMENT_HISTORY = EMPLOYMENT_HISTORY._append(NEW_JOB_1, ignore_index=True)
        # EMPLOYMENT_HISTORY = EMPLOYMENT_HISTORY._append(NEW_JOB_2, ignore_index=True)
        with sync_playwright() as playwright:
            run(playwright, EMPLOYMENT_HISTORY, APPLICATION_LINK, USER_INPUTS, 
                wait=200000
                )
            
    def test_one_part_and_full_time(self):
        new_job_1 = {
            "PART_TIME": "Y",
            "FULL_TIME": "Y",
        }
        
        # update job_1 dates
        NEW_JOB_1 = {**JOB_1, **new_job_1}
        
        # create empty dataframe
        EMPLOYMENT_HISTORY = pd.DataFrame(columns=columns)
        # add rows
        EMPLOYMENT_HISTORY = EMPLOYMENT_HISTORY._append(NEW_JOB_1, ignore_index=True)
        # EMPLOYMENT_HISTORY = EMPLOYMENT_HISTORY._append(NEW_JOB_2, ignore_index=True)
        with sync_playwright() as playwright:
            run(playwright, EMPLOYMENT_HISTORY, APPLICATION_LINK, USER_INPUTS, 
                wait=200000
                )
            
            
    def test_one_blank_ongoing(self):
        new_job_1 = {
            "END_DATE": "",
        }
        
        # update job_1 dates
        NEW_JOB_1 = {**JOB_1, **new_job_1}
        
        # create empty dataframe
        EMPLOYMENT_HISTORY = pd.DataFrame(columns=columns)
        # add rows
        EMPLOYMENT_HISTORY = EMPLOYMENT_HISTORY._append(NEW_JOB_1, ignore_index=True)
        # EMPLOYMENT_HISTORY = EMPLOYMENT_HISTORY._append(NEW_JOB_2, ignore_index=True)
        with sync_playwright() as playwright:
            run(playwright, EMPLOYMENT_HISTORY, APPLICATION_LINK, USER_INPUTS, 
                wait=200000
                )
            
    def test_invalid_date(self):
        new_job_1 = {
            "END_DATE": "31/02/2028",
        }
        
        # update job_1 dates
        NEW_JOB_1 = {**JOB_1, **new_job_1}
        
        # create empty dataframe
        EMPLOYMENT_HISTORY = pd.DataFrame(columns=columns)
        # add rows
        EMPLOYMENT_HISTORY = EMPLOYMENT_HISTORY._append(NEW_JOB_1, ignore_index=True)
        # EMPLOYMENT_HISTORY = EMPLOYMENT_HISTORY._append(NEW_JOB_2, ignore_index=True)
        with sync_playwright() as playwright:
            run(playwright, EMPLOYMENT_HISTORY, APPLICATION_LINK, USER_INPUTS, 
                wait=200000,
                browser='webkit'
                )
            
    

if __name__ == '__main__':
    unittest.main()
