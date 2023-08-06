from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


# create a new Chrome browser instance
service = Service(executable_path=r"C:\Users\gagan\Documents\python-selenium-automation\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service= service)
driver.maximize_window()

driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")

#finding logo
#driver.find_element(By.CLASS_NAME,"a-icon-logo").click()

#clicking email field
#driver.find_element(By.ID,"ap_email").click()

#clicking continue button
#driver.find_element(By.ID,"continue").click()

#clicking Conditions of use link
#driver.find_element(By.XPATH, "//a[text()='Conditions of Use']").click()

#Clicking Privacy Notice link
#driver.find_element(By.XPATH, "//a[text()='Privacy Notice']").click()

#clicking need help
#driver.find_element(By.XPATH, "//span[@class = 'a-expander-prompt']").click()

#clicking forgot password link
#driver.find_element(By.ID,"auth-fpp-link-bottom").click()

#clicking other issues link
#driver.find_element(By.ID,"ap-other-signin-issues-link").click()

#clicking create account button
#driver.find_element(By.ID,"createAccountSubmit").click()