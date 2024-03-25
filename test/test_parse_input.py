import pytest
from tictactoe import parse_input_for_coordinates


def test_parse_input_adjusts_to_zero_based_index():
    assert parse_input_for_coordinates("1,1") == [0, 0]


def test_unparsable_data_throws_an_exception():
    with pytest.raises(ValueError) as e_info:
        parse_input_for_coordinates("asdasd")


def test_line_index_is_too_high_throws_an_exception():
    with pytest.raises(ValueError) as e_info:
        parse_input_for_coordinates("55,3")


def test_column_index_is_too_high_throws_an_exception():
    with pytest.raises(ValueError) as e_info:
        parse_input_for_coordinates("3,55")


def test_line_index_is_too_low_throws_an_exception():
    with pytest.raises(ValueError) as e_info:
        parse_input_for_coordinates("0,1")


def test_column_index_is_too_low_throws_an_exception():
    with pytest.raises(ValueError) as e_info:
        parse_input_for_coordinates("1,0")
