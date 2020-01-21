#------Global variables-----
game_still_going = True

#who won /tie
winner = None

#whose turn it is
current_player = "X"


board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-",]
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2] + " | ")
    print(board[3] + " | " + board[4] + " | " + board[5] + " | ")
    print(board[6] + " | " + board[7] + " | " + board[8] + " | ")

def play_game():


#display initial board
    display_board()
    # while game is going on
    while game_still_going:

    #handle single turn of an arbitary player
        handle_turn(current_player)

    #check if the game has ended
        check_if_game_over()

    #Flip to the other player
        flip_player()

    #game has ended
    if winner == "X" or winner == "O":
        print(winner + " Won.")
    elif winner == None:
        print("Tie.")


def handle_turn(player):
    print(player + "'s turn.")
    position = input("choose a position from 1 - 9: ")

    valid = False
    while not valid:    

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("choose a position from 1 to 9: ")
        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't go there, Go again.")

    board[position] = player
    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():
#set global variable
    global winner
    #check rows
    row_winner = check_row()
    #check column
    column_winner = check_column()
    #check diagonals
    diagonal_winner = check_diagonal()


    if row_winner:
        winner = row_winner      
    elif column_winner:
        winner = column_winner        
    elif diagonal_winner:
        winner = diagonal_winner  
    else:
        winner = None
    return

def check_row():
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_still_going = False
    #return winner (x or o)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_column():
    global game_still_going
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3:
        game_still_going = False
    #return winner (x or o)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonal():
    global game_still_going
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"

    if diagonal_1 or diagonal_2:
        game_still_going = False
    #return winner (x or o)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]

    return

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return

def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"

    return

play_game()

# board
# display board
# play game
#handle turn
# check win
   #check rows, column and diagonis\
# check tie
# flip player
