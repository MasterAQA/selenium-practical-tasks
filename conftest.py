import pytest
from selenium import webdriver

from pages.abtest_page import AbtestPage
from pages.add_remove_elements_page import AddRemoveElementsPage
from pages.basic_auth_page import BasicAuthPage
from pages.broken_images_page import BrokenImagesPage
from pages.checkbox_page import CheckboxPage
from pages.context_menu_page import ContextMenu
from pages.drag_and_drop_page import DragAndDrop
from pages.dropdown_page import DropdownPage
from pages.dynamic_controls_page import DynamicControlsPage
from pages.horizontal_slider_page import HorizontalSliderPage
from pages.hovers_page import HoversPage
from pages.inputs_page import InputsPage
from pages.multiple_windows_page import MultipleWindowsPage
from pages.data_table_page import DataTablePage


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()

    yield driver
    driver.quit()


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


@pytest.fixture()
def drag_and_drop_page(driver) -> DragAndDrop:
    return DragAndDrop(driver=driver)


@pytest.fixture()
def dropdown_page(driver) -> DropdownPage:
    return DropdownPage(driver=driver)


@pytest.fixture()
def dynamic_controls_page(driver) -> DynamicControlsPage:
    return DynamicControlsPage(driver=driver)


@pytest.fixture()
def horizontal_slider_page(driver) -> HorizontalSliderPage:
    return HorizontalSliderPage(driver=driver)


@pytest.fixture()
def hovers_page(driver) -> HoversPage:
    return HoversPage(driver=driver)


@pytest.fixture()
def inputs_page(driver) -> InputsPage:
    return InputsPage(driver=driver)


@pytest.fixture()
def multiple_windows_page(driver) -> MultipleWindowsPage:
    return MultipleWindowsPage(driver=driver)


@pytest.fixture()
def data_table_page(driver) -> DataTablePage:
    return DataTablePage(driver=driver)
