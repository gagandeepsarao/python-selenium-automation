from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


# create a new Chrome browser instance
service = Service(executable_path=r"C:\Users\gagan\Documents\python-selenium-automation\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service= service)
driver.maximize_window()

driver.get("https://www.amazon.com")

driver.find_element(By.XPATH,"//span[text()='& Orders']").click()
heading = driver.find_element(By.XPATH,"//h1[@class='a-spacing-small']").text
expected_heading = "Sign in"
assert heading == expected_heading, f'The {heading} is equal to {expected_heading}'
print("Test Case Passed")