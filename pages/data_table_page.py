import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage


class DataTablePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _DATA_TABLE = (By.LINK_TEXT, "Sortable Data Tables")
    _DATA_TABLE_WINDOWS_TITLE = (By.TAG_NAME, "h3")
    _DATA_TABLE_XPATH = (By.XPATH, "//table[@id='table1']")

    def navigate_to_page(self):
        self.wait_for(*self._DATA_TABLE).click()

    def get_title_text(self) -> str:
        return self.wait_for(*self._DATA_TABLE_WINDOWS_TITLE).text

    def values_from_column(self, index) -> list:
        self.wait_for(*self._DATA_TABLE_XPATH)
        return self.find_elements_text(
            *(
                self._DATA_TABLE_XPATH[0],
                (self._DATA_TABLE_XPATH[1] + f"/tbody/tr/td[{index}]"),
            )
        )

    def values_from_line(self, index) -> list:
        self.wait_for(*self._DATA_TABLE_XPATH)
        return self.find_elements_text(
            *(
                self._DATA_TABLE_XPATH[0],
                (self._DATA_TABLE_XPATH[1] + f"/tbody/tr[{index}]/td"),
            )
        )

    def values_from_area(
        self, column_value_1, column_value_2, line_value_1, line_value_2
    ):
        self.wait_for(*self._DATA_TABLE_XPATH)
        list_1 = self.column_range(column_value_1, line_value_1, line_value_2)
        list_2 = self.column_range(column_value_2, line_value_1, line_value_2)

        return dict(zip(list_1, list_2))

    def column_range(self, column_value, line_value_1, line_value_2):
        empty_list = []
        for j in range(line_value_1, line_value_2):
            data = self.find_element(
                *(
                    self._DATA_TABLE_XPATH[0],
                    (self._DATA_TABLE_XPATH[1] + f"/tbody/tr[{j}]/td[{column_value}]"),
                )
            ).text
            empty_list.append(data)
        return empty_list

    def size_handles(self) -> int:
        return len(self.driver.window_handles)

    def at_page(self) -> bool:
        return self.at_page_base("/tables")

    def at_new_page(self) -> bool:
        return self.at_page_base("/windows/new")
