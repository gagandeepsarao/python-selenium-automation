

from behave import given, when, then
from selenium.webdriver.common.by import By

SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
ORDERS_BTN = (By.ID, 'nav-orders')
FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterDescItem')
BEST_SELLER = (By.XPATH,"//a[text()='Best Sellers']")
BEST_SELLERS_LINKS = (By.XPATH,'//div[starts-with(@class, "_p13n-zg-nav-tab-all_style")]//a')
FIRST_PRODUCT = (By.XPATH,'//div[@class= "p13n-sc-truncate-desktop-type2  p13n-sc-truncated"]')
ADD_TO_CART_BTN = (By.ID,'add-to-cart-button')
ADDED_TO_CART_TEXT = (By.XPATH,"//span[@class='a-size-medium-plus a-color-base sw-atc-text a-text-bold']")


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Search for {product}')
def search_on_amazon(context, product):
    context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    context.driver.find_element(*SEARCH_BTN).click()


@when('Click Orders')
def click_orders(context):
    context.driver.find_element(*ORDERS_BTN).click()


@when('Click on Best Sellers')
def click_best_sellers(context):
    context.driver.find_element(*BEST_SELLER).click()


@when('Click on the first product')
def click_on_first_product(context):
    context.driver.find_element(*FIRST_PRODUCT).click()


@when('Click on Add to cart button')
def click_on_add_to_cart_button(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()


@then('Verify footer has {expected_amount} links')
def verify_link_amount(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*FOOTER_LINKS)
    assert len(links) == expected_amount, f'Expected {expected_amount} links but got {len(links)}'


@then('Verify many links are shown in the footer')
def verify_many_links(context):
    links = context.driver.find_elements(*FOOTER_LINKS)
    assert len(links) > 1, f'Expected at least 2 links, but got {len(links)}'


@then('Verify 5 links are shown on the top of the page')
def verify_five_links_are_present(context):
    links = context.driver.find_elements(*BEST_SELLERS_LINKS)
    assert len(links) == 5, f'Expected 5 links, but got {len(links)}'


@then('Verify "Added to Cart" text is displayed on the page')
def verify_added_to_cart_text_displayed(context):
    context.driver.find_element(*ADDED_TO_CART_TEXT).click()
