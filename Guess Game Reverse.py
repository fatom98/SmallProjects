print("I will try to guess your number. Here we go")

guess = 50
false_guess = 0

while false_guess!=7:
    ans = input(f"Is it {guess}?: ")

    if ans=="yes":
        print (f"Americaaaaa fuck yeah\n{false_guess} turns it took to guess")
        break

    elif "upper" in ans: #inc guess

        if "close" in ans:  #inc 1< guess <10

            if "too" in ans:
                guess += 1
            else:
                guess += 5

        elif "far" in ans:

            if "too" in ans:
                guess += 15
            else:
                guess += 10

    elif "lower" in ans:

        if "close" in ans:

            if "too" in ans:
                guess -= 1
            else:
                guess -= 5

        elif "far" in ans:

            if "close" in ans:

                if "too" in ans:
                    guess -= 15
                else:
                    guess -= 10

    else:
        print("Invalid Entry. Please try again")
        continue

    false_guess += 1
    print(f"{7 - false_guess} turns left")