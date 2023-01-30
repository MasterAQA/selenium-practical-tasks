INPUTS_TITLE_TEXT = "Inputs"

INPUT_VALUE_1 = 112
INPUT_VALUE_2 = 4
INPUT_VALUE_3 = -4


def test_imputs(inputs_page) -> None:
    inputs_page.navigate_to_page()

    assert inputs_page.at_page()


def test_imputs_title_text(inputs_page) -> None:
    inputs_page.navigate_to_page()

    assert inputs_page.at_page()
    assert inputs_page.get_title_text() == INPUTS_TITLE_TEXT


def test_imputs_enter_int(inputs_page) -> None:
    inputs_page.navigate_to_page()
    inputs_page.input_int(112)

    assert inputs_page.at_page()
    assert inputs_page.get_input_value() == INPUT_VALUE_1


def test_imputs_arrow_up(inputs_page) -> None:
    inputs_page.navigate_to_page()
    [inputs_page.input_arrow_up() for _ in range(4)]

    assert inputs_page.at_page()
    assert inputs_page.get_input_value() == INPUT_VALUE_2


def test_imputs_arrow_down(inputs_page) -> None:
    inputs_page.navigate_to_page()
    [inputs_page.input_arrow_down() for _ in range(4)]

    assert inputs_page.at_page()
    assert inputs_page.get_input_value() == INPUT_VALUE_3
