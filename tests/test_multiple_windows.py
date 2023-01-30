MULTIPLE_WINDOWS_TITLE_TEXT = "Opening a new window"
NEW_WINDOW_TEXT = "New Window"
SIZE_HANDLES_2 = 2
SIZE_HANDLES_3 = 3


def test_multiple_windows(multiple_windows_page) -> None:
    multiple_windows_page.navigate_to_page()

    assert multiple_windows_page.at_page()


def test_multiple_windows_title_text(multiple_windows_page) -> None:
    multiple_windows_page.navigate_to_page()

    assert multiple_windows_page.at_page()
    assert multiple_windows_page.get_title_text() == MULTIPLE_WINDOWS_TITLE_TEXT


def test_multiple_windows_new_window(multiple_windows_page) -> None:
    multiple_windows_page.navigate_to_page()
    multiple_windows_page.new_window()
    two_window = multiple_windows_page.window_handle_by_index(1)
    multiple_windows_page.switch_window(two_window)

    assert multiple_windows_page.get_title_text() == NEW_WINDOW_TEXT
    assert multiple_windows_page.at_new_page()


def test_multiple_windows_new_window_and_return(multiple_windows_page) -> None:
    multiple_windows_page.navigate_to_page()
    first_window = multiple_windows_page.window_handle_by_index(0)
    multiple_windows_page.new_window()
    two_window = multiple_windows_page.window_handle_by_index(1)
    multiple_windows_page.switch_window(first_window)

    assert multiple_windows_page.at_page()
    assert multiple_windows_page.get_title_text() == MULTIPLE_WINDOWS_TITLE_TEXT
    assert multiple_windows_page.size_handles() == SIZE_HANDLES_2


def test_multiple_windows_new_windows(multiple_windows_page) -> None:
    multiple_windows_page.navigate_to_page()
    first_window = multiple_windows_page.window_handle_by_index(0)
    multiple_windows_page.new_window()
    two_window = multiple_windows_page.window_handle_by_index(1)
    multiple_windows_page.switch_window(first_window)
    multiple_windows_page.new_window()
    three_window = multiple_windows_page.window_handle_by_index(2)
    multiple_windows_page.switch_window(three_window)

    assert multiple_windows_page.get_title_text() == NEW_WINDOW_TEXT
    assert multiple_windows_page.at_new_page()
    assert multiple_windows_page.size_handles() == SIZE_HANDLES_3
