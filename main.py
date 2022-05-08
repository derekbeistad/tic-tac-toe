"""
2 Users: userA and userB.
Game will randomly decide who goes first.
"""

from random import choice

EMPTY_BOARD = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_']
]

BOARD_LABELS = """
Tic Tac Toe Position Labels:
A1 | A2 | A3
------------
B1 | B2 | B3
------------
C1 | C2 | C3
"""


def print_board():
    for n in range(3):
        print(game_board[n])
    print("\n")


def create_row_index():
    if 'A' in chosen_position:
        game_board_row = 0
    elif 'B' in chosen_position:
        game_board_row = 1
    elif 'C' in chosen_position:
        game_board_row = 2
    else:
        print("invalid input")
    return game_board_row


def create_col_index():
    if '1' in chosen_position:
        game_board_col = 0
    elif '2' in chosen_position:
        game_board_col = 1
    elif '3' in chosen_position:
        game_board_col = 2
    else:
        print("invalid input")
    return game_board_col


def check_position_open(play_row, play_col):
    if game_board[play_row][play_col] == '_':
        return False
    else:
        return True


def check_for_winner():
    global game_over
    for n in range(3):
        if game_board[n] == ['A', 'A', 'A'] or game_board[n] == ['B', 'B', 'B']:
            if 'A' in game_board[n]:
                game_over = True
                print(f"{first_player} wins!")
                return True
            else:
                game_over = True
                print(f"{second_player} wins!")
                return True
        elif game_board[0][n] == 'A' and game_board[1][n] == 'A' and game_board[2][n] == 'A' or game_board[0][
            n] == 'A' and game_board[1][n] == 'A' and game_board[2][n] == 'A':
            if 'A' in game_board[0][n]:
                game_over = True
                print(f"{first_player} wins!")
                return True
            else:
                game_over = True
                print(f"{second_player} wins!")
                return True

    if game_board[0][0] == 'A' and game_board[1][1] == 'A' and game_board[2][2] == 'A' or game_board[0][2] == 'A' and \
            game_board[1][1] == 'A' and game_board[2][0] == 'A':
        game_over = True
        print(f"{first_player} wins!")
        return True
    elif game_board[0][0] == 'B' and game_board[1][1] == 'B' and game_board[2][2] == 'B' or game_board[0][2] == 'B' and \
            game_board[1][1] == 'B' and game_board[2][0] == 'B':
        game_over = True
        print(f"{second_player} wins!")
        return True


def first_players_turn():
    global chosen_position
    chosen_position = input(f"{first_player}, enter the position you'd like to play: ").upper()
    row_index = create_row_index()
    col_index = create_col_index()
    if check_position_open(play_row=row_index, play_col=col_index):
        print("Position already taken, try again.")
        first_players_turn()
    else:
        game_board[row_index][col_index] = 'A'
        print_board()

        # Check for winner
        if check_for_winner():
            return True


def second_players_turn():
    global chosen_position
    chosen_position = input(f"{second_player}, enter the position you'd like to play: ").upper()
    row_index = create_row_index()
    col_index = create_col_index()
    if check_position_open(play_row=row_index, play_col=col_index):
        print("Position already taken, try again.")
        second_players_turn()
    else:
        game_board[row_index][col_index] = 'B'
        print_board()

        # Check for winner
        if check_for_winner():
            return True


game_over = False
userA = input("Enter the name for the first player: ")
userB = input("Enter the name for the second player: ")
game_board = EMPTY_BOARD

# find starting player
player = [userA, userB]
first_player = choice(player)
if userA == first_player:
    second_player = userB
else:
    second_player = userA
print(f"{first_player} is player 'A' and goes first. {second_player} is player 'B' goes second.")

while not game_over:
    # display board
    print(BOARD_LABELS)
    print_board()

    # First players plays
    if first_players_turn():
        game_over = True
        break

    # Second player plays
    if second_players_turn():
        game_over = True
        break
