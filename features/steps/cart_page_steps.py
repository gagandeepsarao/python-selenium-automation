from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@when('Click on cart icon')
def click_cart(context):
    context.app.cart_page.click_cart()


@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.app.cart_page.click_add_to_cart()
    sleep(2)


@when('Open cart page')
def click_cart(context):
    context.app.cart_page.click_cart()


@then('Verify {expected_text} text present')
def verify_text_present(context, expected_text):
    context.app.cart_page.verify_text_present(expected_text)


@then('Verify cart has {expected_amount} item(s)')
def verify_cart_has_expected_amount(context, expected_amount):
    context.app.cart_page.verify_cart_has_expected_amount(expected_amount)


@then('Verify cart has correct product')
def verify_cart_has_right_product(context):
    context.app.cart_page.verify_cart_has_right_product()
