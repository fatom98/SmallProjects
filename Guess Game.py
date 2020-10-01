import random

print ("!!!Welcome to the most exquisite game of all time :)!!!")
name = input("Please enter your name:")
while True:
    if name=="":
        print ("Name cant be blank. Please type your name.")
        name = input("Please enter your name:")
    else:
        break

print (f"Welcome {name}. You're in a virtual reality guess game. Here how this game works. ")
print ("I kept a number in my mind which in between 0 and 100. You'll try to figure out the number by guessing. You have 7 guesses total.")
print ("When you make your guess I'll tell you if you are far away or close. ")
print ("Lets begin. Good Luck :)")
def again():
    while True:
        choice = input("You wanna play again?:")
        if choice == "yes":
            Guess()
        elif choice == "no":
            print ("Ok. It was nice seing you. I hope we'll meet again. Stay safe by then")
            break
        else:
            print ("I dont know what that is. Please type yes or no")
                    
def Guess():
    number = random.randint(1,100)
    answer = input("Your guess is:")
    guess=7
    while guess<8 and guess>0:
        if answer not in range(100):
            print ("Your entry is  not valid. Please type a number between 0 and 100")
            answer = input("Your guess is:")
        
        elif answer==str(number):

            print("woooow are you a kahin :)")
            again()
                    
        elif answer>str(number):

            print("You went too far try a smaller number")
            guess -= 1

            print(f"Now you're left with {guess} number of guesses. Choose wisely.")
            answer = input("Your guess is:")
          
        else:
            print("Is this your best guess? Try bigger numbers")
            guess -= 1
            print(f"Now you're left with {guess} number of guesses. Choose wisely.")
            answer = input("Your guess is:")
    if guess==0:
        print
        print(f"HAHAHAHAHA. It was {number}.)
        again()
Guess()
