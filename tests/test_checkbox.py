import time

import pytest

CHECKBOX_TITLE_TEXT = "Checkboxes"


def test_checkbox(checkbox_page) -> None:
    checkbox_page.navigate_to_page()

    assert checkbox_page.at_page()


def test_checkbox_title_text(checkbox_page) -> None:
    checkbox_page.navigate_to_page()

    assert checkbox_page.at_page()
    assert checkbox_page.get_title_text() == CHECKBOX_TITLE_TEXT


def test_checkbox_input(checkbox_page) -> None:
    checkbox_page.navigate_to_page()
    checkbox_page.checkbox_element(1).click()

    assert checkbox_page.at_page()
    assert checkbox_page.checkbox_element(1).is_selected()


def test_checkbox_uninput(checkbox_page) -> None:
    checkbox_page.navigate_to_page()
    checkbox_page.checkbox_element(2).click()

    assert checkbox_page.at_page()
    assert checkbox_page.checkbox_element(2).is_selected() == False


def test_checkboxes_input(checkbox_page) -> None:
    checkbox_page.navigate_to_page()
    [checkbox_page.checkbox_element(_).click() for _ in range(1, 3)]

    assert checkbox_page.at_page()
    assert checkbox_page.checkbox_element(1).is_selected()
    assert checkbox_page.checkbox_element(2).is_selected() == False
