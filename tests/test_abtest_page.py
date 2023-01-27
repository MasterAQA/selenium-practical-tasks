ABTEST_TITLE_TEXT = "A/B Test"
ABTEST_PART_OF_TEXT = "learn different versions"


def test_abtest_page(abtest_page) -> None:
    abtest_page.navigate_to_abtest_page()

    assert abtest_page.at_page()


def test_abtest_page_title(abtest_page) -> None:
    abtest_page.navigate_to_abtest_page()

    assert abtest_page.at_page()
    assert abtest_page.get_title().is_displayed()
    assert ABTEST_TITLE_TEXT in abtest_page.get_title_text()


def test_abtest_page_text(abtest_page) -> None:
    abtest_page.navigate_to_abtest_page()

    assert abtest_page.at_page()
    assert abtest_page.get_content().is_displayed()
    assert ABTEST_PART_OF_TEXT in abtest_page.get_content_text()
