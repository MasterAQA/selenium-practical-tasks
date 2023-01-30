from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AbtestPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    _ABTEST_MENU = (By.LINK_TEXT, "A/B Testing")
    _ABTEST_TITLE = (By.TAG_NAME, "h3")
    _ABTEST_TEXT = (By.XPATH, "//div[@class='example']/p")

    def navigate_to_page(self):
        self.wait_for(*self._ABTEST_MENU).click()

    def get_title(self):
        return self.wait_for(*self._ABTEST_TITLE)

    def get_title_text(self) -> str:
        return self.wait_for(*self._ABTEST_TITLE).text

    def get_content(self):
        return self.wait_for(*self._ABTEST_TEXT)

    def get_content_text(self) -> str:
        return self.wait_for(*self._ABTEST_TEXT).text

    def at_page(self) -> bool:
        return self.at_page_base("/abtest")
