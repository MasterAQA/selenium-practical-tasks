from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ContextMenu(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _CONTEXT_MENU = (By.LINK_TEXT, "Context Menu")
    _CONTEXT_MENU_TITLE = (By.TAG_NAME, "h3")
    _CONTEXT_MENU_ZONE = (By.XPATH, "//div[@id='hot-spot']")

    def navigate_to_page(self):
        self.wait_for(*self._CONTEXT_MENU).click()

    def get_title_text(self) -> str:
        return self.wait_for(*self._CONTEXT_MENU_TITLE).text

    def right_click_on_context_zone(self):
        self.actionChains.context_click(
            self.wait_for(*self._CONTEXT_MENU_ZONE)
        ).perform()

    def alert_text(self) -> str:
        return self.driver.switch_to.alert.text

    def alert_accept(self):
        self.driver.switch_to.alert.accept()

    def alert_dismiss(self):
        self.driver.switch_to.alert.dismiss()

    def at_page(self) -> bool:
        return self.at_page_base("/context_menu")
