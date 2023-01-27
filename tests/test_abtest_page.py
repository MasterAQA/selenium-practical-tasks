from pages.abtest_page import AbtestPage

ABTEST_TITLE_TEXT = "A/B Test"
ABTEST_PART_OF_TEXT = "learn different versions"


def test_abtest_page(driver) -> None:
    page = AbtestPage(driver)
    page.navigate_to_abtest_page()

    assert page.at_page()


def test_abtest_page1(abtest_page) -> None:
    abtest_page.navigate_to_abtest_page()

    assert abtest_page.at_page()


def test_abtest_page_title(driver) -> None:
    page = AbtestPage(driver)
    page.navigate_to_abtest_page()

    assert page.at_page()
    assert page.get_title().is_displayed()
    assert ABTEST_TITLE_TEXT in page.get_title_text()


def test_abtest_page_text(driver) -> None:
    page = AbtestPage(driver)
    page.navigate_to_abtest_page()

    assert page.at_page()
    assert page.get_content().is_displayed()
    assert ABTEST_PART_OF_TEXT in page.get_content_text()
