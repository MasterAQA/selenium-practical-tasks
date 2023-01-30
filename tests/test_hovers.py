import time

import pytest

HOVERS_TITLE_TEXT = "Hovers"

HOVER_CONTENT_1 = "name: user1"
HOVER_CONTENT_3 = "name: user3"


def test_hovers(hovers_page) -> None:
    hovers_page.navigate_to_page()

    assert hovers_page.at_page()


def test_hovers_title_text(hovers_page) -> None:
    hovers_page.navigate_to_page()

    assert hovers_page.at_page()
    assert hovers_page.get_title_text() == HOVERS_TITLE_TEXT


def test_hovers_img(hovers_page) -> None:
    hovers_page.navigate_to_page()
    hovers_page.hover_img(1)

    assert hovers_page.at_page()
    assert hovers_page.get_content_after_hover(1) == HOVER_CONTENT_1


def test_hovers_img_check_1(hovers_page) -> None:
    hovers_page.navigate_to_page()
    hovers_page.hover_img(1)

    assert hovers_page.at_page()
    assert hovers_page.get_content_after_hover(1) == HOVER_CONTENT_1


def test_hovers_img_check_3(hovers_page) -> None:
    hovers_page.navigate_to_page()
    hovers_page.hover_img(3)

    assert hovers_page.at_page()
    assert hovers_page.get_content_after_hover(3) == HOVER_CONTENT_3
