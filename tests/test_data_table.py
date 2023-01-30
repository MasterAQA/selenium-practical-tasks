import time

import pytest

DATA_TABLE_TITLE_TEXT = "Data Tables"
FBACH_TEXT = "fbach@yahoo.com"
COLUMN_LIST_NAMES = ["John", "Frank", "Jason", "Tim"]
LINE_LIST_CONTENT = [
    "Bach",
    "Frank",
    "fbach@yahoo.com",
    "$51.00",
    "http://www.frank.com",
    "edit delete",
]
DICT_DATA_TABLE_CONTENT = {"Smith": "jsmith@gmail.com", "Bach": "fbach@yahoo.com"}


def test_data_table(data_table_page) -> None:
    data_table_page.navigate_to_page()

    assert data_table_page.at_page()


def test_data_table_title_text(data_table_page) -> None:
    data_table_page.navigate_to_page()

    assert data_table_page.at_page()
    assert data_table_page.get_title_text() == DATA_TABLE_TITLE_TEXT


def test_data_table_column(data_table_page) -> None:
    data_table_page.navigate_to_page()
    time.sleep(2)
    result = data_table_page.values_from_column(2)

    assert data_table_page.at_page()
    assert result == COLUMN_LIST_NAMES


def test_data_table_line(data_table_page) -> None:
    data_table_page.navigate_to_page()
    result = data_table_page.values_from_line(2)

    assert data_table_page.at_page()
    assert result == LINE_LIST_CONTENT


def test_data_table_area_dict(data_table_page) -> None:
    data_table_page.navigate_to_page()
    result = data_table_page.values_from_area(1, 3, 1, 3)

    assert data_table_page.at_page()
    assert result == DICT_DATA_TABLE_CONTENT
