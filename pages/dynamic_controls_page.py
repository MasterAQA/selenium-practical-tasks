from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage


class DynamicControlsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _DYNAMIC_CONTROLS = (By.LINK_TEXT, "Dynamic Controls")
    _DYNAMIC_CONTROLS_TITLE = (By.TAG_NAME, "h4")
    _REMOVE_ADD_BUTTON = (By.XPATH, "//form[@id='checkbox-example']/button")
    _RESULT_MESSAGE = (By.XPATH, "//form[@id='checkbox-example']/p")

    def navigate_to_page(self):
        self.wait_for(*self._DYNAMIC_CONTROLS).click()

    def get_title_text(self) -> str:
        return self.wait_for(*self._DYNAMIC_CONTROLS_TITLE).text

    def remove_add_button(self, value):
        self.wait_for(
            *(
                self._REMOVE_ADD_BUTTON[0],
                (self._REMOVE_ADD_BUTTON[1] + f"[contains(text(), {value})]"),
            )
        ).click()

    def result_message(self, value) -> str:
        return self.wait_for(
            *(
                self._RESULT_MESSAGE[0],
                (self._RESULT_MESSAGE[1] + f'[contains(text(), "{value}")]'),
            )
        ).text

    def at_page(self) -> bool:
        return self.at_page_base("/dynamic_controls")
