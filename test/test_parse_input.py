from tictactoe import parse_input_for_coordinates


def test_parse_input_can_extract_coordinates():
    assert parse_input_for_coordinates("1,1") == [1, 1]
