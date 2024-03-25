from game_logic import player_has_won


def test_nobody_has_won_with_empty_board():
    assert player_has_won([], []) == None


def test_noughts_has_won_with_diagonal_line():
    assert player_has_won([[0, 0], [1, 1], [2, 2]], []) == "o"


def test_crosses_has_won_with_diagonal_line():
    assert player_has_won([], [[0, 2], [1, 1], [2, 0]]) == "x"


def test_noughts_has_won_with_horizontal_line():
    assert player_has_won([[0, 0], [0, 1], [0, 2]], []) == "o"


def test_crosses_has_won_with_horizontal_line():
    assert player_has_won([], [[2, 0], [2, 1], [2, 2]]) == "x"


def test_noughts_has_won_with_vertical_line():
    assert player_has_won([[0, 0], [1, 0], [2, 0]], []) == "o"


def test_crosses_has_won_with_vertical_line():
    assert player_has_won([], [[0, 2], [1, 2], [2, 2]]) == "x"
