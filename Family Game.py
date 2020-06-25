import random
yes_no = ["yes","no","y","n"]
numbers = list()
for i in range(10000,100000):
    control = dict()
    for j in str(i):
        if j not in control:
            control[j] = 1
        else:
            control[j] += 1
    if len(control.values()) == 5:
        numbers.append(str(i))
def Game():
    t = 1
    players = list()
    print("\nWelcome to the Akbulut Dynasty's fun family game.\n")
    print("Please enter gamers names.\n")
    while True:
        name1 = input("First player's name is?:")
        if name1 == "":
            print("\nPlease enter a valid name.\n")
        else:
            break
    print("")
    while True:
        name2 = input("Second player's name is?:")
        if name2 == "":
            print("\nPlease enter a valid name.\n")
        elif name2 == name1:
            print("\n{} is already taken. Please enter another name\n".format(name1))
        else:
            break
    players.append(name1)
    players.append(name2)
    print("\nNow i'll decide who is gonna start first.\n")
    decision = random.choice(players)
    if decision == name1:
        first = name1
        second = name2
    else:
        first = name2
        second = name1
    print("{} is the first player\n".format(first))
    print("{}, please enter your number but remember your number must be a positive 5 digit non repeting number.\n".format(first))
    while True:
        first_nb = input("Your number is?:")
        if first_nb not in numbers:
            print("\nYour number should be a 5 digit positive number and should not repeat. Please enter another valid number.\n")
        else:
            break
    print("*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n")
    print("{}, please enter your number but remember your number must be a positive 5 digit non repeating number.\n".format(second))
    while True:
        second_nb = input("Your number is?:")
        if second_nb not in numbers:
            print("\nYour number should be a 5 digit positive number and should not repeat. Please enter another valid number.\n")
        else:
            break
    print("*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n")
    while True:
        if t%2 == 1:
            plus = list()
            minus = list()
            print("It is {}'s turn. Try to guess {}'s number\n".format(first,second))
            while True:
                guess = input("Your guess is:")
                if guess not in numbers:
                    print("\nYour number should be a 5 digit positive number and should not repeat. Please enter another valid number.\n")
                else:
                    if guess == second_nb:
                        print("\n################################## {} Wins !!! ##################################\n".format(first))
                        Again()
                    for i in range(5):
                        if guess[i] == second_nb[i]:
                            plus.append(guess[i])
                    for i in guess:
                        for j in second_nb:
                            if i in j and i not in plus:
                                minus.append(int(i))
                    print("+{}, -{}\n".format(len(plus),len(minus)))
                    break
            t += 1
        if t%2 == 0:
            plus = list()
            minus = list()
            print("It is {}'s turn. Try to guess {}'s number\n".format(second, first))
            while True:
                guess = input("Your guess is:")
                if guess not in numbers:
                    print("\nYour number should be a 5 digit positive number and should not repeat. Please enter another valid number.\n")
                else:
                    if guess == first_nb:
                        print("\n################################## {} Wins !!! ##################################\n".format(second))
                        Again()
                    for i in range(5):
                        if guess[i] == first_nb[i]:
                            plus.append(guess[i])
                    for i in guess:
                        for j in first_nb:
                            if i in j and i not in plus:
                                minus.append(int(i))
                    print("+{}, -{}\n".format(len(plus), len(minus)))
                    break
            t += 1
def Again():
    while True:
        answer = input("Do you want to play again?:").lower()
        if answer not in yes_no:
            print("\nYour answer should be either yes or no\n")
        elif answer == "yes" or answer == "y":
            Game()
        else:
            print("\nIt was nice to play with you i hope we will meet again soon. Good bye.\n")
            exit()
Game()