import random

print ("!!! Welcome to the most exquisite game of all time :)!!!")
name = input("Please enter your name: ")
while True:
    if name=="":
        print ("Name can't be blank. Please type your name.")
        name = int(input("Please enter your name: "))
    else:
        break
print (f"Welcome {name}. You're in a virtual reality guess game. Here how this game works. ")
print ("I kept a number in my mind which in between 0 and 100. You'll try to figure out the number by guessing. You have 7 guesses total.")
print ("When you make your guess i'll tell you if you are far away or close. ")
print ("Lets begin. Good Luck :)")
def again():
    while True:
        choice = input("You wanna play again?: ")
        if choice.lower() == "yes":
            Guess()
        elif choice.lower() == "no":
            print ("Ok. It was nice seeing you. I hope we'll meet again. Stay safe by then")
            exit()
        else:
            print ("I dont know what that is. Please type yes or no")
def Guess():
    number = random.randint(1,100)
    answer = int(input("\nYour guess is: "))
    guess=7
    while guess<8 and guess>1:
        while True:
            if answer > 100:
                print ("Your entry is not valid. Please type a number between 0 and 100")
                try:
                    answer = int(input("Your guess is: "))
                except:
                    print('Please Enter Integer values Only !')
            else:
                break
        if answer==number:

            print("woooow are you a kahin :)")
            again()
        elif answer>number:

            print("You went too far try a smaller number")
            guess -= 1

            print(f"Now you're left with {guess} number of guesses. Choose wisely.\n")
            try:
                answer = int(input("Your guess is: "))
            except:
                print('Please Enter Integer values Only !')        
                
        else:
            print("Is this your best guess? Try bigger numbers")
            guess -= 1
            print(f"Now you're left with {guess} number of guesses. Choose wisely.\n")
            try:
                answer = int(input("Your guess is: "))
            except:
                print('Please Enter Integer values Only !')
    if guess==1:
        print(f"HAHAHAHAHA. It was {number}.")
        again()
Guess()