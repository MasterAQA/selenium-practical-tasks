from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from config import URL


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver
        self.actionChains = ActionChains(driver)
        self.default_url = URL
        self.get_url(self.default_url)

    def get_url(self, url: str):
        self._driver.get(url)

    def wait_for(self, *locator: str) -> WebDriver:
        return WebDriverWait(self._driver, 10).until(
            ec.presence_of_element_located(locator)
        )

    def find_element(self, *locator: str) -> WebElement:
        return self.wait_for(*locator).find_element(*locator)

    def find_elements(self, *locator: str) -> list:
        return self.wait_for(*locator).find_elements(*locator)

    def find_elements_text(self, *locator: str) -> list:
        list_objects = self.wait_for(*locator).find_elements(*locator)
        list_text_obj = []
        [list_text_obj.append(_.text) for _ in list_objects]
        return list_text_obj

    def at_page_base(self, link_end: str) -> bool:
        return (self._driver.current_url) == f"{self.default_url+link_end}"

    def at_page_base_admin(self, link_end: str) -> bool:
        return (self._driver.current_url) == (
            self.default_url.replace("https://", f"https://admin:admin@") + link_end
        )

    def get_image_src_on_index(self, _locator: tuple, index: int) -> str:
        return self.find_element(
            *(_locator[0], (_locator[1] + f"[{index}]"))
        ).get_attribute("src")
