from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


# create a new Chrome browser instance
service = Service(executable_path=r"C:\Users\gagan\Documents\python-selenium-automation\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service= service)
driver.maximize_window()

driver.get("https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&ignoreAuthState=1&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&disableLoginPrepopulate=1&switch_account=signin&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

driver.find_element(By.CSS_SELECTOR, ".a-link-nav-icon").click()
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name").send_keys("test")
driver.find_element(By.CSS_SELECTOR, "#ap_email").send_keys("test")
driver.find_element(By.CSS_SELECTOR,   "#ap_password").send_keys("test")
driver.find_element(By.CSS_SELECTOR, "#ap_password_check").send_keys("test")
driver.find_element(By.CSS_SELECTOR, "#continue").click()
driver.find_element(By.CSS_SELECTOR,"[href*='condition_of_use']").click()
driver.find_element(By.CSS_SELECTOR,"[href*='privacy_notice']").click()
driver.find_element(By.CSS_SELECTOR,"[href*='signin']").click()












sleep(10)