from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DragAndDrop(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _DRAG_AND_DROP = (By.LINK_TEXT, "Drag and Drop")
    _DRAG_AND_DROP_TITLE = (By.TAG_NAME, "h3")
    _DRAG_AND_DROP_DRUG_A = (By.XPATH, "//div[@id='columns']/div[@id='column-a']")
    _DRAG_AND_DROP_DRUG_B = (By.XPATH, "//div[@id='columns']/div[@id='column-b']")

    def navigate_to_page(self):
        self.wait_for(*self._DRAG_AND_DROP).click()

    def get_title_text(self) -> str:
        return self.wait_for(*self._DRAG_AND_DROP_TITLE).text

    def get_element_a_text(self) -> str:
        return self.wait_for(*self._DRAG_AND_DROP_DRUG_A).text

    def get_element_b_text(self) -> str:
        return self.wait_for(*self._DRAG_AND_DROP_DRUG_B).text

    def drag_a_to_b(self):
        self.wait_for(*self._DRAG_AND_DROP_DRUG_A)
        self.actionChains.drag_and_drop(
            self.find_element(*self._DRAG_AND_DROP_DRUG_A),
            self.find_element(*self._DRAG_AND_DROP_DRUG_B),
        ).perform()

    def drag_b_to_a(self):
        self.wait_for(*self._DRAG_AND_DROP_DRUG_A)
        self.actionChains.drag_and_drop(
            self.find_element(*self._DRAG_AND_DROP_DRUG_B),
            self.find_element(*self._DRAG_AND_DROP_DRUG_A),
        ).perform()

    def at_page(self) -> bool:
        return self.at_page_base("/drag_and_drop")
