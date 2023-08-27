from pages.base_page import Page
from selenium.webdriver.common.by import By

class ProductPage(Page):
    PRODUCT_NAME = (By.ID, 'productTitle')

    def get_product_name(self):
        product_name = self.find_element(*self.PRODUCT_NAME).text
        print(f'Current product: {product_name}')



