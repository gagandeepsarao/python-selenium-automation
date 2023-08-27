from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultPage(Page):
    SEARCH_RESULT = (By.CSS_SELECTOR, '.a-color-state.a-text-bold')
    PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")

    def verify_search_result(self, result):  # "tea"
        self.verify_text(result, *self.SEARCH_RESULT)

    def click_first_product(self):
        self.click(*self.PRODUCT_PRICE)