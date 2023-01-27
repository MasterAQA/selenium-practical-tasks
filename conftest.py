import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains

from pages.abtest_page import AbtestPage
from pages.add_remove_elements_page import AddRemoveElementsPage
from pages.basic_auth_page import BasicAuthPage
from pages.broken_images_page import BrokenImagesPage
from pages.checkbox_page import CheckboxPage
from pages.context_menu_page import ContextMenu


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()

    yield driver
    driver.close()


@pytest.fixture()
def abtest_page(driver) -> AbtestPage:
    return AbtestPage(driver=driver)


@pytest.fixture()
def add_remove_elements_page(driver) -> AddRemoveElementsPage:
    return AddRemoveElementsPage(driver=driver)


@pytest.fixture()
def basic_auth_page(driver) -> BasicAuthPage:
    return BasicAuthPage(driver=driver)


@pytest.fixture()
def broken_images_page(driver) -> BrokenImagesPage:
    return BrokenImagesPage(driver=driver)


@pytest.fixture()
def checkbox_page(driver) -> CheckboxPage:
    return CheckboxPage(driver=driver)


@pytest.fixture()
def context_menu_page(driver) -> ContextMenu:
    return ContextMenu(driver=driver)
