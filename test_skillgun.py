from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

def test_skillgun_login():
    driver.get('http://skillgun.com')
    time.sleep(5)
    mobile = driver.find_element(By.NAME, 'ctl00$ContentPlaceHolder1$tbPhoneNumber')
    mobile.send_keys('6302483639')
    time.sleep(5)
    email = driver.find_element(By.ID, 'ContentPlaceHolder1_tbEmail')
    email.send_keys('sreenivasulupinnepalli@gmail.com')
    pw = driver.find_element(By.ID, 'ContentPlaceHolder1_tbPassword')
    pw.send_keys('Sreenu@8242')
    cb = driver.find_element(By.ID, 'ckbkPolicyAgreement')
    cb.click()
    time.sleep(10)
    login = driver.find_element(By.NAME, 'ctl00$ContentPlaceHolder1$btnLogin')
    login.click()
    time.sleep(5)
    assert 'Home' in driver.current_url

def test_skillgun_profile_settings():
    profile = driver.find_element(By.LINK_TEXT, 'profile settings')
    profile.click()
    time.sleep(5)
    assert 'Profile' in driver.current_url



def test_skillgun_edit_contacts():
    editcontact = driver.find_element(By.ID, 'ContentPlaceHolder1_hlEditContact')
    editcontact.click()
    time.sleep(5)
    assert 'EditContactDetails' in driver.current_url
def test_skillgun_profile_save_contacts():
    radio = driver.find_element(By.ID, 'ContentPlaceHolder1_RadioButtonList1_0')
    radio.click()
    per_city = driver.find_element(By.ID,'ContentPlaceHolder1_tbPACity')
    per_city.clear()
    per_city.send_keys('palamaneru')
    time.sleep(5)
    per_state = driver.find_element(By.ID,'ContentPlaceHolder1_ddlPAState')
    time.sleep(5)
    per_state.send_keys('Bihar')
    time.sleep(5)
    savecontact = driver.find_element(By.ID,'ContentPlaceHolder1_btnSubmit')
    savecontact.click()
    time.sleep(5)
    success = driver.find_element(By.ID,'ContentPlaceHolder1_pmsg')
    assert success.text == 'Contact Details Updated Successfully'


    driver.close()

