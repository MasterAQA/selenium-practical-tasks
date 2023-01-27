from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AddRemoveElementsPage(BasePage):

    _ADD_REMOVE_ELEMENTS = (By.LINK_TEXT, "Add/Remove Elements")
    _ADD_REMOVE_TITLE = (By.TAG_NAME, "h3")
    _ADD_ELEMENT = (By.XPATH, "//div[@class='example']/button")
    _REMOVE_ELEMENT = (By.XPATH, "//button[@class='added-manually'][1]")
    _COUNT_ELEMENTS = (By.XPATH, "//button[@class='added-manually']")

    def navigate_to_page(self):
        self.wait_for(*self._ADD_REMOVE_ELEMENTS).click()

    def get_title_text(self):
        return self.wait_for(*self._ADD_REMOVE_TITLE).text

    def add_element(self):
        self.wait_for(*self._ADD_ELEMENT).click()

    def remove_element(self):
        self.wait_for(*self._REMOVE_ELEMENT).click()

    def check_elements_count(self) -> int:
        return len(self.find_elements(*self._COUNT_ELEMENTS))

    def at_page(self):
        return self.at_page_base("/add_remove_elements/")
