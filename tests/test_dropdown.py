import time

import pytest

DROPDOWN_TITLE_TEXT = "Dropdown List"
DROPDOWN_INDEX_1 = "Option 1"
DROPDOWN_INDEX_2 = "Option 2"


def test_dropdown(dropdown_page) -> None:
    dropdown_page.navigate_to_page()

    assert dropdown_page.at_page()


def test_dropdown_title_text(dropdown_page) -> None:
    dropdown_page.navigate_to_page()

    assert dropdown_page.at_page()
    assert dropdown_page.get_title_text() == DROPDOWN_TITLE_TEXT


def test_dropdown_select_1(dropdown_page) -> None:
    dropdown_page.navigate_to_page()
    dropdown_page.dropdown().select_by_index(1)

    assert dropdown_page.at_page()
    assert dropdown_page.dropdown_text() == DROPDOWN_INDEX_1


def test_dropdown_select_2(dropdown_page) -> None:
    dropdown_page.navigate_to_page()
    dropdown_page.dropdown().select_by_index(2)

    assert dropdown_page.at_page()
    assert dropdown_page.dropdown_text() == DROPDOWN_INDEX_2
