from selenium.webdriver.common.by import By
from behave import *
from time import sleep


ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
PRODUCT_NAME = (By.ID, 'productTitle')
COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")
COLOR_SELECTOR = (By.CSS_SELECTOR, "#variation_color_name .selection")
SELECTED_COLOR = (By.CSS_SELECTOR,'.selection')


# @given('Open Amazon product {product_id} page')
# def open_amazon_product(context, product_id):
#     context.driver.get(f'https://www.amazon.com/dp/{product_id}/')

#homework 5
@given('Open Amazon product {product_id} page')
def open_amazon_product(context, product_id):
     context.driver.get(f'https://www.amazon.com/gp/product/B07BJKRR25/')
    # context.driver.get(f'https://www.amazon.com/gp/{product_id}/')


@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    sleep(2)


@when('Store product name')
def get_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Current product: {context.product_name}')


#Homework5
@when('Click on each color')
def click_on_each_color(context):
    expected_colors = ['Black', 'Blue Over Dye', 'Dark Blue Vintage', 'Dark Indigo', 'Dark Wash', 'Indigo Wash', 'Light Wash', 'Medium Blue Vintage', 'Medium Wash', 'Rinsed', 'Vintage Wash', 'Washed Black', 'Bright White', 'Dark Khaki Brown', 'Light Khaki Brown', 'Olive', 'Light Blue Vintage', 'Washed Grey', 'Sage Green']
    colors_list = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for color in colors:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        colors_list.append(current_color)

    assert colors_list == expected_colors, f'Expected {expected_colors} did not match actual {colors_list}'

#Homework5
@then('Verify that one color has been selected')
def verify_one_color_is_selected(context):
    color = context.driver.find_element(*SELECTED_COLOR).text
    if color != "":
        f'Color is not selected.'


@then('Verify user can click through colors')
def verify_can_click_colors(context):
    expected_colors = ['Army Green', 'Black', 'Blue', 'Brown'] # 0, 1, 2, 3
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for color in colors[:4]:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text

        actual_colors.append(current_color)

    assert actual_colors == expected_colors, f'Expected {expected_colors} did not match actual {actual_colors}'