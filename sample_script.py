from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# get the path to the ChromeDriver executable

# create a new Chrome browser instance
service = Service(executable_path=r"C:\Users\gagan\Documents\python-selenium-automation\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.wait = WebDriverWait(driver, 2)
# open the url
driver.get('https://www.google.com/')

# populate search field
search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Table')

button = driver.find_element(By.NAME, 'btnK')

driver.wait.until(EC.element_to_be_clickable(button)).click()

# verify search results
assert 'table' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
