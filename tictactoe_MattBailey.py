# Matthew Bailey, Tic Tac Toe Assignment


def main():
    player = next_player("")
    board = create_board()
    while not (has_winner(board) or is_a_draw(board)):
        # display/create the board
        display_board(board)
        # allow the user to 'move'
        make_move(player, board)
        #toggle which player makes which move on the board
        player = next_player(player)
    #re-display the board after each move has been made
    display_board(board)
    print("Good game. Thanks for playing!") 

def create_board():
    #create the board by using an array/dictonary, starting with an empy dictonrary 
    board = []
    for square in range(9):
        #iterate through the dictronary, square is a 'tempoarary' variable
        board.append(square + 1)
        #this is where we label each of the 9 squares. Remember, starts with 0 
    return board

def display_board(board):
    #create the board the user will be able to see (this is provided!)
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print('- + - + -')
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print('- + - + -')
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()
    
def is_a_draw(board):
    #This is saying if the isn't a winner, the board will declare it a tie
    for square in range(9):
        if board[square] != "X" and board[square] != "O":
            return False
    print("It's a tie!")
    return True 
    
def has_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def make_move(player, board):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[square - 1] = player
    if square != 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
        print("Please try again. Only the numbers 1-9 are accepted.")

def next_player(current):
    if current == "" or current == "O":
        return "X"
    elif current == "X":
        return "O"

if __name__ == "__main__":
    main()