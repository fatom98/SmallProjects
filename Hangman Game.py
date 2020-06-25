HANGMAN = [
"""
-----
|   |
|
|
| 
|
| 
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  |
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | | 
|
--------
"""]
def Hangman():
    false_guess = 0
    empty = ""
    true = list()
    false = list()
    print ("Welcome to the AkGame's high tech hangman game :).")
    sentence = input("Please enter the word or sentence:")
    print("*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n")
    line = sentence.replace(" ", "/")
    for i in range(len(line)):
        if line[i] != "/":
            empty += "-"
        else:
            empty += line[i]
    print (empty)
    count = list(line)
    display = list(empty)
    print ("If you wanna guess the whole sentence you have to type found")
    guess = input("Your guess is?:")
    while True:
        if false_guess == 10:
            false_guess = 0
            lost()
        if guess == "found":
            final = input("woooow bold move. Lets see if it's true:")
            if final == sentence:
                print ("wooooow it's true. Are you kahin")
                again()
                break
            else:
                lost()
        if len(guess) != 1:
            print ("Your guess must be either a letter or found")
            guess = input("Your guess is?:")
        if guess in true:
            print ("You already said {} and i displated it. Please type another thing".format(guess))
            guess = input("Your guess is?:")
        if guess in false:
            print ("You already said {} and it was false. Please type another thing".format(guess))
            guess = input("Your guess is?:")
        elif guess in count:
            for i in range(len(count)):
                if guess == count[i]:
                    display[i] = count[i]
                else:
                    pass
            print ("".join(display))
            true.append(guess)
            guess = input("Your guess is?:")
        else:
            print (HANGMAN[false_guess])
            false_guess += 1
            false.append(guess)
            guess = input("Your guess is?:")
def again():
    answer = input("Do you want to play again? yes or no:")
    while True:
        if answer == "yes":
            Hangman()
        if answer == "no":
            break
        else:
            print ("please type eiter yes or no")
            answer = input("Do you want to play again? yes or no:")
def lost():
    print ("you lost the game sorry :(")
    again()
Hangman()