from pages.main_page import MainPage
from pages.header import Header
from pages.search_result_page import SearchResultPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.product_page import  ProductPage
from pages.amazon_privacy import  Amazon_privacy


class Application:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_result_page = SearchResultPage(driver)
        self.cart_page = CartPage(driver)
        self.product_page = ProductPage(driver)
        self.amazon_privacy = Amazon_privacy(driver)