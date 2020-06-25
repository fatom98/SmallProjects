from os import name, system
import random
import time

indexes = [str(i+1) for i in range(0,9)]

moves = {"1":"00","2":"01","3":"02","4":"10","5":"11","6":"12","7":"20","8":"21","9":"22"}


def login():
    print("Welcome to Tic Tac Toe. This game is piece of cake. \n"
          "Two person will play this game by entering index of row and cloumn they wanted to change.\n"
          "Good luck i hope you learn better by practicing :).\n")
    global gameBoard

    gameBoard = [[".", ".", "."],
                [".", ".", "."],
                [".", ".", "."]]

    state = True

    while state:
        playerName1 = input("Please enter first players: ").capitalize()
        print("")

        if playerName1 == "": print("your name can't be  blank\n")
        elif len(playerName1) < 3: print("Your name needs to be longer than 2 characters.\n")
        else:
            print(f"Welcome {playerName1} good luck.\n")
            state = False

    state = True

    while state:
        playerName2 = input("Please enter second player's name: ").capitalize()
        print("")

        if playerName1 == "": print("your name can't be  blank\n")
        elif len(playerName1) < 3: print("Your name needs to be longer than 2 characters.\n")
        elif playerName2 == playerName1: print(f"{playerName1} is taken. Please choose another name\n")
        else:
            print(f"Welcome {playerName2} good luck.\n")
            state = False

    prepareForGame(playerName1, playerName2)


def prepareForGame(playerName1, playerName2):
    print("Now I will decide who goes first and playes as what.\n")

    players = random.sample([playerName1, playerName2], 2)
    firstPlayer, secondPlayer = players[0], players[1]

    shapes = random.sample(["X", "O"], 2)
    firstPlayerShape, secondPlayerShape = shapes[0], shapes[1]

    print(f"{firstPlayer} goes first and playes as {firstPlayerShape}\n\n{secondPlayer} is second and playes as {secondPlayerShape}\n")

    players = {firstPlayer: firstPlayerShape, secondPlayer: secondPlayerShape}

    gameLogic(firstPlayer, secondPlayer, players)


def gameLogic(firstPlayer, secondPlayer, players):

    state = True

    turn = 0

    while state:

        for row in gameBoard:
            print(f"{row}\n")

        if turn % 2 == 0:
            name = firstPlayer
            print(f"It is your turn {name}\n")

            while True:
                index = input("Please choose an index ex(1,2,3 etc.): ")
                print("")
                if index not in indexes: print("Please enter a valid index with spaces between it.\n")
                else:
                    row, column = list(moves[index])
                    row, column = int(row), int(column)
                    if gameBoard[row][column] == ".":
                        gameBoard[row][column] = players[firstPlayer]
                        break
                    else:
                        print(f"({index}) is filled with {gameBoard[row][column]}. Please choose another index\n")

        else:
            name = secondPlayer
            print(f"It is your turn {name}\n")

            while True:
                index = input("Please choose an index ex(1,2,3 etc.): ")
                print("")
                if index not in indexes:
                    print("Please enter a valid index with spaces between it.\n")
                else:
                    row, column = list(moves[index])
                    row, column = int(row), int(column)

                    if gameBoard[row][column] == ".":
                        gameBoard[row][column] = players[secondPlayer]
                        break
                    else:
                        print(f"({index}) is filled with {gameBoard[row][column]}. Please choose another index\n")

        if gameBoard[0][0] == gameBoard[0][1] == gameBoard[0][2] != "." or \
            gameBoard[1][0] == gameBoard[1][1] == gameBoard[1][2] != "." or \
            gameBoard[2][0] == gameBoard[2][1] == gameBoard[2][2] != "." or \
            gameBoard[0][0] == gameBoard[1][0] == gameBoard[2][0] != "." or \
            gameBoard[0][1] == gameBoard[1][1] == gameBoard[2][1] != "." or \
            gameBoard[0][2] == gameBoard[1][2] == gameBoard[2][2] != "." or \
            gameBoard[0][0] == gameBoard[1][1] == gameBoard[2][2] != "." or \
            gameBoard[0][2] == gameBoard[1][1] == gameBoard[2][0] != ".":

            print(f"Congrulations {name} you won.\n")

            for row in gameBoard:
                print(f"{row}\n")

            print("Game is over\n")
            state = False

        elif "." not in gameBoard[0] and "." not in gameBoard[1] and "." not in gameBoard[2]:
            print("I'm sorry. The bord is full. Its a drawn :(\n")
            state = False

        turn += 1

    while True:
        again = input("Do yo want to play again (y or n)?: ")
        print("")
        if again == "y":
            print("Creating the board. Please be patient\n")
            time.sleep(2)
            clear()

            login()
        elif again == "n":
            print("Thank for playing. I hope i can see you soon :)")
            exit()
        else: print("your answer only can be y or no. Please enter a valid answer.\n")

def clear():
    if name == 'nt':
        _ = system('cls')

if __name__ == '__main__':
    login()