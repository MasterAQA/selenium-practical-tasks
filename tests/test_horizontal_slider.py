import time

import pytest

HORIZONTAL_SLIDER_TITLE_TEXT = "Horizontal Slider"


def test_horizontal_slider(horizontal_slider_page) -> None:
    horizontal_slider_page.navigate_to_page()

    assert horizontal_slider_page.at_page()


def test_horizontal_slider_title_text(horizontal_slider_page) -> None:
    horizontal_slider_page.navigate_to_page()

    assert horizontal_slider_page.at_page()
    assert horizontal_slider_page.get_title_text() == HORIZONTAL_SLIDER_TITLE_TEXT


def test_horizontal_slider_move(horizontal_slider_page) -> None:
    horizontal_slider_page.navigate_to_page()
    horizontal_slider_page.move_slider(0.5)

    assert horizontal_slider_page.at_page()
    assert horizontal_slider_page.slider_value() == 0.5


def test_horizontal_slider_move_(horizontal_slider_page) -> None:
    horizontal_slider_page.navigate_to_page()
    horizontal_slider_page.move_slider(4)

    assert horizontal_slider_page.at_page()
    assert horizontal_slider_page.slider_value() == 4


def test_horizontal_slider_move_max(horizontal_slider_page) -> None:
    horizontal_slider_page.navigate_to_page()
    horizontal_slider_page.move_slider(6)

    assert horizontal_slider_page.at_page()
    assert horizontal_slider_page.slider_value() == 5
