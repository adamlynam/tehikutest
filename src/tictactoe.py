def parse_input_for_coordinates(text_input: str) -> list[int]:
    parts = text_input.split(",")
    return [int(parts[0]), int(parts[1])]


def render_horitonzal_line() -> str:
    return "---------"


def calculate_move(
    play_line_index: int,
    play_column_index: int,
    nought_moves: list[list[int]],
    crosses_moves: list[list[int]],
) -> str:
    if [play_line_index, play_column_index] in nought_moves:
        return "o"
    elif [play_line_index, play_column_index] in crosses_moves:
        return "x"
    else:
        return " "


def render_play_line(
    play_line_index: int, nought_moves: list[list[int]], crosses_moves: list[list[int]]
) -> str:
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


def display_board(board):
    for line in board:
        print(line)


# primary entry point for the app
if __name__ == "__main__":

    # game state
    exiting: bool = False
    noughts_turn: bool = True
    noughts_moves: list[list[int]] = []
    crosses_moves: list[list[int]] = []

    # game loop
    print("Welcome to Tic Tac Toe")
    while not exiting:
        if noughts_turn:
            print("It is noughts (o) turn")
        else:
            print("It is crosses (x) turn")
        print(
            "TIP: Coordinates should be entered as row number, column number. e.g. 1,1 for top left corner (type exit to quit)"
        )
        print("Please enter your move:")
        text_input = input()
        if text_input == "exit":
            exiting = True
        else:
            try:
                coordinates = parse_input_for_coordinates(text_input)
                # check for valid move first
                if noughts_turn:
                    noughts_moves.append(coordinates)
                    noughts_turn = False
                else:
                    crosses_moves.append(coordinates)
                    noughts_turn = True
                display_board(render_board(noughts_moves, crosses_moves))
            except Exception:
                print("Your move could not be understood, try again")

    print("Thank you for playing Tic Tac Toe by Adam Lynam")
