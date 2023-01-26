from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from config import URL

class Base_page:
    def __init__(self, driver):
        self._driver = driver
        self.default_url = URL
        self.get_url()

    def get_url(self) -> None:
        self._driver.get(self.default_url)

    def wait_for(self, *locator: str) -> WebDriver:
        return WebDriverWait(self._driver, 10).until(
            ec.presence_of_element_located(locator)
        )

    def at_page_base(self, link_end: str) -> bool:
        return (self._driver.current_url) == f"{self.default_url+link_end}"
