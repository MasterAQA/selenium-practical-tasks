from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver


class CheckboxPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    _CHECKBOX = (By.LINK_TEXT, "Checkboxes")
    _CHECKBOX_TITLE = (By.TAG_NAME, "h3")
    _CHECKBOX_INPUT = (By.XPATH, "//form[@id='checkboxes']/input")

    def navigate_to_page(self):
        self.wait_for(*self._CHECKBOX).click()

    def get_title_text(self) -> str:
        return self.wait_for(*self._CHECKBOX_TITLE).text

    def checkbox_element(self, index: int) -> WebDriver:
        return self.wait_for(
            *(self._CHECKBOX_INPUT[0], (self._CHECKBOX_INPUT[1] + f"[{index}]"))
        )

    def at_page(self) -> bool:
        return self.at_page_base("/checkboxes")
