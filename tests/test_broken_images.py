BROKEN_IMAGES_TITLE_TEXT = "Broken Images"
PASS_BASIC_AUTH_PART_OF_TEXT = "Congratulations!"


def test_broken_images(broken_images_page) -> None:
    broken_images_page.navigate_to_page()

    assert broken_images_page.at_page()


def test_broken_images_title_text(broken_images_page) -> None:
    broken_images_page.navigate_to_page()

    assert broken_images_page.at_page()
    assert broken_images_page.get_title_text() == BROKEN_IMAGES_TITLE_TEXT


def test_broken_images_check_image(broken_images_page) -> None:
    broken_images_page.navigate_to_page()

    assert broken_images_page.at_page()
    assert broken_images_page.check_broken_image(3)


def test_broken_images_check_broken_images(broken_images_page) -> None:
    broken_images_page.navigate_to_page()

    assert broken_images_page.at_page()
    assert broken_images_page.check_broken_image(1) == False
    assert broken_images_page.check_broken_image(2) == False
