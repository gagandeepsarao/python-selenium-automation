from behave import given, when, then
from selenium.webdriver.common.by import By

SIGNIN_HEADER = (By.XPATH, "//h1[@class='a-spacing-small']")



@then('Verify Sign In page is opened')
def verify_signin_opened(context):
    actual_text = context.driver.find_element(*SIGNIN_HEADER).text
    assert actual_text == 'Sign in', f'Expected Sign in but got {actual_text}'






