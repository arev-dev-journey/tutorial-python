import random

def display_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])
test_board = ['#','X','O','X','O','X','O','X','O','X']

def player_input():
    marker = ''

    # Keep asking player 1 to choose X or O
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1, choose X or O: ').upper()
    
    if marker == 'X':
        return('X','O')
    else:
        return('O','X')

def place_marker(board,marker,position):
    board[position] = marker

def win_check(board,mark):
    return((board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[4] == board[5] == board[6] == mark) or 
    (board[7] == board[8] == board[9] == mark) or 
    (board[7] == board[4] == board[1] == mark) or
    (board[8] == board[5] == board[2] == mark) or 
    (board[9] == board[6] == board[3] == mark) or
    (board[7] == board[5] == board[3] == mark) or 
    (board[9] == board[5] == board[1] == mark))

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board,position):

    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position = 0
    
    while position not in range(1,10) or not space_check(board,position):
        position = int(input("Choose a position: (1-9) "))
    return position

def replay():
    return input("Do you want to play again? Enter Yes or No: ").lower().startswith('y')

print("Let's play Tic Tac Toe")

while True:
    # Reset the board
    the_board = [' ']*10
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first')

    play_game = input("Are you ready to play? Enter Y or N. ")

    if play_game.lower() == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player 1's turn

            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player1_marker,position)

            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Congratulations! Player 1 wins the game!!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
        else:
            # Player 2's turn
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player2_marker,position)

            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('Player 2 has Won!!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'
 
    if not replay():
        break

