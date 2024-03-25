def render_horitonzal_line():
    return "---------"


def calculate_move(
    play_line_index: int,
    play_column_index: int,
    nought_moves: list[list[int]],
    crosses_moves: list[list[int]],
):
    if [play_line_index, play_column_index] in nought_moves:
        return "o"
    elif [play_line_index, play_column_index] in crosses_moves:
        return "x"
    else:
        return " "


def render_play_line(
    play_line_index: int, nought_moves: list[list[int]], crosses_moves: list[list[int]]
):
    position_zero = calculate_move(play_line_index, 0, nought_moves, crosses_moves)
    position_one = calculate_move(play_line_index, 1, nought_moves, crosses_moves)
    position_two = calculate_move(play_line_index, 2, nought_moves, crosses_moves)
    return f"{position_zero} | {position_one} | {position_two}"


def render_board(
    nought_moves: list[list[int]], crosses_moves: list[list[int]]
) -> list[str]:
    board = []
    board.append(render_play_line(0, nought_moves, crosses_moves))
    board.append(render_horitonzal_line())
    board.append(render_play_line(1, nought_moves, crosses_moves))
    board.append(render_horitonzal_line())
    board.append(render_play_line(2, nought_moves, crosses_moves))
    return board
