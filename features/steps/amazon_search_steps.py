from behave import given, when, then
from selenium.webdriver.common.by import By


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Search for table')
def search_on_amazon(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('table')
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@then('Verify search result is correct')
def verify_search_result(context):
    expected_result = '"table"'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, '.a-color-state.a-text-bold').text
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'

@when("Click Returns & Orders")
def click_returns_button(context):
    context.driver.find_element(By.ID, 'nav-orders').click()


@when("Click cart icon")
def click_cart_icon(context):
    context.driver.find_element(By.ID,'nav-cart-count-container').click()


@then("Verify Sign in page opened")
def verify_signin_page_opened(context):
    expected_result = "Sign in"
    actual_result = context.driver.find_element(By.CSS_SELECTOR,'h1.a-spacing-small').text
    assert expected_result ==  actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'


@then("Verify email input field is present")
def verify_email_field_present(context):
    expected_result = "email"
    actual_result = context.driver.find_element(By.XPATH,"//input[@id='ap_email']/preceding-sibling::label").text
    assert expected_result in actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'


@then("Verify cart is empty")
def verify_cart_empty(context):
    expected_result = 'empty'
    actual_result = context.driver.find_element(By.XPATH,"//*[normalize-space(text())= 'Your Amazon Cart is empty']").text
    assert expected_result in actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'




