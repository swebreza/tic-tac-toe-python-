board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]


################################################################
def displayboard():
    print(board[0] + " |", board[1] + " |", board[2] + "         1|2|3")
    print(board[3] + " |", board[4] + " |", board[5] + "         4|5|6")
    print(board[6] + " |", board[7] + " |", board[8] + "         7|8|9")


##############################################################
def handel_turn(turns11):
    try:
        position = int(input("Enter positions from 1-9: ")) - 1
    except:
        print("Please input a number")
        exit()
    if board[position] != "-":
        print("Enter at valid space")
    else:
        board[position] = turns11
        displayboard()


############################################################
def play():
    turns = "X"
    count = int(1)
    displayboard()  # Displaying game board
    while count < 10:
        handel_turn(turns)
        if count % 2 == 0:
            turns = "X"
        else:
            turns = "O"
        #flip(turns)
        check(turns)
        count = count + 1


###########################################################
def check(turns1):
    # check for "X" and "O"
    row1 = board[0] == board[1] == board[2] != "-"  # Row Check
    row2 = board[3] == board[4] == board[5] != "-"  # Row Check
    row3 = board[6] == board[7] == board[8] != "-"  # Row Check
    col1 = board[0] == board[3] == board[6] != "-"  # Column check
    col2 = board[1] == board[4] == board[7] != "-"  # Column check
    col3 = board[2] == board[5] == board[8] != "-"  # Column check
    dig1 = board[0] == board[4] == board[8] != "-"  # Diagonal check
    dig2 = board[2] == board[4] == board[6] != "-"  # Diagonal check
    if row1 or row2 or row3 or dig1 or dig2 is True:
        print(turns1, " Looses")
        exit()
    elif col1 or col2 or col3 is True:
        print(turns1, " looses")
        exit()
    return turns1
play()


#By MD Suweb Reza
