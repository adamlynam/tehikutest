from tictactoe import board_is_full


def test_board_is_not_full_for_empty_board():
    assert board_is_full([], []) == False


def test_board_is_full_when_all_spaces_are_used():
    assert (
        board_is_full(
            [[0, 0], [0, 1], [1, 2], [2, 1], [2, 2]], [[0, 2], [1, 0], [1, 1], [2, 0]]
        )
        == True
    )
