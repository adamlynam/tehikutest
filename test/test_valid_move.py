from tictactoe import move_has_already_been_taken


def test_move_already_taken_returns_false_when_no_moves_have_been_recorded():
    assert move_has_already_been_taken([0, 0], [], []) == False


def test_move_already_taken_returns_true_when_move_was_taken_by_nought():
    assert move_has_already_been_taken([0, 0], [[0, 0]], []) == True


def test_move_already_taken_returns_true_when_move_was_taken_by_cross():
    assert move_has_already_been_taken([0, 0], [], [[0, 0]]) == True
