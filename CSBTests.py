from playwright.sync_api import sync_playwright
import pandas as pd


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
   "END_DATE": "01/01/2021",
   "FULL_TIME": "Y",
   "PART_TIME": "N",
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
# create empty dataframe
df = pd.DataFrame(columns=columns)


# add rows
df = df.append(JOB_1, ignore_index=True)
df = df.append(JOB_2, ignore_index=True)


def run(playwright):
    # Launch the browser
    browser = playwright.chromium.launch(headless=False)  # Set headless=True for headless mode
    context = browser.new_context()
    page = context.new_page()

    # Navigate to the desired URL
    page.goto(APPLICATION_LINK)  # Replace with your target URL
    
    # Wait for the page to load
    page.wait_for_load_state('load')
    
    # Locate the "continue" button by its ID and click it
    page.click('#continue')
    
    # PAGE TWO
    # Wait for the page to load
    page.wait_for_load_state('load')

    # Locate the checkbox by its ID and click it
    checkbox = page.locator('#label-16')  # Using ID selector
    checkbox.click()  # This checks the checkbox
    
    # Locate the "confirm" button by its ID and click it
    page.click('#confirmButton')
    
    # PAGE THREE
    # Wait for the page to load
    page.wait_for_load_state('load')
    
    page.click('#idButtonProceed')

    
    # START FILLING FORM
    # Wait for the page to load
    page.wait_for_load_state('load')
    
    # Fill the form
    # page.fill('#idhkid0', USER_INPUTS["HKID"][0])  
    # page.fill('#idhkid1', USER_INPUTS["HKID"][1]) 
    # page.fill('#idhkid2', USER_INPUTS["HKID"][2])
    page.fill('#idpassport', USER_INPUTS["PASSPORT"])
    page.fill('#emailFile', USER_INPUTS["EMAIL"])
    page.fill('#idEmail02', USER_INPUTS["EMAIL"])
    page.fill('#idPin', USER_INPUTS["PIN"])
    page.fill('#idPin02', USER_INPUTS["PIN"])
    page.fill('#remindLabel', USER_INPUTS["PIN_REMINDER"])
    
    # Click the "continue" button idButtonContinue
    page.click('#idButtonContinue')
    
    # NEW PAGE
    # Wait for the page to load
    page.wait_for_load_state('load')
    
    # Click the "continue" button idButtonContinue
    page.click('#idButtonContinue')
    
    # NEW PAGE
    # Wait for the page to load
    page.wait_for_load_state('load')
    
    # Fill surname gf340from_field_name
    page.fill('#gf340from_field_name', USER_INPUTS["ENGLISH_SURNAME"])
    # Fill given name gf340from_field_name2
    page.fill('#gf340from_field_name2', USER_INPUTS["ENGLISH_GIVEN_NAME"])
    # Fill DOB dob0
    page.fill('#dob0', USER_INPUTS["DOB_DAY"])
    page.fill('#dob1', USER_INPUTS["DOB_MONTH"])
    page.fill('#dob2', USER_INPUTS["DOB_YEAR"])
    # Fill passport issuing authority
    page.fill('#IssuingAuthority0', USER_INPUTS["PASSPORT_ISSUING_AUTHORITY"])
    
    # Click gender gf340from_field_sexM or gf340from_field_sexF
    if USER_INPUTS["GENDER"] == "M":
        page.click('#gf340from_field_sexM')
    elif USER_INPUTS["GENDER"] == "F":
        page.click('#gf340from_field_sexF')
        
    page.select_option('#dobplace', USER_INPUTS["PLACE_OF_BIRTH"])
    
    # click permanent resident gf340from_field_permresY or gf340from_field_permresN
    if USER_INPUTS["PERMANENT_RESIDENT"] == "Y":
        page.click('#gf340from_field_permresY')
    elif USER_INPUTS["PERMANENT_RESIDENT"] == "N":
        page.click('#gf340from_field_permresN')
        
    # Fill residential address in gf340from_field_radd1 and gf340from_field_radd2
    page.fill('#gf340from_field_radd1', USER_INPUTS["RESIDENTIAL_ADDRESS"])
    
    # Choose district from dropdown sradd3
    page.select_option('#sradd3', USER_INPUTS["RESIDENTIAL_ADDRESS_DISTRICT"])
    # page.fill('#field.radd3', USER_INPUTS["RESIDENTIAL_ADDRESS_DISTRICT"])
    
    # click guilty of offence gf340from_field_guilty-1 or gf340from_field_guilty-2 
    if USER_INPUTS["GUILTY_OF_OFFENCE"] == "Y":
        page.click('#gf340from_field_guilty-1')
    elif USER_INPUTS["GUILTY_OF_OFFENCE"] == "N":
        page.click('#gf340from_field_guilty-2')
    
    # Choose country from dropdown field myraddr
    page.select_option('#myraddr', USER_INPUTS["RESIDENTIAL_ADDRESS_COUNTRY"])
    
    # Click consent field.consent
    page.click('#field\\.consent')
    # Click consent field.consentA, field.consentB
    page.click('#field\\.consentA')
    page.click('#field\\.consentB')
    
    # Fill mobile number gf340from_field_tele1
    page.fill('#gf340from_field_tele1', USER_INPUTS["MOBILE_NUMBER"])
    
    # Submit with confirmButton
    page.click('#confirmButton.btn_mouseout_red')
    
    # COMMENT OUT TO AVOID ACTUAL REQUESTS Submit with submitButton
    # page.click('#submitButton')
    
    # EMPLOYMENT HISTORY
    # Goal: Identify all the possible errors. This is a rich source of errors (and also where the value is).
    
    # Dates: DateForm0, DateEmpoto0, DateForm1, DateEmpoto1, ...
    # Employer: empfirm0, empfirm1, ...
    # Position: emppos0, emppos1, ...
    # Nature of Work: empnature0, empnature1, ...
    # Full time checkbox: emptype0-1, emptype1-1, ...
    # Part time checkbox: emptype10-1, emptype11-1, ...
    
    
    
    
    # Optional: Wait to see the result
    page.wait_for_timeout(200000)  # Wait for 200 seconds

with sync_playwright() as playwright:
    run(playwright)