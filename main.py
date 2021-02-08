def print_board(a1, b1, c1, a2, b2, c2, a3, b3, c3):
    print("   A     B     C")
    print("      |     |")
    print("1 ", a1, " | ", b1, " | ", c1)
    print("      |     |     ")
    print(" -----------------")
    print("      |     |")
    print("2 ", a2, " | ", b2, " | ", c2)
    print("      |     |")
    print(" -----------------")
    print("      |     |")
    print("3 ", a3, " | ", b3, " | ", c3)
    print("      |     |")
    return ''


def check_if_three(x):
    if x[0][0] == x[0][1] and x[0][1] == x[0][2] and x[0][0] != ' ':
        return True
    elif x[1][0] == x[1][1] and x[1][1] == x[1][2] and x[2][0] != ' ':
        return True
    elif x[2][0] == x[2][1] and x[2][1] == x[2][2] and x[2][0] != ' ':
        return True
    elif x[0][0] == x[1][0] and x[1][0] == x[2][0] and x[0][0] != ' ':
        return True
    elif x[0][1] == x[1][1] and x[1][1] == x[2][1] and x[0][1] != ' ':
        return True
    elif x[0][2] == x[1][2] and x[1][2] == x[2][2] and x[0][2] != ' ':
        return True
    elif x[0][0] == x[1][1] and x[1][1] == x[2][2] and x[0][0] != ' ':
        return True
    elif x[2][0] == x[1][1] and x[1][1] == x[0][2] and x[2][0] != ' ':
        return True
    return False


def letters_to_numbers(letter):
    if letter == 'a' or letter == 'A':
        return 0
    if letter == 'b' or letter == 'B':
        return 1
    if letter == 'c' or letter == 'C':
        return 2


play = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
print(print_board(play[0][0], play[0][1], play[0][2], play[1][0], play[1][1], play[1][2], play[2][0], play[2][1],
                  play[2][2]))

while not check_if_three(play):

    player1row = ""
    player1column = ""
    player2row = ""
    player2column = ""

    # player 1
    # ----------
    player1move = input('Player 1, where do you want to play? ')

    # finds invalid input
    while len(player1move) != 2:
        player1move = input('Please input a valid move: ')
    while not (((player1move[0] == 'a' or player1move[0] == 'b' or player1move[0] == 'c') and
                (player1move[1] == '1' or player1move[1] == '2' or player1move[1] == '3')) or (
                       (player1move[1] == 'a' or player1move[1] == 'b' or player1move[1] == 'c') and
                       (player1move[0] == '1' or player1move[0] == '2' or player1move[0] == '3'))):
        player1move = input('Please input a valid move: ')

    # converts user input to numbers for 2D array
    if player1move[0] == 'a' or player1move[0] == 'b' or player1move[0] == 'c':
        player1column = letters_to_numbers(player1move[0])
        player1row = int(player1move[1])-1
    else:
        player1column = letters_to_numbers(player1move[1])
        player1row = int(player1move[0])-1

    # makes sure that space isn't already taken
    while play[player1row][player1column] == 'O':
        print('SPOT TAKEN! PLEASE TRY AGAIN')
        player1row = int(input("Player 1: What row do you want to play? "))
        player1column = input("Player 1: What column do you want to play? ")

    play[player1row][player1column] = 'X'
    print(print_board(play[0][0], play[0][1], play[0][2], play[1][0], play[1][1], play[1][2], play[2][0], play[2][1],
                      play[2][2]))
    lastPlayer = 'Player 1'

    if check_if_three(play):
        break

    # player 2
    # ----------
    player2move = input('Player 2, where do you want to play? ')

    # finds invalid input
    while len(player2move) != 2:
        player2move = input('Please input a valid move: ')
    while not (((player2move[0] == 'a' or player2move[0] == 'b' or player2move[0] == 'c') and
                (player2move[1] == '1' or player2move[1] == '2' or player2move[1] == '3')) or (
                       (player2move[1] == 'a' or player2move[1] == 'b' or player2move[1] == 'c') and
                       (player2move[0] == '1' or player2move[0] == '2' or player2move[0] == '3'))):
        player2move = input('Please input a valid move: ')

    # converts user input to numbers for 2D array
    if player2move[0] == 'a' or player2move[0] == 'b' or player2move[0] == 'c':
        player2column = letters_to_numbers(player2move[0])
        player2row = int(player2move[1]) - 1
    else:
        player2column = letters_to_numbers(player2move[1])
        player2row = int(player2move[0]) - 1

    # makes sure that space isn't already taken
    while play[player2row][player2column] == 'X':
        print('SPOT TAKEN! PLEASE TRY AGAIN')
        player2row = int(input("Player 2: What row do you want to play? "))
        player2column = input("Player 2: What column do you want to play? ")

    play[player2row][player2column] = 'O'
    print(print_board(play[0][0], play[0][1], play[0][2], play[1][0], play[1][1], play[1][2], play[2][0], play[2][1],
                      play[2][2]))
    lastPlayer = 'Player 2'

print('Yay! ', lastPlayer, ' won!!')
