from pages.add_remove_elements_page import AddRemoveElementsPage

ADD_REMOVE_ELEMENTS_TITLE = "Add/Remove Elements"


def test_add_remove_elements_page(add_remove_elements_page):
    add_remove_elements_page.navigate_to_page()

    assert add_remove_elements_page.at_page()



def test_add_remove_elements_page_title(add_remove_elements_page):
    add_remove_elements_page.navigate_to_page()

    assert add_remove_elements_page.at_page()
    assert add_remove_elements_page.get_title_text() == ADD_REMOVE_ELEMENTS_TITLE


def test_add_remove_elements_page_add_elements(add_remove_elements_page):
    add_remove_elements_page.navigate_to_page()

    [add_remove_elements_page.add_element() for _ in range(5)]

    assert add_remove_elements_page.at_page()
    assert add_remove_elements_page.check_elements_count() == 5

def test_add_remove_elements_page_remove_elements(add_remove_elements_page):
    add_remove_elements_page.navigate_to_page()

    [add_remove_elements_page.add_element() for _ in range(5)]
    [add_remove_elements_page.remove_element() for _ in range(4)]

    assert add_remove_elements_page.at_page()
    assert add_remove_elements_page.check_elements_count() == 1



