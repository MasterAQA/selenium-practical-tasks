from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import requests


class BrokenImagesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    _BROKEN_IMAGES = (By.LINK_TEXT, "Broken Images")
    _BROKEN_IMAGES_TITLE = (By.TAG_NAME, "h3")
    _BROKEN_IMAGES_LINK = (By.XPATH, "//div[@class='example']/img")

    def navigate_to_page(self):
        self.wait_for(*self._BROKEN_IMAGES).click()

    def get_title_text(self) -> str:
        return self.wait_for(*self._BROKEN_IMAGES_TITLE).text

    def check_broken_image(self, index: int) -> bool:
        return (
            requests.get(
                self.get_image_src_on_index(self._BROKEN_IMAGES_LINK, index)
            ).status_code
            == 200
        )

    def at_page(self) -> bool:
        return self.at_page_base("/broken_images")
