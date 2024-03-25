def parse_input_for_coordinates(text_input: str) -> list[int]:
    parts = text_input.split(",")

    # validate user input
    try:
        line_index = int(parts[0])
        column_index = int(parts[1])
    except Exception:
        raise ValueError("Could not parse input as coordinates")
    if line_index < 1:
        raise ValueError("Line index cannot be less than 1")
    if column_index < 1:
        raise ValueError("Column index cannot be less than 1")
    if line_index > 3:
        raise ValueError("Line index cannot be greater than 3")
    if column_index > 3:
        raise ValueError("Column index cannot be greater than 3")

    return [line_index - 1, column_index - 1]


def move_has_already_been_taken(
    move: list[int], noughts_moves: list[list[int]], crosses_moves: list[list[int]]
) -> bool:
    if move in noughts_moves or move in crosses_moves:
        return True

    return False


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


all_moves = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]


def board_is_full(noughts_moves: list[list[int]], crosses_moves: list[list[int]]):
    for move in all_moves:
        if move not in noughts_moves and move not in crosses_moves:
            return False

    return True


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
                move = parse_input_for_coordinates(text_input)

                # check for valid move
                if move_has_already_been_taken(move, noughts_moves, crosses_moves):
                    print("Unfortunately, that space is already taken")
                    print("Please enter another move")
                else:
                    # record the move
                    if noughts_turn:
                        noughts_moves.append(move)
                        noughts_turn = False
                    else:
                        crosses_moves.append(move)
                        noughts_turn = True

                    # display the game board
                    display_board(render_board(noughts_moves, crosses_moves))

                    # check for win
                    player_that_won = player_has_won(noughts_moves, crosses_moves)
                    if player_that_won != None:
                        if player_that_won == "o":
                            print("Congratulations noughts (o), you have won")
                        if player_that_won == "x":
                            print("Congratulations crosses (x), you have won")
                        exiting = True
                    else:
                        # check for a tie
                        if board_is_full(noughts_moves, crosses_moves):
                            print(
                                "The board has filled up without a winner, the game ends in a tie"
                            )
                            exiting = True

            except Exception as ex:
                print(ex)
                print("Please enter your move again")

    print("Thank you for playing Tic Tac Toe by Adam Lynam")
