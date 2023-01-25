from selenium.webdriver.common.by import By
from pages.base_page import *


class Add_remove_elements_page(Base_page):

    _ADD_REMOVE_ELEMENTS = (By.LINK_TEXT, "Add/Remove Elements")
    _ADD_REMOVE_TITLE = (By.TAG_NAME, "h3")
    _ADD_ELEMENT = (By.XPATH, "//div[@class='example']/button")
    _REMOVE_ELEMENT = (By.XPATH, "//button[@class='added-manually'][1]")

    def navigate_to_add_remove_elements_page(self):
        self.wait_for(*self._ADD_REMOVE_ELEMENTS).click()

    def check_title(self):
        return self.wait_for(*self._ADD_REMOVE_TITLE).text

    def add_element(self):
        self.wait_for(*self._ADD_ELEMENT).click()

    def add_elements(self, count):
        for i in range (0, count):
            self.add_element()

    def remove_element(self):
        self.wait_for(*self._REMOVE_ELEMENT).click()

    def remove_elements(self, count):
        for i in range(0, count):
            self.remove_element()

    def check_page(self):
        return self.check_page_base("/add_remove_elements/")
