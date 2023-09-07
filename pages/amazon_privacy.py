from time import sleep
from pages.base_page import Page

from selenium.webdriver.common.by import By


class Amazon_privacy(Page):

    PRIVACY_LINK = (By.XPATH,"//a[text() = 'Privacy Notice']")
    PRIVACY_NOTICE_TEXT = (By.XPATH,"//h1[@id='GUID-8966E75F-9B92-4A2B-BFD5-967D57513A40__GUID-2C1DF364-8FA3-4387-BCDB-2A63B7C51B64']']")



    def open_amazon_terms_page(self):
        self.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088 ')


    def store_original_window(self):
        return self.get_current_window()

    def click_on_privacy_notice_link(self):
        self.click(*self.PRIVACY_LINK)

    def verify_amazon_privacy_page_opened(self):
        self.verify_partial_url('nodeId=GX7NJQ4ZB8MHFRNJ')


