import time

from pages.add_remove_elements_page import Add_remove_elements_page


def test_add_remove_elements_page_should_work():
    page = Add_remove_elements_page()
    page.navigate_to_add_remove_elements_page()

    page.add_element()
    page.add_elements(5)

    page.remove_element()
    page.remove_elements(5)
    time.sleep(1)

    assert page.check_page() is True
    assert page.check_title() == "Add/Remove Elements"