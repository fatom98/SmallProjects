import random, os, time

indexes = [str(i+1) for i in range(0,9)]

moves = {"1":"00","2":"01","3":"02","4":"10","5":"11","6":"12","7":"20","8":"21","9":"22"}


def login():

    print("Welcome to Tic Tac Toe")

    global gameBoard, playerName1, playerName2

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

    prepareForGame()


def prepareForGame():
    print("Now I will decide who goes first and plays as what.\n")

    firstPlayer, secondPlayer = random.sample([playerName1, playerName2], 2)

    firstPlayerShape, secondPlayerShape = random.sample(["X", "O"], 2)

    print(f"{firstPlayer} goes first and plays as {firstPlayerShape}\n\n{secondPlayer} is second and plays as {secondPlayerShape}\n")

    time.sleep(3)

    players = {firstPlayer: firstPlayerShape, secondPlayer: secondPlayerShape}

    gameLogic(firstPlayer, secondPlayer, players)


def gameLogic(firstPlayer, secondPlayer, players):

    state = True

    turn = 0

    while state:

        clear()

        for row in gameBoard:
            print(f"{row}\n\n")


        if turn % 2 == 0:
            name = firstPlayer
            print(f"It is your turn {name}\n")

            while True:
                index = input("Please choose an index: ")
                print("")

                if index not in indexes: print("Please enter a valid index with spaces between it.\n")

                else:
                    row, column = list(moves[index])
                    row, column = int(row), int(column)

                    if gameBoard[row][column] == ".":
                        gameBoard[row][column] = players[firstPlayer]
                        break

                    else:
                        print(f"({index}) is filled with {gameBoard[row][column]}. Please choose another index\n", end = "\r")

        else:
            name = secondPlayer
            print(f"It is your turn {name}\n")

            while True:
                index = input("Please choose an index: ")
                print("")

                if index not in indexes:
                    print("Please enter a valid index\n")

                else:
                    row, column = list(moves[index])
                    row, column = int(row), int(column)

                    if gameBoard[row][column] == ".":
                        gameBoard[row][column] = players[secondPlayer]
                        break
                    else:
                        print(f"({index}) is filled with {gameBoard[row][column]}. Please choose another index\n", end = "\r")

        if gameBoard[0][0] == gameBoard[0][1] == gameBoard[0][2] != "." or \
            gameBoard[1][0] == gameBoard[1][1] == gameBoard[1][2] != "." or \
            gameBoard[2][0] == gameBoard[2][1] == gameBoard[2][2] != "." or \
            gameBoard[0][0] == gameBoard[1][0] == gameBoard[2][0] != "." or \
            gameBoard[0][1] == gameBoard[1][1] == gameBoard[2][1] != "." or \
            gameBoard[0][2] == gameBoard[1][2] == gameBoard[2][2] != "." or \
            gameBoard[0][0] == gameBoard[1][1] == gameBoard[2][2] != "." or \
            gameBoard[0][2] == gameBoard[1][1] == gameBoard[2][0] != ".":

            clear()

            for row in gameBoard:
                print(f"{row}\n\n")

            print(f"Congratulations {name} you won.\n")


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
            clear()
            login()

        elif again == "n":
            print("Thank for playing. I hope i can see you soon :)")
            exit()

        else: print("your answer only can be y or no. Please enter a valid answer.\n")


def clear():
    os.system("cls" if os.name == "nt" else "clear")


if __name__ == '__main__':
    login()
