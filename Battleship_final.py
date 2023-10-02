#the random module is imported to allow randomization
import random

#define lists of coordinates
list_nu = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list_le = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

#method to define board
p_board = []
c_board = []
h_c_board = []
string = "abcdefghij"
direction_list = ["r", "d"]

#define random starting position computer ship
def start_position_ship(list_nu, list_le):
    start_n = random.choice(list_nu)
    start_l = random.choice(list_le)
    start_position = (start_n, start_l)
    return start_position
	
#method to initialise board as a list
def Init_Board(board):
    for n in range(10):
        board.append([])
    for n in range(10):
        for k in range(10):
            board[n].append("-")

#method to pring the board
def Print_Player_Board(board):
    print("\n*********************")
    print("*** Player Board ****")
    print("********************* \n")
    print("  a b c d e f g h i j")
    for n in range(10):
        print(str(n), end = " ")
        for k in range(10):
            print(str(board[n][k]) + " ", end = "")
        print()
    print(" \n")

#print computer board  
def Print_Computer_Board(board):
    print("\n*********************")
    print("** Computer Board **")
    print("********************* \n")
    print("  a b c d e f g h i j")
    for i in range (10):
        print(str(i) + " ", end = "")
        for k in range(10):
            print(str(board[i][k]) + " ", end = "")
        print()
    print(" \n")

Init_Board(p_board)
Init_Board(c_board)
Init_Board(h_c_board)

#function to determine position of a certain element on the board
def Find_index(board, element):
    for l in range(10):
        for k in range(10):
            y = board[l][k]        
            if y == element:
                return l, k

Print_Player_Board(p_board)

#method to request input about the ships to be placed, the starting coordinates and the direction
def Input():
    shi = input("Please indicate the ship to place typing the letter c, b, s, or d. \nRemember: \nc = carrier, occupying 5 spaces on the board; \nb =  battleship, occupying 4 spaces on the board; \ns = submarine, occupying 3 spaces on the board; \nd = destroyer, occupying 2 spaces on the board: \n")
    ship = str(shi)
    nu = input("Please indicate the first coordinate (number between 0 and 9): \n")
    n = int(nu)
    le = input("Please indicate the second coordinate (a letter between a and j): \n")
    l = str(le)
    for letter in string:
        if letter == l:
            ind = string.find(letter)
            index = int(ind)
    direct = input("Please indicate the direction of your ship, i.e. r (from left to right starting from starting coordinate or d (from top to bottom starting from starting coordinate: \n")
    direction = str(direct)
    return ship, n, l, direction, index
  
#method to create the player_ship
def Ship_player(ship):
    ship_player = []
    if ship == "c":
        for k in range(5):
            if direction == "r":
                if (index + 4) < 10:
                    ship_p = (n, (index + k))
                    ship_player.append(ship_p)
                else:
                    ship_p = (n, (5 + k))
                    ship_player.append(ship_p)
            elif direction == "d":
                if (n + 4) < 10:
                    ship_p = ((n + k), index)
                    ship_player.append(ship_p)
                else:
                    ship_p = ((k + 5), index)
                    ship_player.append(ship_p)
    elif ship == "b":
        for k in range(4):
            if direction == "r":
                if (index + 3) < 10:
                    ship_p = (n, (index + k))
                    ship_player.append(ship_p)
                else:
                    ship_p = (n, (6 + k ))
                    ship_player.append(ship_p)
            elif direction == "d":
                if (n + 3) < 10:
                    ship_p = ((n + k), index)
                    ship_player.append(ship_p)
                else:
                    ship_p = ((k + 6), index)
                    ship_player.append(ship_p)
    elif ship == "s":
        for k in range(3):
            if direction == "r":
                if (index + 2) < 10:
                    ship_p = (n, (index + k))
                    ship_player.append(ship_p)
                else:
                    ship_p = (n, (7 + k))
                    ship_player.append(ship_p)
            elif direction == "d":
                if (n + 2) < 10:
                    ship_p = ((n + k), index)
                    ship_player.append(ship_p)
                else:
                    ship_p = ((k + 7), index)
                    ship_player.append(ship_p)
    elif ship == "d":
        for k in range(2):
            if direction == "r":
                if (index + 1) < 10:
                    ship_p = (n, (index + k))
                    ship_player.append(ship_p)
                else:
                    ship_p = (n, (k + 8))
                    ship_player.append(ship_p)
            elif direction == "d":
                if (n + 1) < 10:
                    ship_p = ((n + k), index)
                    ship_player.append(ship_p)
                else:
                    ship_p = ((k + 8), index)
                    ship_player.append(ship_p)
    return ship_player

#method to place ship on the board
def Place_ship(ship_player, board, ship):
    for item in ship_player:
        for n in range(10):
            if n == item[0]:
                for k in range(10):
                    if k == item[1]:
                        if ship == "c":
                            board[item[0]][item[1]] = "C"
                        elif ship == "b":
                            board[item[0]][item[1]] = "B"
                        elif ship == "s":
                            board[item[0]][item[1]] = "S"
                        elif ship == "d":
                            board[item[0]][item[1]] = "D"
    return board

#start of game for the player
print("Welcome to Battleship game, player.\nLet's start with placing your ships on the board. \nYou will need to place: \none carrier, \none battleship, \ntwo submarines, and \nthree destroyers.")
for i in range(1, 8):
    ship, n, l, direction, index = Input() 
    ship_player = Ship_player(ship)
    new_player_board = Place_ship(ship_player, p_board, ship)
    Print_Player_Board(p_board)
    print("You have placed your ship no. {number}.\nRemember: you need to place: \none carrier, \none battleship, \ntwo submarines, and \nthree destroyers. \nStill {number2} to place.".format(number = i, number2 = (7 - i)))
print("Your ships have all been placed.")

#function to position computer ships
def Computer_ship_position(board, ship, ship_length):
    st = start_position_ship(list_nu, list_nu)
    ship_direction = random.choice(direction_list)  
    if ship_direction == "d":
        if (st[0] + ship_length - 1) <= 9:
            c = st[1]
            for l in range(st[0], (st[0] + ship_length)):
                y = board[l][c]
                if y == "C" or y == "B" or y == "S" or y == "D":
                    indx = Find_index(board, y)
                    for l in range(st[0], indx[0]):
                        board[l][c] = "-"
                    Computer_ship_position(h_c_board, ship, ship_length)
                    break
                else:
                    board[l][c] = ship  
        else:
            c = st[1]
            for l in range((10 - ship_length), 10):
                y = board[l][c]
                if y == "C" or y == "B" or y == "S" or y == "D":
                    indx = Find_index(board, y)
                    for l in range((10-ship_length), indx[0]):
                        board[l][c] = "-"
                    Computer_ship_position(h_c_board, ship, ship_length)
                    break
                else:
                    board[l][c] = ship
    elif ship_direction == "r":
        if (st[1] + ship_length - 1) <= 9:
            r = st[0]
            for l in range(st[1], (st[1] + ship_length)):
                y = board[r][l]
                if y == "C" or y == "B" or y == "S" or y == "D":
                    indx = Find_index(h_c_board, y)
                    for l in range(st[1], indx[1]):
                        board[r][l] = "-"
                    Computer_ship_position(h_c_board, ship, ship_length)
                    break
                else:
                    board[r][l] = ship
        else:
            r = st[0]
            for l in range((10 - ship_length), 10):
                y = board[r][l]
                if y == "C" or y == "B" or y == "S" or y == "D":
                    indx = Find_index(h_c_board, y)
                    for l in range((10 - ship_length), indx[1]):
                        board[st[0]][l] = "-"
                    Computer_ship_position(h_c_board, ship, ship_length)
                    break
                else:
                    board[r][l] = ship
    return board

#initialisation of computer ships
c_carrier = Computer_ship_position(h_c_board, ship = "C", ship_length = 5)
c_battleship = Computer_ship_position(h_c_board, ship = "B", ship_length = 4)
c_submarine1 = Computer_ship_position(h_c_board, ship = "S", ship_length = 3)
c_submarine2 = Computer_ship_position(h_c_board, ship = "S", ship_length = 3)
c_destroyer1 = Computer_ship_position(h_c_board, ship = "D", ship_length = 2)
c_destroyer2 = Computer_ship_position(h_c_board, ship = "D", ship_length = 2)
c_destroyer3 = Computer_ship_position(h_c_board, ship = "D", ship_length = 2)

#Print_Computer_Board(h_c_board)

print("All enemy ships have been deployed!\n")

#Player choses the places in the board to hit and hit or miss is verified
def Player_input(h_c_board, c_board):
    r = int(input("Please inicate the position you would like to hit.\nPlease input a number between 0 and 9:\n"))
    col = input("\nPlease input a letter between a and j:\n")
    c = string.index(col)
    y = h_c_board[r][c]
    if y == "-":
        print("No hit! Do not dispair and try again!\n")
        c_board[r][c] = " "
        return c_board
    else:
        c_board[r][c] = "X"
        h_c_board[r][c] = "X"
        print("Hit!\n")
        return c_board, h_c_board

#function checkes if a ship was sank
def Check_ship_sank(board, ship):
    count = 0
    for r in range(10):
        for c in range(10):
            y = board[r][c]
            if y == ship:
                count += 1
    if ship == "C" and count == 0:
        print("You have sank the carrier!\n")
    elif ship == "B" and count == 0:
        print("You have sank the battleship!\n")
    elif ship == "S" and count == 3:
        print("You have sank one submarine!\n")
    elif ship == "S" and count == 0:
        print("You have sank both submarines!\n")
    elif ship == "D" and count == 4:
        print("You have sank one destroyer!\n")
    elif ship == "D" and count == 2:
        print("You have sank two destroyers!\n")
    elif ship == "D" and count == 0:
        print("You have sank all destroyers!\n")
    
#function checks if all ships were sank
def Check_if_won(board): 
    count = 0
    for r in range(10):
        for c in range(10):
            y = board[r][c]
            if y == "C" or y == "D" or y == "B" or y == "S":
                count += 1
    if count == 0 and board == h_c_board:
        print("You have sank all the enemy ships!! You have won!!")
        return False
    elif count == 0 and board == p_board:
        print("Your enemy sank all your ships!! You have lost...")
        return False

#function checks computer input and verifies if ship is hit mis
def Computer_input(p_board):
    r = random.choice(list_nu)
    c = random.choice(list_nu)
    y = p_board[r][c]
    if y == "-":
        print("Your enemy did not hit!\n")
        p_board[r][c] = " "
        return p_board
    elif y == "C" or y == "B" or y == "D" or y == "S":
        p_board[r][c] = "X"
        print("Your ship was hit!\n")
        return p_board

#the moves of the player and of the computer are executed
for i in range(100):
    Player_input(h_c_board, c_board)
    #Print_Computer_Board(h_c_board)
    Print_Computer_Board(c_board)
    Check_ship_sank(h_c_board, ship = "C")
    Check_ship_sank(h_c_board, ship = "B")
    Check_ship_sank(h_c_board, ship = "D")
    Check_ship_sank(h_c_board, ship = "S")
    z = Check_if_won(h_c_board)
    if z == False:
        break
    Computer_input(p_board)
    Print_Player_Board(p_board)
   # Check_ship_sank(p_board, ship = "C")
   # Check_ship_sank(p_board, ship = "B")
   # Check_ship_sank(p_board, ship = "D")
   # Check_ship_sank(p_board, ship = "S")
    w = Check_if_won(p_board)
    if w == False:
        break
