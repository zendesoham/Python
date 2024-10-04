
def display_board(b):
    print('\n')
    print(f" {b[0]} | {b[1]} | {b[2]} ")
    print("---|---|---")
    print(f" {b[3]} | {b[4]} | {b[5]} ")
    print("---|---|---")
    print(f" {b[6]} | {b[7]} | {b[8]} ")
    print('\n')
    
def game_on():
    user_input = 'wrong'
    while user_input.lower() not in ['n','y']:
        user_input = input('do you want to play [y/n] : ')
        if user_input.lower() not in ['n','y']:
            print("incorrect value please enter y or n")
            
    if user_input.lower() == 'y':
        return True
    elif user_input.lower() == 'n':
        return False

def choice():
    user_choice = 'wrong'
    while not user_choice.isdigit():
        user_choice = input("please enter your position [1-9] : ")
        if not user_choice.isdigit():
            print("please enter a digit")
        elif int(user_choice) not in [1,2,3,4,5,6,7,8,9]:
            user_choice = 'wrong'
            print("please enter a digit  1 - 9")
    return int(user_choice)    

def game_on():
    user_input = 'wrong'
    while user_input.lower() not in ['n','y']:
        user_input = input('do you want to play [y/n] : ')
        if user_input.lower() not in ['n','y']:
            print("incorrect value please enter y or n")
            
    if user_input.lower() == 'y':
        return True
    elif user_input.lower() == 'n':
        return False

def win_check(g):
    if  g[0] == g[1] == g[2] == "X" or g[3] == g[4] == g[5] == "X" or g[6] == g[7] == g[8] == "X" or g[0] == g[3] == g[6] == "X" or g[1] == g[4] == g[7] == "X" or g[2] == g[5] == g[8]  == "X" or g[0] == g[4] == g[8] == "X" or g[2] == g[4] == g[6] == "X":
        return "X"
    elif  g[0] == g[1] == g[2] == "O" or g[3] == g[4] == g[5] == "O" or g[6] == g[7] == g[8] == "O" or g[0] == g[3] == g[6] == "O" or g[1] == g[4] == g[7] == "O" or g[2] == g[5] == g[8]  == "O" or g[0] == g[4] == g[8] == "O" or g[2] == g[4] == g[6] == "O":
        return "O"

def alter_board(mark,position,gameboard):
    d = {1:0,2:1,3:2,4:3,5:4,6:5,7:6,8:7,9:8}
    gameboard[d[position]] = mark
    return gameboard

def choice():
    user_choice = 'wrong'
    while not user_choice.isdigit():
        user_choice = input("please enter your position [1-9] : ")
        if not user_choice.isdigit():
            print("please enter a digit")
        elif int(user_choice) not in [1,2,3,4,5,6,7,8,9]:
            user_choice = 'wrong'
            print("please enter a digit  1 - 9")
    return int(user_choice)

def game_on():
    user_input = 'wrong'
    while user_input.lower() not in ['n','y']:
        user_input = input('do you want to play [y/n] : ')
        if user_input.lower() not in ['n','y']:
            print("incorrect value please enter y or n")
            
    if user_input.lower() == 'y':
        return True
    elif user_input.lower() == 'n':
        return False

def win_check(g):
    if  g[0] == g[1] == g[2] == "X" or g[3] == g[4] == g[5] == "X" or g[6] == g[7] == g[8] == "X" or g[0] == g[3] == g[6] == "X" or g[1] == g[4] == g[7] == "X" or g[2] == g[5] == g[8]  == "X" or g[0] == g[4] == g[8] == "X" or g[2] == g[4] == g[6] == "X":
        return "X"
    elif  g[0] == g[1] == g[2] == "O" or g[3] == g[4] == g[5] == "O" or g[6] == g[7] == g[8] == "O" or g[0] == g[3] == g[6] == "O" or g[1] == g[4] == g[7] == "O" or g[2] == g[5] == g[8]  == "O" or g[0] == g[4] == g[8] == "O" or g[2] == g[4] == g[6] == "O":
        return "O"


from IPython.display import clear_output

#control flow

game_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
game_sts = game_on()

while game_sts:
    clear_output()
    display_board(game_board)
    #win check 
    if win_check(game_board) == "X":
        game_sts = False
        print("X wins!!!!!!!!!!!!!!!!!!!!1")
        game_sts = game_on()
        clear_output()
        game_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        display_board(game_board)
        if not game_sts:
            break
    elif win_check(game_board) == "O":
        game_sts = False
        print("O wins!!!!!!!!!!!!!!!!!!!!")
        game_sts = game_on()
        clear_output()
        game_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        display_board(game_board)
        if not game_sts:
            break 
    #turn for X
    print("for X")
    position = choice()
    game_board =  alter_board('X',position,game_board)
    clear_output()
    display_board(game_board)
    if ' ' not in game_board:
        game_sts = False
        print("Its a TIE")
        game_sts = game_on()
        if not game_sts:
            break
        game_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        clear_output()
        display_board(game_board)
        
    else:
        pass
    #win check
    if win_check(game_board) == "X":
        game_sts = False
        print("X wins !!!!!!!!!!!!!!!!!!!")
        game_sts = game_on()
        clear_output()
        game_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        display_board(game_board)
        if not game_sts:
            break
    elif win_check(game_board) == "O":
        game_sts = False
        print("O wins !!!!!!!!!!!!!!!!!!!!")
        game_sts = game_on()
        clear_output()
        game_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        display_board(game_board)
        if not game_sts:
            break 
    # turn for O
    print("for O")
    position = choice()
    game_board =  alter_board('O',position,game_board)
    clear_output()
    display_board(game_board)
    if ' ' not in game_board:
        game_sts = False
        print("Its a TIE")
        game_sts = game_on()
        if not game_sts:
            break
        game_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        clear_output()
        display_board(game_board)
        
    else:
        pass
clear_output()
print("Thanks for playing")
    

            