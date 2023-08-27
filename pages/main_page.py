from time import sleep
from pages.base_page import Page

from selenium.webdriver.common.by import By


class MainPage(Page):
    CART_BUTTON = (By.ID, "nav-cart-count-container")
    CART_EMPTY_TEXT = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']")

    def open_main(self):
        self.driver.get('https://www.amazon.com/')
        sleep(2)
        self.driver.refresh()

