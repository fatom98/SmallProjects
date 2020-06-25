import random
import copy

names = []

def main():
    
    while True:
        number = input("Please enter the amounth of people: ")
        if number.isdigit() == False:
            print("Please enter a number not something else")
        elif int(number) % 2 != 0:
            print("You cant enter odd number of people. Please enter an even number")
        else:
            counter = 1
            for i in range(int(number)):
                n = input(f"Please enter {counter}. Name: ")
                names.append(n)
                counter += 1
            break
    sort(names)
    
def sort(names):
    sorte = []
    trial = copy.copy(names)
    for i in range(len(names)//2):
        a = random.choice(trial)
        trial.remove(a)
        b = random.choice(trial)
        trial.remove(b)
        sorte.append((a,b))
    print(sorte)
    again()
    
def again():
    while True:
        again = input("Do you want me to shuffle again?:")
        if again == "yes" or again == "y":
            sort(names)
        elif again == "no" or again == "n":
            print("It was nice seeing you. See you later :)")
            exit()
        else:
            print("Your entry should be yes or no. Please enter again")
            
main()

