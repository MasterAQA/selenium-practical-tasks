import time

from pages.abtest_page import Abtest_page


def test_abtest_page_should_work():
    page = Abtest_page()
    page.navigate_to_abtest_page()
    time.sleep(1)

    assert page.check_page() is True
    assert "A/B Test" in page.check_title()
    assert "learn different versions" in page.check_text()


