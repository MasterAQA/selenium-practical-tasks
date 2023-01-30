from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage


class HorizontalSliderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _HORIZONTAL_SLIDER = (By.LINK_TEXT, "Horizontal Slider")
    _HORIZONTAL_SLIDER_TITLE = (By.TAG_NAME, "h3")
    _SLIDER = (By.XPATH, "//div[@class='sliderContainer']/input")
    _SLIDER_VALUE = (By.XPATH, "//span[@id='range']")

    def navigate_to_page(self):
        self.wait_for(*self._HORIZONTAL_SLIDER).click()

    def get_title_text(self) -> str:
        return self.wait_for(*self._HORIZONTAL_SLIDER_TITLE).text

    def move_slider(self, percent):
        width = self.wait_for(*self._SLIDER).size["width"]
        one_percent = width / 100
        self.actionChains.drag_and_drop_by_offset(
            self.find_element(*self._SLIDER),
            (((percent * 10) * one_percent) / 0.5) - (one_percent * 50),
            0,
        ).perform()

    def slider_value(self) -> float:
        return float(self.wait_for(*self._SLIDER_VALUE).text)

    def at_page(self) -> bool:
        return self.at_page_base("/horizontal_slider")
