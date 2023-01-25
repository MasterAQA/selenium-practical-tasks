from selenium.webdriver.common.by import By
from pages.base_page import *


class Abtest_page(Base_page):

    _ABTEST_MENU = (By.LINK_TEXT, "A/B Testing")
    _ABTEST_TITLE = (By.TAG_NAME, "h3")
    _ABTEST_TEXT = (By.XPATH, "//div[@class='example']/p")

    def navigate_to_abtest_page(self):
        self.wait_for(*self._ABTEST_MENU).click()

    def check_title(self):
        return self.wait_for(*self._ABTEST_TITLE).text

    def check_text(self):
        return self.wait_for(*self._ABTEST_TEXT).text

    def check_page(self):
        return self.check_page_base("/abtest")

