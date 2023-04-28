"""
This is a very simple represation of the game tic tac toe using Python.
"""
import random
import time

# Global variables.
board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
game_running = True
current_player = "X"
winner = None


def printBoard(board):
    """
    This function acts as a board for the game tic tac toe
    and takes in board as a parameter and prints it out as a user-friendly output.
    """
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("-"*10)
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-"*10)
    print(board[6] + " | " + board[7] + " | " + board[8])


def playerInput(board):
    """
    This function takes user input and assign that input value to 
    the board(list) in the right position.
    """
    user_input = int(input("Select a spot 1-9: "))
    if board[user_input-1] == "-":
        board[user_input-1] = current_player
    else:
        print("That spot is already occupied, try another one.")


def checkHorizontle(board):
    """
    This function checks if there is three matching Xs or Os on the board horizontally.
    """
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkVertical(board):
    """
    This function checks if there is three matching Xs or Os on the board vertically.
    """
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[3]
        return True


def checkDiagonal(board):
    """
    This function checks if there is three matching Xs or Os on the board diagonally.
    """
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[2]
        return True


def checkIfWin(board):
    """
    This fucntion checks for the winner in this game.
    """
    global game_running
    if checkHorizontle(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        game_running = False

    elif checkVertical(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        game_running = False

    elif checkDiagonal(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        game_running = False


def checkIfTie(board):
    """
    If all of the spots on the board are filled up but there is no winner, 
    this function will print out 'It is a tie! 'informing the user 
    that there's no winner in this game.
    """
    global game_running
    if "-" not in board:
        printBoard(board)
        print("It is a tie!")
        game_running = False


def switchPlayer():
    """ This function will assisst in switching players."""
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


def computer(board):
    """ This funciton acts as a bot playing againstt the user. 
    Note! This isn't a smart bot!"""
    while current_player == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()

# A loop for playing the game untill there is a winner.
while game_running:
    printBoard(board)
    playerInput(board)
    checkIfWin(board)
    checkIfTie(board)
    switchPlayer()
    time.sleep(0.8)
    computer(board)
    checkIfWin(board)
    checkIfTie(board)