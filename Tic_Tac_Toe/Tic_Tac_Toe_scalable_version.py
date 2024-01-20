#my version of game Tic-Tac-Toe - changed
#In this version of game - I believe, you will can change size of board.

boards_side = int(input("Enter size of board's side: "))

board = [i for i in range(boards_side * boards_side)]

#paremeters for display game's board
amount_pluses = boards_side + 1                    #к-во перегородок для доски
amount_lines = boards_side * 7 + amount_pluses     #к-во строк c перегородками
amount_columns = boards_side * 15 + amount_pluses  #к-во столбцов с перегородками

def display_board(cells):

    index = 0
    
##    print("amount_columns =", amount_columns)
        
    for i in range(amount_lines):
##    i = 0
##    total_counter = 0
    
##    while total_counter < amount_columns:
##        if i == 8:
##            total_counter += i
##            i = 0

        if i % 8 == 0:
            print('+', end = '')
            for i in range(boards_side):
                if i == boards_side - 1:
                    print(' -' * 7 + ' +')
                    continue
                print(' -' * 7, end = ' +')
        elif i % 4 == 0:

            left_whitespaces = 7
            right_whitespaces = 7
            tmp_len_number = 1
            indicator = 0
            
            print('|', end = '')
            for j in range(boards_side):
                if len(str(cells[index])) == 1:
                    left_whitespaces = 7
                    right_whitespaces = 7
                    tmp_len_number = len(str(cells[index]))
                    print(' ' * left_whitespaces, end = '')
                    print(str(cells[index]) + ' ' * right_whitespaces, end = '|')
                    index += 1
                    continue
                elif len(str(cells[index])) >= 2 and (len(str(cells[index])) - tmp_len_number > 0):
                    if tmp_len_number % 2 == 0:
                        right_whitespaces -= 1
                    elif (len(str(cells[index])) - tmp_len_number) == 2:
                        left_whitespaces -= 1
                        right_whitespaces -= 1
                    else:
                        left_whitespaces -= 1
                        
                    tmp_len_number = len(str(cells[index]))

                if j == boards_side - 1:                   
                    print(' ' * left_whitespaces, end = '')
                    print(str(cells[index]) + ' ' * right_whitespaces, end = '|')
                    print()
                else:
                    print(' ' * left_whitespaces, end = '')
                    print(str(cells[index]) + ' ' * right_whitespaces, end = '|')
                index += 1
                indicator += 1

                
        elif i % 2 != 0:
            print()
        else:
            print('|', end = '')
            for k in range(boards_side):
                if k == boards_side - 1:
                    print('  ' * 7 + ' |')
                    continue
                print('  ' * 7, end = ' |')
        i += 1
                
##display_board(test_side, board)

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
    return 'O'

import random

def enter_move(boards_side, cells, who):
    # The function accepts the board current status, asks the user about their move,
    # checks the input and return cell's number

    if who == 'X':
        while True:
            rand_number = random.randint(0, len(cells) - 1)
            if cells[rand_number] != 'X' and cells[rand_number] != 'O':
                return rand_number
            
        return rand_number
    
    elif who == 'O':
        while True:
            display_board(cells)
            user_cell = int(input("Enter your number [1 - " + str(boards_side * boards_side) + "][or -1 to exit]: "))
            if user_cell == -1:
                user_cell = -1
                print('Bye')
                return user_cell
            elif user_cell < 0 or user_cell > boards_side * boards_side:
                print("Error number of cell! Try again")
            else:
                for i in range(boards_side * boards_side):
                    if i == user_cell and cells[i] != 'X' and cells[i] != 'O':
                        return user_cell

def check_empty_fields(cells):
    flag = True

    for i in range(len(cells)):
        if cells[i] != 'X' and cells[i] != 'O':
            return False

    return flag

def victory_for(board, boards_side):
    
    # The function analyzes the board status in order to check if
    # the player using 'O's or 'X's has won the game
    length = len(board)
    tmp_matrix = []
    k = 0
    
    while k < length:
        arr = []
        for j in range(boards_side):
            arr.append(board[k + j])
        tmp_matrix.append(arr)
        k += boards_side
        
##    print(tmp_matrix)
    
    #first combinations

    for i in range(boards_side):
        if tmp_matrix[i].count('X') == boards_side or tmp_matrix[i].count('O') == boards_side:
            print("Var-1")
            print("Winner is", tmp_matrix[i][0])
            return True
        
    #secound combinations

    for i in range(boards_side):
        tmp_str = ''
        for j in range(boards_side):
            tmp_str += str(tmp_matrix[j][i])    
        if tmp_str == 'X' * boards_side or tmp_str == 'O' * boards_side:
            print("Var-2")
            print("Winner is", tmp_str[0])
            return True

    #third combinations

    tmp_str = ''
    for i in range(boards_side):
        for j in range(boards_side):
            if i == j:
                tmp_str += str(tmp_matrix[i][j])

    if tmp_str == 'X' * boards_side or tmp_str == 'O' * boards_side:
        print("Var-3")
        print("Winner is", tmp_str[0])
        return True

    tmp_str = ''
    for i in range(boards_side):
        for j in range(boards_side - 1, -1, -1):
            if i == boards_side - j - 1:
##                print(tmp_matrix[i][j])
                tmp_str += str(tmp_matrix[i][j])

##    print(tmp_str)

    if tmp_str == 'X' * boards_side or tmp_str == 'O' * boards_side:
        print("Var-3")
        print("Winner is", tmp_str[0])
        return True

        
    if check_empty_fields(board):
        print("This is PAT! 1-1. Okay.")
        return True

    return False

##board = [i for i in range(1, 10)]  #cells for board

def start_game(computer_move, cells):
    
    #first moving for computer!
    who_move = computer_move
    test_indicator = 0

    while True:
        flag = victory_for(cells, boards_side)
##        print('flag =', flag)
        if flag:
            display_board(cells)
            print("Game finish. Bye.")
            break
        number_cell = enter_move(boards_side, cells, who_move)
        if number_cell == -1:
            print("Game was interrupted. Bye.")
            break
        who_move = make_list_of_fields(cells, number_cell, who_move)  #X <-> O
##        print('who_move =', who_move)
##        print("indicator =", test_indicator)
##        test_indicator += 1

#testing game
start_game('X', board)
