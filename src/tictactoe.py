def parse_input_for_coordinates(text_input: str) -> list[int]:
    parts = text_input.split(",")
    return [int(parts[0]), int(parts[1])]


def render_horitonzal_line() -> str:
    return "---------"


def calculate_move(
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
    position_zero = calculate_move(play_line_index, 0, noughts_moves, crosses_moves)
    position_one = calculate_move(play_line_index, 1, noughts_moves, crosses_moves)
    position_two = calculate_move(play_line_index, 2, noughts_moves, crosses_moves)
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


def display_board(board: list[str]):
    for line in board:
        print(line)


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
                # extract the move from the user input
                coordinates = parse_input_for_coordinates(text_input)
                # TODO: check for valid move first

                # record the move
                if noughts_turn:
                    noughts_moves.append(coordinates)
                    noughts_turn = False
                else:
                    crosses_moves.append(coordinates)
                    noughts_turn = True

                # display the game board
                display_board(render_board(noughts_moves, crosses_moves))

                # check for win
                player_that_won = player_has_won(noughts_moves, crosses_moves)
                if player_that_won != None:
                    if player_that_won == "o":
                        print("Congratulations noughts, you have won")
                    if player_that_won == "x":
                        print("Congratulations crosses, you have won")
                    exiting = True
            except Exception:
                print("Your move could not be understood, try again")

    print("Thank you for playing Tic Tac Toe by Adam Lynam")
