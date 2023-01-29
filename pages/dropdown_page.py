from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage


class DropdownPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _DROPDOWN = (By.LINK_TEXT, "Dropdown")
    _DROPDOWN_TITLE = (By.TAG_NAME, "h3")
    _DROPDOWN_XPATH = (By.XPATH, "//select[@id='dropdown']")
    _DROPDOWN_SELECTED_XPATH = (
        By.XPATH,
        "//select[@id='dropdown']/option[contains(@selected,'selected')]",
    )
    _DRAG_AND_DROP_DRUG_B = (By.XPATH, "//div[@id='columns']/div[@id='column-b']")

    def navigate_to_page(self):
        self.wait_for(*self._DROPDOWN).click()

    def get_title_text(self) -> str:
        return self.wait_for(*self._DROPDOWN_TITLE).text

    def dropdown(self) -> Select:
        return Select(self.driver.find_element(*self._DROPDOWN_XPATH))

    def dropdown_text(self) -> str:
        return self.find_element(*self._DROPDOWN_SELECTED_XPATH).text

    def at_page(self) -> bool:
        return self.at_page_base("/dropdown")
