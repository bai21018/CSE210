# Matthew Bailey, Tic Tac Toe Assignment
import time 

play_loop = True

def main():
    while play_loop == True:
        print("Hello and welcome to a simple version of Tic Tac Toe! Would you like to play?")
        play_again = input("Type 'y' for yes and 'n' for no: ")
        if play_again.lower() == 'y':
            print("Generating player board...")
            time.sleep(5)
            player = next_player("")
            block = create_block()
            while not (has_winner(block) or is_a_draw(block)):
                # display/create the block
                display_block(block)
                # allow the user to 'move'
                make_move(player, block)
                #toggle which player makes which move on the block
                player = next_player(player)
            #re-display the block after each move has been made
            display_block(block)
            print("Game Over. Try again?") 
        else:
            print("Thank you for playing!")
        play_again = input("Type 'y' for yes and 'n' for no: ")
    

def create_block():
    #create the block by using an array/dictonary, starting with an empy dictonrary 
    block = []
    for square in range(9):
        #iterate through the dictronary, square is a 'tempoarary' variable
        block.append(square + 1)
        #this is where we label each of the 9 squares. Remember, starts with 0 
    return block

def display_block(block):
    #create the block the user will be able to see (this is provided!)
    print()
    print(f"{block[0]} | {block[1]} | {block[2]}")
    print('- + - + -')
    print(f"{block[3]} | {block[4]} | {block[5]}")
    print('- + - + -')
    print(f"{block[6]} | {block[7]} | {block[8]}")
    print()
    
def is_a_draw(block):
    #This is saying if the isn't a winner, the block will declare it a tie
    for square in range(9):
        if block[square] != "X" and block[square] != "O":
            return False
    print("It's a tie!")
    return True 
    
def has_winner(block):
    return (block[0] == block[1] == block[2] or
            block[3] == block[4] == block[5] or
            block[6] == block[7] == block[8] or
            block[0] == block[3] == block[6] or
            block[1] == block[4] == block[7] or
            block[2] == block[5] == block[8] or
            block[0] == block[4] == block[8] or
            block[2] == block[4] == block[6])

def make_move(player, block):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    block[square - 1] = player
    if square != 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
        print("Please try again. Only the numbers 1-9 are accepted.")

def next_player(current):
    if current == "" or current == "O":
        return "X"
    elif current == "X":
        return "O"

if __name__ == "__main__":
    main()