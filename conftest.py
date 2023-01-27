import pytest
from selenium import webdriver
from pages.abtest_page import AbtestPage

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()

    yield driver
    driver.close()


@pytest.fixture()
def abtest_page(driver) -> AbtestPage:
    return AbtestPage(driver=driver)