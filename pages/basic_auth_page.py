from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class BasicAuthPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    _BASIC_AUTH = (By.LINK_TEXT, "Basic Auth")
    _BASIC_AUTH_TITLE = (By.TAG_NAME, "h3")
    _BASIC_AUTH_TEXT = (By.XPATH, "//div[@class='example']/p")

    def navigate_to_page(self):
        self.wait_for(*self._BASIC_AUTH).click()

    def pass_basic_auth(self, user: str, pass_: str):
        self.get_url(self.default_url.replace("https://", f"https://{user}:{pass_}@"))

    def get_title_text(self) -> str:
        return self.wait_for(*self._BASIC_AUTH_TITLE).text

    def get_content_text(self) -> str:
        return self.wait_for(*self._BASIC_AUTH_TEXT).text

    def at_page(self) -> bool:
        return self.at_page_base("/basic_auth")

    def at_page_admin(self) -> bool:
        return self.at_page_base_admin("/basic_auth")
