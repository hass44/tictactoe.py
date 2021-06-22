
import random


def display_board(board):
    print('\n' * 100)
    print("\n")
    print("    |     |")
    print(" " + board[1] + "  |  " + board[2] + "  |  " + board[3])
    print("    |     |")
    print("---------------")
    print("    |     |")
    print(" " + board[4] + "  |  " + board[5] + "  |  " + board[6])
    print("    |     |")
    print("---------------")
    print("    |     |")
    print(" " + board[7] + "  |  " + board[8] + "  |  " + board[9])
    print("    |     |")

def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ')
        marker = marker.upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def put_marker(board, marker, position):
    board[position] = marker

def check_win(board, mark):
    return((board[1] == mark and board[2] == mark and board[3] == mark) or
           (board[4] == mark and board[5] == mark and board[6] == mark) or
           (board[7] == mark and board[8] == mark and board[9] == mark) or
           (board[1] == mark and board[4] == mark and board[7] == mark) or
           (board[2] == mark and board[5] == mark and board[8] == mark) or
           (board[3] == mark and board[6] == mark and board[9] == mark) or
           (board[1] == mark and board[5] == mark and board[9] == mark) or
           (board[3] == mark and board[5] == mark and board[7] == mark))

def who_first():
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def check_space(board, position):
    return board[position] == ' '

def if_board_full(board):
    for i in range(1,10):
        if check_space(board, i):
            return False
    return True

def player_pick_position(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not check_space(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position

def replay():
    return input("Do you wish to play again Y/N").upper().startswith('Y')

print("Welcome to Tic Tac Toe by Hassaan!")

while True:
    myBoard = [' '] * 10                                # initialise board
    player1_marker, player2_marker = player_input()     # get markers for both players

    whose_turn = who_first()                            # pick who goes first
    print(whose_turn + " will go first")

    play_game = input("Ready to play? Y/N :")
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if whose_turn == 'Player 1':                    # Player 1 turn
            display_board(myBoard)
            position = player_pick_position(myBoard)
            put_marker(myBoard, player1_marker, position)

            if check_win(myBoard, player1_marker):
                display_board(myBoard)
                print("Player 1 has won the game!")
                game_on = False
            else:
                if if_board_full(myBoard):
                    display_board(myBoard)
                    print("This game is a draw!")
                    break
                else:
                    whose_turn = 'Player 2'

        else:
            display_board(myBoard)
            position = player_pick_position(myBoard)
            put_marker(myBoard, player2_marker, position)

            if check_win(myBoard, player2_marker):
                display_board(myBoard)
                print("CPlayer 2 has won the game")
                game_on = False
            else:
                if if_board_full(myBoard):
                    display_board(myBoard)
                    print("This game is a draw!")
                    break
                else:
                    whose_turn = 'Player 1'

    if not replay():
        break
