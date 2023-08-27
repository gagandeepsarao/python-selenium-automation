from time import sleep
from pages.base_page import Page

from selenium.webdriver.common.by import By


class CartPage(Page):

    CART_BUTTON = (By.ID, "nav-cart-count-container")
    CART_EMPTY_TEXT = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']")
    ADD_TO_CART = (By.ID,"add-to-cart-button")
    CART_COUNT = (By.ID,"nav-cart-count")
    PRODUCT_NAME = (By.XPATH, '//span[@class= "a-truncate-cut"]')

    def click_cart(self):
        self.click(*self.CART_BUTTON)

    def click_add_to_cart(self):
        self.click(*self.ADD_TO_CART)

    def verify_text_present(self, expected_result):
        self.verify_text(expected_result,  *self.CART_EMPTY_TEXT)

    def verify_cart_has_expected_amount(self,expected_amount):
        self.verify_text(expected_amount, *self.CART_COUNT)

    def verify_cart_has_right_product(self):
        self.verify_partial_text('Pitcher', *self.PRODUCT_NAME)


