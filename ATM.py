import datetime
users = {"Ahmed":"1234","Zeynep":"4321","Alberto":"4422"}
admins = {"Ibrahim":"1122"}
usact = {"Ahmed":{"balance":2000,"deposits":[],"withdrawal":[],"transfer":[]},"Zeynep":{"balance":3500,"deposits":[],"withdrawal":[],"transfer":[]},"Alberto":{"balance":1750,"deposits":[],"withdrawal":[],"transfer":[]}}
def main():
    print("     --- Welcome to Sehir Bank ---\n"
          "         -------------------\n"
          "        /      Istanbul     \ \n"
          "        |"+ str(datetime.datetime.now()).split(".")[0] + "|\n"
          "        \                   /\n"
          "         -------------------\n")
    print("1. Login\n2. Exit")
    while True:
        ask = input("Which one do you choose?:")
        if ask == "1":
            print("What do you want to login as:\n"
                  "1. Admin\n"
                  "2. User\n"
                  "3. Go Back")
            while True:
                ans = input("Which one do you choose?:")
                if ans == "1":
                    while True:
                        admus = input("Admin Name:")
                        admpass = input("Admin Password:")
                        if admus not in admins:
                            print("Invalid user name. Please enter again.")
                        elif admpass != admins[admus]:
                            print("Wrong Password. Please enter again")
                        else:
                            print("Welcome Ibrahim")
                            admin(users,usact)
                elif ans == "2":
                    login(users)
                elif ans == "3":
                    main()
                else:
                    print("Invalid entry. Please enter again")
        elif ask == "2":
            exit()
        else:
            print("Invalid entry. Please enter again")
def login(users):
    while True:
        usname = input("Please enter your username:")
        passwrd = input("Please enter your password")
        if usname not in users:
            print("Invalid username. Please enter again")
        elif passwrd != users[usname]:
            print("Invalid password. Please enter again")
        else:
            print(usname + " Welcome to Sehir Bank." )
            break
    menu(users,usact,usname,passwrd)
def menu(users,usact,usname,passwrd):
    print("Please enter the number of the service\n"
          "1. Withdraw Money\n"
          "2. Deposit Money\n"
          "3. Transfer Money\n"
          "4. My Account Information\n"
          "5. Logout")
    while True:
        ask = input("Please choose a service")
        if ask == "1":
            while True:
                wtd = input("Please enter the amount you want to withdraw:")
                if int(wtd) <= usact[usname]["balance"]:
                    usact[usname]["balance"] -= int(wtd)
                    usact[usname]["withdrawal"].append((wtd,str(datetime.datetime.now()).split(".")[0]))
                    print(wtd + "TL withdrawn from your account\n"
                          "Going back to main menu...")
                    menu(users,usact,usname,passwrd)
                else:
                    print("You dont have that much money.")
                    menu(users,usact,usname,passwrd)
        elif ask == "2":
            while True:
                dep = input("Please enter the amount you want to deposit:")
                usact[usname]["balance"] += int(dep)
                usact[usname]["deposits"].append((dep,str(datetime.datetime.now()).split(".")[0]))
                print(dep + "TL added to your account\n"
                            "Going back to main menu...")
                menu(users,usact,usname,passwrd)
        elif ask == "3":
           transfer(users,usact,usname,passwrd)
        elif ask == "4":
            print("--------- Sehir Bank ----------\n"
                  "----- "+str(datetime.datetime.now()).split(".")[0]+" -----\n"
                  "-------------------------------")
            print("Your Name: "+usname)
            print("your Password: "+passwrd)
            print("Your Balance Amount (TL): "+str(usact[usname]["balance"]))
            print("-------------------------------\n"
                  "User Activities Report:\n\n\n"
                  "Your Withdrawals:\n")
            for i in usact[usname]["withdrawal"]:
                print("     "+i[1] +" "+i[0])
            print("\n\nYour Deposits:\n")
            for i in usact[usname]["deposits"]:
                print("     "+i[1]+" "+i[0])
            print("\n\nYour Transfers:\n")
            for i in usact[usname]["transfer"]:
                print("     "+i[2]+" Transferred to "+i[1]+" "+i[0])
            print("\n\n-------------------------------\n"
                  "Going back to main menu...")
            menu(users,usact,usname,passwrd)
        elif ask == "5":
            print("You are loggin out. Thank you for choosing Sehir Bank. Whish to see you again")
            main()
        else:
            print("Invalid service. Please enter again")
def transfer(users,usact,usname,passwrd):
    print("Warning: If you want to abort the transfer please enter abort")
    while True:
        trans = input("Please enter the name of the user you want transfer money to:")
        if trans == "abort":
            print("Going back to main menu...")
            menu(users, usact, usname,passwrd)
        elif trans == usname:
            print("Transfering to user with the name " + trans + " is not possible!\n"
                                                                 "User does not exist!")
        elif trans not in users:
            print("Transfering to user with the name " + trans + " is not possible!\n"
                                                                 "User does not exist!")
        else:
            amount = input("Please enter the amount you want to transfer:")
            if int(amount) <= usact[usname]["balance"]:
                usact[usname]["balance"] -= int(amount)
                usact[usname]["transfer"].append((amount,trans,str(datetime.datetime.now()).split(".")[0]))
                print("Money transferred succesfully\n"
                      "Going back to the menu...")
                menu(users, usact, usname,passwrd)
            else:
                print("Sorry you dont have the entered amount \n\n"
                      "1. Go back to manin menu\n"
                      "2. Transfer again")
                while True:
                    sub = input("Which one do you choose?:")
                    if sub == "1":
                        menu(users,usact,usname,passwrd)
                    elif sub == "2":
                        transfer(users,usact,usname)
                    else:
                        print("Invalid entry. Please enter again")
def admin(users,usact):
    print("--- Admin Menu ---\n"
          "Please enter a number of the setting operations supported:\n"
          "1. Add User\n"
          "2. Remove User\n"
          "3. Display all Users\n"
          "4. Exit Admin Menu")
    while True:
        select = input("Which operation do you choose?:")
        if select == "1":
            print("Access Granted")
            nwus = input("Enter the new user name:")
            nwps = input("Enter the new user password")
            users[nwus] = nwps
            usact[nwus] = {"balance":5000,"deposits":[],"withdrawal":[],"transfer":[]}
            print(nwus+" was added as an user")
            admin(users,usact)
        elif select == "2":
            print("Access Granted")
            remove = input("Enter the username:")
            if remove not in users:
                print(remove+" does not exist as an user to Sehir Bank.")
                admin(users,usact)
            else:
                users.pop(remove)
                usact.pop(remove)
                print(remove+" was removed as an user to Sehir Bank")
                admin(users,usact)
        elif select == "3":
            c = 1
            for i in users:
                print(str(c)+". "+i+" "+users[i])
                c += 1
            print("-----------------")
            admin(users,usact)
        elif select == "4":
            main()
        else:
            print("Invalid entry. Please enter again.")
main()