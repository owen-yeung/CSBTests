# from playwright.sync_api import sync_playwright
import pandas as pd



def run(playwright, employment_history, application_link, user_inputs):
    # Launch the browser
    browser = playwright.chromium.launch(headless=False)  # Set headless=True for headless mode
    context = browser.new_context()
    page = context.new_page()

    # Navigate to the desired URL
    page.goto(application_link)  # Replace with your target URL
    
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
    # page.fill('#idhkid0', user_inputs["HKID"][0])  
    # page.fill('#idhkid1', user_inputs["HKID"][1]) 
    # page.fill('#idhkid2', user_inputs["HKID"][2])
    page.fill('#idpassport', user_inputs["PASSPORT"])
    page.fill('#emailFile', user_inputs["EMAIL"])
    page.fill('#idEmail02', user_inputs["EMAIL"])
    page.fill('#idPin', user_inputs["PIN"])
    page.fill('#idPin02', user_inputs["PIN"])
    page.fill('#remindLabel', user_inputs["PIN_REMINDER"])
    
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
    page.fill('#gf340from_field_name', user_inputs["ENGLISH_SURNAME"])
    # Fill given name gf340from_field_name2
    page.fill('#gf340from_field_name2', user_inputs["ENGLISH_GIVEN_NAME"])
    # Fill DOB dob0
    page.fill('#dob0', user_inputs["DOB_DAY"])
    page.fill('#dob1', user_inputs["DOB_MONTH"])
    page.fill('#dob2', user_inputs["DOB_YEAR"])
    # Fill passport issuing authority
    page.fill('#IssuingAuthority0', user_inputs["PASSPORT_ISSUING_AUTHORITY"])
    
    # Click gender gf340from_field_sexM or gf340from_field_sexF
    if user_inputs["GENDER"] == "M":
        page.click('#gf340from_field_sexM')
    elif user_inputs["GENDER"] == "F":
        page.click('#gf340from_field_sexF')
        
    page.select_option('#dobplace', user_inputs["PLACE_OF_BIRTH"])
    
    # click permanent resident gf340from_field_permresY or gf340from_field_permresN
    if user_inputs["PERMANENT_RESIDENT"] == "Y":
        page.click('#gf340from_field_permresY')
    elif user_inputs["PERMANENT_RESIDENT"] == "N":
        page.click('#gf340from_field_permresN')
        
    # Fill residential address in gf340from_field_radd1 and gf340from_field_radd2
    page.fill('#gf340from_field_radd1', user_inputs["RESIDENTIAL_ADDRESS"])
    
    # Choose district from dropdown sradd3
    page.select_option('#sradd3', user_inputs["RESIDENTIAL_ADDRESS_DISTRICT"])
    # page.fill('#field.radd3', user_inputs["RESIDENTIAL_ADDRESS_DISTRICT"])
    
    # click guilty of offence gf340from_field_guilty-1 or gf340from_field_guilty-2 
    if user_inputs["GUILTY_OF_OFFENCE"] == "Y":
        page.click('#gf340from_field_guilty-1')
    elif user_inputs["GUILTY_OF_OFFENCE"] == "N":
        page.click('#gf340from_field_guilty-2')
    
    # Choose country from dropdown field myraddr
    page.select_option('#myraddr', user_inputs["RESIDENTIAL_ADDRESS_COUNTRY"])
    
    # Click consent field.consent
    page.click('#field\\.consent')
    # Click consent field.consentA, field.consentB
    page.click('#field\\.consentA')
    page.click('#field\\.consentB')
    
    # Fill mobile number gf340from_field_tele1
    page.fill('#gf340from_field_tele1', user_inputs["MOBILE_NUMBER"])
    
    
    
    # EMPLOYMENT HISTORY
    # Goal: Identify all the possible errors. This is a rich source of errors (and also where the value is).
    
    for i in range(len(employment_history)):
        job = employment_history.iloc[i]
        # Fill employer empfirm0, empfirm1, ...
        page.fill(f'#empfirm{i}', job["EMPLOYER"])
        # Fill position emppos0, emppos1, ...
        page.fill(f'#emppos{i}', job["JOB_TITLE"])
        # Fill nature of work empnature0, empnature1, ...
        page.fill(f'#empnature{i}', job["DUTIES"])
        # wait for debug
        # page.wait_for_timeout(2000000)
        # Fill full time checkbox emptype0-1, emptype1-1, ...
        if job["FULL_TIME"] == "Y":
            page.click(f'#emptype{i}-1')
        # Fill part time checkbox emptype10-1, emptype11-1, ...
        if job["PART_TIME"] == "Y":
            page.click(f'#emptype1{i}-1')
        # Fill dates DateForm0, DateEmpto0, DateForm1, DateEmpto1, ...
        page.fill(f'#DateForm{i}', job["START_DATE"])
        page.fill(f'#DateEmpto{i}', job["END_DATE"])
        
    
    # SUBMISSION
    # Submit with confirmButton
    page.click('#confirmButton.btn_mouseout_red')
    
    # COMMENT OUT TO AVOID ACTUAL REQUESTS Submit with submitButton
    # page.click('#submitButton')
    
    
    # Optional: Wait to see the result
    page.wait_for_timeout(200000)  # Wait for 200 seconds


        
