import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage


class InputsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _INPUTS = (By.LINK_TEXT, "Inputs")
    _INPUTS_TITLE = (By.TAG_NAME, "h3")

    _INPUTS_INPUT = (By.XPATH, "//div[@class='example']/input")

    def navigate_to_page(self):
        self.wait_for(*self._INPUTS).click()

    def get_title_text(self) -> str:
        return self.wait_for(*self._INPUTS_TITLE).text

    def get_input_value(self) -> int:
        return int(self.wait_for(*self._INPUTS_INPUT).get_attribute("value"))

    def input_int(self, value):
        self.actionChains.send_keys_to_element(
            self.wait_for(*self._INPUTS_INPUT), value
        ).perform()

    def input_arrow_up(self):
        self.actionChains.send_keys_to_element(
            self.wait_for(*self._INPUTS_INPUT), Keys.ARROW_UP
        ).perform()

    def input_arrow_down(self):
        self.actionChains.send_keys_to_element(
            self.wait_for(*self._INPUTS_INPUT), Keys.ARROW_DOWN
        ).perform()

    def at_page(self) -> bool:
        return self.at_page_base("/inputs")
