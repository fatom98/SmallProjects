import random
interval=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24",
          "25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46",
          "47","48","49","50","51","52","53","54","55","56","57","58","60","61","62","63","64","65","66","67","68","69",
          "70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89","90","91",
          "92","93","94","95","96","97","98","99"]
print ("!!!Welcome to the most exquisite game of all time :)!!!")
name = input("Please enter your name:")
while True:
    if name=="":
        print ("Name cant be blank. Please type your name.")
        name = input("Please enter your name:")
    else:
        break
print ("Welcome" + " " + name + ". " + "You're in a virtual reality guess game. Here how this game works. ")
print ("I kept a number in my mind which in between 0 and 100. You'll try to figure out the number by guessing. You have 7 guesses total.")
print ("When you make your guess i'll tell you if you are far away or close. ")
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
    while guess<8 and guess>1:
        while True:
            if answer not in interval:
                print ("Your entry is  not valid. Please type a number between 0 and 100")
                answer = input("Your guess is:")
            else:
                break
        if answer==str(number):

            print("woooow are you a kahin :)")
            again()
        elif answer>str(number):

            print("You went too far try a smaller number")
            guess -= 1

            print("Now you're left with" + " " + str(guess) + " " + "number of guesses. Choose wisely.")
            answer = input("Your guess is:")
        else:

            print("Is this your best guess? Try bigger numbers")
            guess -= 1
            print("Now you're left with" + " " + str(guess) + " " + "number of guesses. Choose wisely.")
            answer = input("Your guess is:")
    if guess==1:
        print
        print("HAHAHAHAHA. It was" + " " + str(number) + ".")
        again()
Guess()