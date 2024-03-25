def move_has_already_been_taken(
    move: list[int], noughts_moves: list[list[int]], crosses_moves: list[list[int]]
) -> bool:
    if move in noughts_moves or move in crosses_moves:
        return True

    return False


def player_has_diagonal_win(moves):
    if [0, 0] in moves and [1, 1] in moves and [2, 2] in moves:
        return True
    if [0, 2] in moves and [1, 1] in moves and [2, 0] in moves:
        return True
    return False


def player_has_horizontal_win(moves):
    if [0, 0] in moves and [0, 1] in moves and [0, 2] in moves:
        return True
    if [1, 0] in moves and [1, 1] in moves and [1, 2] in moves:
        return True
    if [2, 0] in moves and [2, 1] in moves and [2, 2] in moves:
        return True
    return False


def player_has_vertical_win(moves):
    if [0, 0] in moves and [1, 0] in moves and [2, 0] in moves:
        return True
    if [0, 1] in moves and [1, 1] in moves and [2, 1] in moves:
        return True
    if [0, 2] in moves and [1, 2] in moves and [2, 2] in moves:
        return True
    return False


def player_has_won(
    noughts_moves: list[list[int]], crosses_moves: list[list[int]]
) -> str | None:
    if player_has_diagonal_win(noughts_moves):
        return "o"
    if player_has_diagonal_win(crosses_moves):
        return "x"
    if player_has_horizontal_win(noughts_moves):
        return "o"
    if player_has_horizontal_win(crosses_moves):
        return "x"
    if player_has_vertical_win(noughts_moves):
        return "o"
    if player_has_vertical_win(crosses_moves):
        return "x"
    return None


all_moves = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]


def board_is_full(noughts_moves: list[list[int]], crosses_moves: list[list[int]]):
    for move in all_moves:
        if move not in noughts_moves and move not in crosses_moves:
            return False

    return True
