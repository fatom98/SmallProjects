import random

print ("Welcome to the AkTech's new hit game. The game is simple. You are going to enter a number, add to tour previous number and remember it.\n" \
       "For example if you said 3 you are going to type 3. on the next turn if you say 4 you are going to type 34. Good Luck :)\n")

class Number:

    def __init__(self):
        self.Users()
    def Users(self):
        self.users = {}
        while True:
            self.name1 = input("Please enter the first player's name:")
            print ("")
            if self.name1 == "":
                print ("Your name can not be empty. Please enter a valid name.\n")
            else:
                self.users[self.name1] = ""
                break
        while True:
            self.name2 = input("Please enter the second player's name:")
            print ("")
            if self.name2 == "":
                print ("Your name can not be empty. Please enter a valid name.\n")
            elif self.name2 == self.name1:
                print (f"{self.name2} is taken. Please enter another name\n")
            else:
                self.users[self.name2] = ""
                break
        self.Game()
    def Game(self):
        self.num = []
        self.players = []
        for i in self.users:
            self.players.append(i)
        for i in range(10):
            self.num.append(str(i))
        print ("Now i'll decide who goes first\n")
        self.first_player = random.choice(self.players)
        self.players.remove(self.first_player)
        self.second_player = random.choice(self.players)
        print (f"{self.first_player} starts first\n")
        while True:
            self.first_number = input(f"{self.second_player} enter {self.first_player}'s first number:")
            print ("")
            if len(self.first_number) != 1:
                print ("Number should be 1 digit. Please enter again\n")
            elif self.first_number not in self.num:
                print ("Your input should be an integer. Please enter again.\n")
            else:
                self.users[self.first_player]+=self.first_number
                break
        i = 0
        while True:
            if i%2==0:
                print (f"----- {self.first_player}'s Turn -----\n")
                print ("I'll print your number try to memorize it.*\n")
                print (f"{self.users[self.first_player]}\n")
                ready = input("Press Enter when you are ready?:")
                print("*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n")
                ask = input("Plese type your number:")
                print ("")

                if ask == self.users[self.first_player]:

                    print ("Correct. You entered right. Congratulations. Moving on.\n")

                    while True:

                        self.second_number = input(f"{self.first_player} enter {self.second_player}'s first number:")
                        print ("")

                        if len(self.second_number) != 1:

                            print ("Number should be 1 digit. Please enter again\n")

                        elif self.second_number not in self.num:

                            print ("Your input should be an integer. Please enter again.\n")

                        else:

                            self.users[self.second_player] += self.second_number
                            break

                else:

                    print (":( unfortunately that is wrong.\n")

                    print (f"################################## {self.second_player} Wins !!! ##################################\n")

                    try:
                        print (f"{self.second_player} remembered {self.second_number} digit number\n")
                    except AttributeError:
                        print(f"{self.second_player} could not even play.\n")



                    while True:

                        again = input("Do you want to play again? Y or N:")
                        print ("")

                        if again == "Y" or again == "y":

                            self.users()

                        elif again == "N" or again == "n":

                            exit()

                        else:

                            print ("You have to enter either Y or N")

            if i%2 == 1:

                print (f"----- {self.second_player}'s Turn -----")

                print ("I'll print your number try to memorize it.*\n")

                print(f"{self.users[self.second_player]}\n")

                ready = input("Press Enter when you are ready?:")
                print("*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n")

                ask = input("Plese type your number:")
                print ("")

                if ask == self.users[self.second_player]:

                    print ("Correct. You entered right. Congratulations. Moving on.\n")

                    while True:

                        self.first_number = input(f"{self.second_player} enter {self.first_player}'s first number:")
                        print ("")

                        if len(self.first_number) != 1:

                            print ("Number should be 1 digit. Please enter again\n")

                        elif self.first_number not in self.num:

                            print ("Your input should be an integer. Please enter again.\n")

                        else:

                            self.users[self.first_player] += self.first_number
                            break

                else:

                    print (":( unfortunately that is wrong.\n")

                    print (f"################################## {self.first_player} Wins !!! ##################################\n")

                    print (f"{self.first_player} remembered {self.first_number} digit number\n")


                    while True:

                        again = input("Do you want to play again? Y or N:")
                        print ("")

                        if again.lower() == "y":

                            self.users()

                        elif again.lower() == "n":

                            exit()

                        else:

                            print ("You have to enter either Y or N")

            i+=1

Number()