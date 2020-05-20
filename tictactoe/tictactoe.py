boardstr = '     |     |     \n_____|_____|_____\n     |     |     \n     |     |     \n_____|_____|_____\n     |     |     \n     |     |     '
board = [x for x in boardstr]
#print(board)
chance = ['X','O','X','O','X','O','X','O','X','O','X']
indexes = [1,2,3,4,5,6,7,8,9]
place_holders = {'1': 2, '2': 8, '3': 14, '4': 56, '5': 62, '6': 68, '7': 110, '8': 116, '9': 122}
used = []
status_list = []
status = False
player = False
marker = 0
game_num = 0
play_again = 0

def placeXO(call, pos):
    board[place_holders[call]]  = chances[pos]
    print('\n'*100)
    print(''.join(board))

def status_check():
    if status == True:
        status_list.append(status)

def check_win():
    if board[2] == 'X' or board[2] == 'O':
        status = board[2] == board[8] == board[14]
        if status == True:
            status_list.append(status)
    if board[56] == 'X' or board[56] == 'O':
        status = board[56] == board[62] == board[68]
        if status == True:
            status_list.append(status)
    if board[110] == 'X' or board[110] == 'O':
        status = board[110] == board[116] == board[122]
        if status == True:
            status_list.append(status)
    if board[2] == 'X' or board[2] == 'O':
        status = board[2] == board[56] == board[110]
        if status == True:
            status_list.append(status)
    if board[8] == 'X' or board[8] == 'O':
        status = board[8] == board[62] == board[116]
        if status == True:
            status_list.append(status)
    if board[14] == 'X' or board[14] == 'O':
        status = board[14] == board[68] == board[122]
        if status == True:
            status_list.append(status)
    if board[2] == 'X' or board[2] == 'O':
        status = board[2] == board[62] == board[122]
        if status == True:
            status_list.append(status)
    if board[14] == 'X' or board[14] == 'O':
        status = board[14] == board[62] == board[110]
        if status == True:
            status_list.append(status)

def reset_game():
    used = []
    status_list = []
    status = False
    player = False
    marker = 0
    board[2], board[8], board[14], board[56], board[62], board[68], board[110], board[116], board[122] = ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '    

while True:
    print('TIK TAK TOE'+'\n')
    print("Let's start the game")
    print("To start the game first choose your sign...\n")

    while marker != 'X' and marker != 'O':
        marker = input("CHOOSE X/O: ").upper()
        if marker != 'X' or marker != 'O':
            print("Wrong input\n")
    if marker == 'X':
        chances = chance[0:-2]
    elif marker == 'O':
        chances = chance[1:-1]

    print(f"\nPlayer 1 assigned '{marker}'...\n\n")

    for i in range(len(chances)):
        player = not player
        index = input("\n\nWhere do you want to place your marker? ")
        #print(type(index))
        if index in used:
            while index in used:
                print('\n\nPosition not available!')
                index = input("Choose another position: ")
        used.append(index)
        #str(index)
        placeXO(index, i)
        check_win()
        if True in status_list:
            if player == True:
                print('\n\nPlAYER 1 HAS WON!')
            else:
                print('\n\nPLAYER 2 HAS WON!')
            break
    else:
        print('\n\nTHE GAME IS A DRAW!')
    game_num += 1
    play_again = input("Do you want to play again?(Y/N) ").upper()
    if play_again == 'Y':
        reset_game()
        print("WELCOME BACK!")
        continue
    elif play_again == 'N':
        break