from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

@given('Open Amazon T&C page')
def open_amazon_terms_page(context):
    context.app.amazon_privacy.open_amazon_terms_page()

@when('Store original windows')
def store_original_window(context):
    context.original_window = context.app.amazon_privacy.store_original_window()

@when('Click on Amazon Privacy Notice link')
def click_on_privacy_notice_link(context):
    context.app.amazon_privacy.click_on_privacy_notice_link()

@when('Switch to the newly opened window')
def switch_new_open_window(context):
    context.app.amazon_privacy.switch_to_new_window()

@then('Verify Amazon Privacy Notice page is opened')
def verify_amazon_privacy_page_opened(context):
    context.app.amazon_privacy.verify_amazon_privacy_page_opened()

@then('User can close new window and switch back to original')
def user_can_close_and_switch_back(context):
    context.app.amazon_privacy.close_page()
    context.app.amazon_privacy.switch_to_window(context.original_window)



