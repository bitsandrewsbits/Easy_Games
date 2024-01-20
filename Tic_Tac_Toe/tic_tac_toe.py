#my version of game Tic-Tac-Toe

def display_board(cells):
    # 2-Creating
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    index = 0

    for i in range(25):
        if i % 8 == 0:
            print('+' + ' -' * 7, ' -' * 7, ' -' * 7, sep = ' +', end = ' +\n')
        elif i % 2 != 0:
            print()
        else:
            if i % 4 == 0:
                for i in range(49):
                    if i % 16 == 0:
                        if i == 48:
                            print('|')
                        else:
                            print('|', end = '')
                    elif i % 8 == 0:
                        print(cells[index], end = '')
                        index += 1
                    else:
                        print(' ', end = '')
            else:
                print('|' + '  ' * 7, '  ' * 7, '  ' * 7, sep = ' |', end = ' |\n')
                
##display_board()

# + - - - - - - - + - - - - - - - +
#         N               N   
# |

# |

# |

# + - - - - - - - +

def make_list_of_fields(cells, filled_cell, who_move):
    #filled_cell = [-i-] - coordinat on board (position in list)
    #updates the board according to the user's decision.

    for i in range(len(cells)):
        if i == filled_cell and cells[i] != 'X' and cells[i] != 'O':
            if who_move == 'X':
                cells[i] = 'X'
                return 'O'
            else:
                cells[i] = 'O'
                return 'X'

import random

def enter_move(cells, who):
    # The function accepts the board current status, asks the user about their move,
    # checks the input and return cell's number

    if who == 'X':
        count = 0
        while count < 20:
            rand_number = random.randint(0, 8)
            if cells[rand_number] != 'X' and cells[rand_number] != 'O':
                return rand_number
            count += 1
            
        return rand_number
            
        
    elif who == 'O':
        while True:
            display_board(cells)
            user_cell = int(input("Enter your number [1 - 9][or -1 to exit]: "))
            if user_cell == -1:
                user_cell = -1
                print('Bye')
                return user_cell
                break
            elif user_cell < 0 or user_cell > 10:
                print("Error number of cell! Try again")
                continue
            else:
                for i in range(0, 9):
                    if i == (user_cell - 1) and (cells[i] != 'X' or cells[i] != 'O'):
                        return user_cell - 1

def check_empty_fields(cells):
    flag = True

    for i in range(len(cells)):
        if cells[i] != 'X' and cells[i] != 'O':
            return False

    return flag

def victory_for(board):
    
    # The function analyzes the board status in order to check if
    # the player using 'O's or 'X's has won the game
    length = len(board)
    i = 0

    #first combinations
    while i < length:
        if board[i:(i + 3)].count('X') == 3 or board[i:(i + 3)].count('O') == 3:
            print("Var-1")
            print("Winner is", board[i])
            return True
        i += 3

    #secound combinations
    i = 0
    while i < 3:
        if board[i] == board[i + 3] and board[i + 3] == board[i + 6]:
            print("Var-2")
            print("Winner is", board[i])
            return True
        i += 1
        
    #third combinations 
    i = 4
    cnt = 0
    while cnt < 3:
        if board[cnt] == board[i] and board[i] == board[(2 * i) - cnt]:
            print("Var-3")
            print("Winner is", board[i])
            return True
        cnt += 2
                
    if check_empty_fields(board):
        print("This is PAT! 1-1. Okay.")
        return True

    return False

board = [i for i in range(1, 10)]  #cells for board

def start_game(computer_move, cells):
    
    #first moving for computer!
    who_move = computer_move

    while True:
        flag = victory_for(cells)
        if flag:
            display_board(cells)
            print("Game finish. Bye.")
            break
        else:
            number_cell = enter_move(cells, who_move)
            if number_cell == -1:
                print("Game was interrupted. Bye.")
                break
            who_move = make_list_of_fields(cells, number_cell, who_move)  #X <-> O

#testing game
start_game('X', board)
