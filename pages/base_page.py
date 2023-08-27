class Page:

    def __init__(self, driver):
        self.driver = driver

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def input_text(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.send_keys(text)

    def verify_text(self,expected_result, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_result == actual_text, f'Error expected {expected_result} does not match actual {actual_text}'




