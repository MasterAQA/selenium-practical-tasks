from pages.add_remove_elements_page import Add_remove_elements_page

ADD_REMOVE_ELEMENTS_TITLE = "Add/Remove Elements"


def test_add_remove_elements_page_should_work():
    page = Add_remove_elements_page()
    page.navigate_to_add_remove_elements_page()

    page.add_element()
    [page.add_element() for _ in range(5)]

    page.remove_element()
    [page.add_element() for _ in range(5)]

    assert page.at_page()
    assert page.get_title_text() == ADD_REMOVE_ELEMENTS_TITLE
