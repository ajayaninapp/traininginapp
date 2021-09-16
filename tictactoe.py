def display_board(board):
     # Remember, this only works in jupyter!
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print("\n\n\n\n")


def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_marker(board, marker, position):
    board[position] = marker

def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'PC'
    else:
        return 'Player '

def space_check(board, position):
    
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position


def pc_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = random.randint(1,9)
        
    return position



def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


print('Welcome to Tic Tac Toe!')
x=0
j=0
round_history=[[0]*9]*10
user_input=['']*10
round_no=0
history_board=[' '] * 10
while True:
    # Reset the board
    theBoard = [' '] * 10
   
    position_history=[0]*9
    i=0
    
    player1_marker, player2_marker = player_input()
    user_input[j]=player1_marker
    turn = 'Pc'
    print(' PC will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)
            position_history[i]=position
            i=i+1

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Pc'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = pc_choice(theBoard)
            place_marker(theBoard, player2_marker, position)
            position_history[i]=position
            i=i+1

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Pc has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'
    round_history[j]=position_history
    j=j+1
    


    if not replay():
        break

round_no=int(input("enter round:\n"))

if user_input[round_no-1]=='':
    print ("no round")
if user_input[round_no-1]=='X':
    print ("hi")
    print(round_history[round_no-1])
    for item in range(0,len(round_history[round_no-1])):
        if round_history[round_no-1][item]==0:
            break
        else:
            if x==0:
                 history_board[round_history[round_no-1][item]]='O'
                 display_board(history_board)
                 x=1
           
            
            
            elif x==1:
                 history_board[round_history[round_no-1][item]]='x'
                 display_board(history_board)
                 x=0
            
             
            
          

    
