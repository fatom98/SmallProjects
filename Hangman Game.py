import os

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


def game():
    false_guess = 0

    true = list()
    false = list()

    print("Welcome to the AkGame's high tech hangman game :) \n")
    sentence = input("Please enter a name: ").strip()
    print(
        "*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n")

    empty = list(sentence.replace(" ", "/"))

    for char in range(len(empty)):
        if empty[char] != "/":
            empty[char] = "-"

    state = "continue"

    while state == "continue":

        print("     ","".join(empty), end="\n\n")

        guess = input("Enter your guess: ").strip()


        if guess == sentence:
            print("\nYou won the game. Congratulations\n")
            state = "end"

        elif false_guess == 11:
            print("\nYou lost :(. Sorry\n")
            state = "end"

        elif "/" in sentence or sentence == "":
            print("\nYour guess must consist of alpha numerical characters\n")

        elif guess in true:
            print(f"\nYou already said {guess} and i displayed it\n")

        elif guess in false:
            print(f"\nYou already said {guess} and it was false\n")

        elif guess in sentence:

            for i in range(len(sentence)):
                if guess == sentence[i]:
                    empty[i] = guess

            true.append(guess)

            if "-" not in empty:
                print("\nYou won the game. Congratulations\n")
                state = "end"

        else:
            print(HANGMAN[false_guess])
            false_guess += 1
            false.append(guess)

    again()


def again():
    while True:
        answer = input("Do you want to play again? (y or n):")

        if answer == "y":
            os.system("cls" if os.name == "nt" else "clear")
            game()

        elif answer == "n":
            exit()

        else:
            print("please type either y or n")


if __name__ == '__main__':
    game()