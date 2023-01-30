BASIC_AUTH_TITLE_TEXT = "Basic Auth"
PASS_BASIC_AUTH_PART_OF_TEXT = "Congratulations!"


def test_basic_auth_page_pass_auth(basic_auth_page) -> None:
    basic_auth_page.pass_basic_auth("admin", "admin")
    basic_auth_page.navigate_to_page()

    assert basic_auth_page.at_page_admin()


def test_basic_auth_page_title_and_content(basic_auth_page) -> None:
    basic_auth_page.pass_basic_auth("admin", "admin")
    basic_auth_page.navigate_to_page()

    assert basic_auth_page.at_page_admin()
    assert basic_auth_page.get_title_text() == BASIC_AUTH_TITLE_TEXT
    assert PASS_BASIC_AUTH_PART_OF_TEXT in basic_auth_page.get_content_text()
