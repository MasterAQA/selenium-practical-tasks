import pytest
from selenium import webdriver
from pages.abtest_page import AbtestPage
from pages.add_remove_elements_page import AddRemoveElementsPage
from pages.basic_auth_page import BasicAuthPage

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

