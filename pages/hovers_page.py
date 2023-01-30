import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage


class HoversPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _HOVERS = (By.LINK_TEXT, "Hovers")
    _HOVERS_TITLE = (By.TAG_NAME, "h3")
    _HOVERS_IMG = (By.XPATH, "//div[@class='figure']")

    def navigate_to_page(self):
        self.wait_for(*self._HOVERS).click()

    def get_title_text(self) -> str:
        return self.wait_for(*self._HOVERS_TITLE).text

    def hover_img(self, index: int):
        self.actionChains.move_to_element(
            self.wait_for(
                *(self._HOVERS_IMG[0], (self._HOVERS_IMG[1] + f"[{index}]/img"))
            )
        ).perform()

    def get_content_after_hover(self, index: int) -> str:
        return self.wait_for(
            *(
                self._HOVERS_IMG[0],
                (self._HOVERS_IMG[1] + f"[{index}]/div[@class='figcaption']/h5"),
            )
        ).text

    def at_page(self) -> bool:
        return self.at_page_base("/hovers")
