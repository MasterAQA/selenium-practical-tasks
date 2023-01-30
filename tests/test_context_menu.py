CONTEXT_MENU_TITLE_TEXT = "Context Menu"
ALERT_TEXT = "You selected a context menu"


def test_context_menu(context_menu_page) -> None:
    context_menu_page.navigate_to_page()

    assert context_menu_page.at_page()


def test_context_menu_title_text(context_menu_page) -> None:
    context_menu_page.navigate_to_page()

    assert context_menu_page.at_page()
    assert context_menu_page.get_title_text() == CONTEXT_MENU_TITLE_TEXT


def test_context_menu_alert_text(context_menu_page) -> None:
    context_menu_page.navigate_to_page()
    context_menu_page.right_click_on_context_zone()

    assert context_menu_page.alert_text() == ALERT_TEXT
    context_menu_page.alert_accept()


def test_context_menu_alert_accept(context_menu_page) -> None:
    context_menu_page.navigate_to_page()
    context_menu_page.right_click_on_context_zone()
    context_menu_page.alert_accept()

    assert context_menu_page.at_page()
    assert context_menu_page.get_title_text() == CONTEXT_MENU_TITLE_TEXT


def test_context_menu_alert_dismiss(context_menu_page) -> None:
    context_menu_page.navigate_to_page()
    context_menu_page.right_click_on_context_zone()
    context_menu_page.alert_dismiss()

    assert context_menu_page.at_page()
    assert context_menu_page.get_title_text() == CONTEXT_MENU_TITLE_TEXT
