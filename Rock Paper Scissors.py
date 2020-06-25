import random

shapes = {"s": "✂", "p": "📄", "r": "🤘"}

def gameLogic():
    print("Welcome to classic awesome Rock Paper Scissor.\nChoose a shape by entering its initial.\nEx r for Rock, s for Scissors and p for paper.\nGood luck :)\n")
    playerName = input("Please enter your name: ").capitalize()
    print("")
    scores = {playerName: 0, "Computer": 0}
    state = True

    while state:
        items = dict()
        playerShape = input("Choose a shape on the count of three 1, 2, 3: ")
        print("")

        if playerShape not in shapes:
            print("Please choose Rock (r), Paper (p) or Scissors (s).\n")
            continue

        computerShape = random.choice(list(shapes.keys()))
        items[playerShape], items[computerShape] = playerName, "Computer"
        print(f"{playerName}: {shapes[playerShape]}{' ' * 10}Computer: {shapes[computerShape]}\n")

        if playerShape == computerShape: print(f"Its a Withdraw\n\n{playerName}: {scores[playerName]}{' ' * 11}Computer: {scores['Computer']}\n")
        elif "r" not in items:
            scores[items['s']] += 1
            print(f"{items['s']} gets point !!!\n\n{playerName}: {scores[playerName]}{' ' * 11}Computer: {scores['Computer']}\n")
        elif "p" not in items:
            scores[items['r']] += 1
            print(f"{items['r']} gets point !!!\n\n{playerName}: {scores[playerName]}{' ' * 11}Computer: {scores['Computer']}\n")
        elif "s" not in items:
            scores[items['p']] += 1
            print(f"{items['p']} gets point !!!\n\n{playerName}: {scores[playerName]}{' ' * 11}Computer: {scores['Computer']}\n")

        if 3 in scores.values():
            print("#####################################################\n"
                f"#################### {list(scores.keys())[list(scores.values()).index(3)]} #######################\n"
                "#####################################################\n")
            state = False

    while True:
        answer = input("Do you want to play again (y or n)?: ")
        print("")

        if answer == "y": gameLogic()
        elif answer == "n": exit()
        else: print("Please enter y or no\n")

if __name__ == '__main__':
    gameLogic()