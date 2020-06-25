def Verify():
    print("\nWelcome If you want to verify your credit card number, You are in the right place\n")
    while True:
        number = input("Please enter your credit card number:")
        if number.isdigit() == False:
            print("\nYour number should be integer. Please enter a 16 digit integer.\n")
        elif len(number) != 16:
            print("\nYour number should be 16 digit. Please enter a 16 digit integer.\n")
        else:
            Execution(number)
            break
def Execution(number):
    hulu = list()
    for i in range(len(number)):
        hulu.append(int(number[-(i+1)]))
    for ind,value in enumerate(hulu):
        if ind % 2 == 1:
            value = value * 2
            if len(str(value))!=1:
                check = list()
                for i in str(value):
                    check.append(int(i))
                value = sum(check)
                hulu[ind] = value
            else:
                hulu[ind] = value
        else:
            pass
    if sum(hulu) % 10 == 0:
        print("\nYour credit card number checks out. It is ready to use :).\n")
        Again()
    else:
        print("\nYour credit card number is fake. Please alert the authorities immidiatly.\n")
        Again()
def Again():
    yes_no = ["yes", "no", "y", "n"]
    while True:
        answer = input("Do you want to check another card?:").lower()
        if answer not in yes_no:
            print("\nYour answer should be either yes or no\n")
        elif answer == "yes" or answer == "y":
            Verify()
        else:
            print("\nIt was nice to play with you i hope we will meet again soon. Good bye.\n")
            exit()
Verify()