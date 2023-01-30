from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MultipleWindowsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _MULTIPLE_WINDOWS = (By.LINK_TEXT, "Multiple Windows")
    _MULTIPLE_WINDOWS_TITLE = (By.TAG_NAME, "h3")
    _LINK_ON_NEW_WINDOW = (By.XPATH, "//div[@class='example']/a")

    def navigate_to_page(self):
        self.wait_for(*self._MULTIPLE_WINDOWS).click()

    def get_title_text(self) -> str:
        return self.wait_for(*self._MULTIPLE_WINDOWS_TITLE).text

    def window_handle_by_index(self, index: int):
        return self.driver.window_handles[index]

    def switch_window(self, index_windows_handle):
        self.driver.switch_to.window(index_windows_handle)

    def new_window(self):
        self.wait_for(*self._LINK_ON_NEW_WINDOW).click()

    def size_handles(self) -> int:
        return len(self.driver.window_handles)

    def at_page(self) -> bool:
        return self.at_page_base("/windows")

    def at_new_page(self) -> bool:
        return self.at_page_base("/windows/new")
