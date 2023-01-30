import pytest

DRAG_AND_DROP_TITLE_TEXT = "Drag and Drop"
ELEMENT_A = "A"
ELEMENT_B = "B"


def test_drag_and_drop(drag_and_drop_page) -> None:
    drag_and_drop_page.navigate_to_page()

    assert drag_and_drop_page.at_page()


def test_drag_and_drop_title_text(drag_and_drop_page) -> None:
    drag_and_drop_page.navigate_to_page()

    assert drag_and_drop_page.at_page()
    assert drag_and_drop_page.get_title_text() == DRAG_AND_DROP_TITLE_TEXT


def test_drag_and_drop_elements_text(drag_and_drop_page) -> None:
    drag_and_drop_page.navigate_to_page()

    assert drag_and_drop_page.at_page()
    assert drag_and_drop_page.get_element_a_text() == ELEMENT_A
    assert drag_and_drop_page.get_element_b_text() == ELEMENT_B


@pytest.mark.xfail(reason="Метод не работает с данным сайтом")
def test_drag_and_drop_drag_a(drag_and_drop_page) -> None:
    drag_and_drop_page.navigate_to_page()
    drag_and_drop_page.drag_a_to_b()

    assert drag_and_drop_page.at_page()
    assert drag_and_drop_page.get_element_a_text() == ELEMENT_B


@pytest.mark.xfail(reason="Метод не работает с данным сайтом")
def test_drag_and_drop_drag_b(drag_and_drop_page) -> None:
    drag_and_drop_page.navigate_to_page()
    drag_and_drop_page.drag_b_to_a()

    assert drag_and_drop_page.at_page()
    assert drag_and_drop_page.get_element_b_text() == ELEMENT_A
