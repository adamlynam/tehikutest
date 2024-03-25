from render import render_board


def test_render_board_returns_empty_board():
    board_state = render_board([], [])
    assert board_state[0] == "  |   |  "
    assert board_state[1] == "---------"
    assert board_state[2] == "  |   |  "
    assert board_state[3] == "---------"
    assert board_state[4] == "  |   |  "


def test_render_board_with_nought_move():
    board_state = render_board([[0, 0]], [])
    assert board_state[0] == "o |   |  "
    assert board_state[1] == "---------"
    assert board_state[2] == "  |   |  "
    assert board_state[3] == "---------"
    assert board_state[4] == "  |   |  "


def test_render_board_with_crosses_move():
    board_state = render_board([], [[2, 2]])
    assert board_state[0] == "  |   |  "
    assert board_state[1] == "---------"
    assert board_state[2] == "  |   |  "
    assert board_state[3] == "---------"
    assert board_state[4] == "  |   | x"
