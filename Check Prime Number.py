numbers = list()
for i in range(1000000):
    numbers.append(str(i))
def is_prime():
    dividers = list()
    while True:
        number = input("Which number would you like to check?:")
        if int(number)<2:
            print("The numbers that are smaller than 2 can not be considered. ")
        elif number not in numbers:
            print("Yavru, eighter your number is too big or not a number. Please enter a valid number")
        else:
            break
    for i in range(2,int(number)):
        if int(number) % i == 0:
            dividers.append(i)
        else:
            pass
    if len(dividers) != 0:
        print("{} is not a prime number. It can be divided by {}".format(number,dividers))
    else:
        print("{} is a prime number.".format(number))
    yesno()
def yesno():
    while True:
        answer = input("Would you like to try another number?:").lower()
        if answer == "yes" or answer == "y":
            is_prime()
        elif answer == "no" or answer == "n":
            print("It was a pleasure to serve you. Have a nice day.")
            exit()
        else:
            print("Your answer should be yer or no. Please enter a valid answer")
is_prime()