def render_horitonzal_line() -> str:
    return "---------"


def render_play_space(
    play_line_index: int,
    play_column_index: int,
    noughts_moves: list[list[int]],
    crosses_moves: list[list[int]],
) -> str:
    if [play_line_index, play_column_index] in noughts_moves:
        return "o"
    elif [play_line_index, play_column_index] in crosses_moves:
        return "x"
    else:
        return " "


def render_play_line(
    play_line_index: int, noughts_moves: list[list[int]], crosses_moves: list[list[int]]
) -> str:
    position_zero = render_play_space(play_line_index, 0, noughts_moves, crosses_moves)
    position_one = render_play_space(play_line_index, 1, noughts_moves, crosses_moves)
    position_two = render_play_space(play_line_index, 2, noughts_moves, crosses_moves)
    return f"{position_zero} | {position_one} | {position_two}"


def render_board(
    noughts_moves: list[list[int]], crosses_moves: list[list[int]]
) -> list[str]:
    board = []
    board.append(render_play_line(0, noughts_moves, crosses_moves))
    board.append(render_horitonzal_line())
    board.append(render_play_line(1, noughts_moves, crosses_moves))
    board.append(render_horitonzal_line())
    board.append(render_play_line(2, noughts_moves, crosses_moves))
    return board
