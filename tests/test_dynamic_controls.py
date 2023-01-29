import time

import pytest

DYNAMIC_CONTROL_TITLE_TEXT = "Dynamic Controls"

AFTER_REMOVE_BUTTON = "It's gone!"
AFTER_ADD_BUTTON = "It's back!"


def test_dynamic_controls(dynamic_controls_page) -> None:
    dynamic_controls_page.navigate_to_page()

    assert dynamic_controls_page.at_page()


def test_dynamic_controls_title_text(dynamic_controls_page) -> None:
    dynamic_controls_page.navigate_to_page()

    assert dynamic_controls_page.at_page()
    assert dynamic_controls_page.get_title_text() == DYNAMIC_CONTROL_TITLE_TEXT


def test_dynamic_controls_remove(dynamic_controls_page) -> None:
    dynamic_controls_page.navigate_to_page()
    dynamic_controls_page.remove_add_button("Remove")
    message_after_action = dynamic_controls_page.result_message("It's gone!")

    assert dynamic_controls_page.at_page()
    assert message_after_action == AFTER_REMOVE_BUTTON


def test_dynamic_controls_add(dynamic_controls_page) -> None:
    dynamic_controls_page.navigate_to_page()
    dynamic_controls_page.remove_add_button("Remove")
    dynamic_controls_page.result_message("It's gone!")
    dynamic_controls_page.remove_add_button("Add")
    message_after_action = dynamic_controls_page.result_message("It's back!")

    assert dynamic_controls_page.at_page()
    assert message_after_action == AFTER_ADD_BUTTON
