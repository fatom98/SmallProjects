users = {"admin":["sehir123"], "Ahmet": ["123", 900, {"mathematics": 3, "physics": 4}], "Ayse": ["456", 400, {"physics": 4, "programming": 3}]}

courses = {"physics": 4, "mathematics": 3, "programming": 3}


def login():
    print("****Welcome to Course Management System****\nPlease provide login information\n")

    while True:
        global userId
        userId = input("Username: ")
        userPassword = input("Password: ")

        if userId not in users: print("Invalid id. Please try again\n")
        elif userPassword != users[userId][0]: print("Your password doesnt match with your id. Please try again\n")
        else: break

    if userId == "admin": adminMenu()
    else: studentMenu()


def adminMenu():
    print("\nWelcome Admin! What do you want to do?\n"
            "1-List courses\n"
            "2-Create a course\n"
            "3-Delete a course\n"
            "4-Show students registered to a course\n"
            "5-Users Budget Menu\n"
            "6-List Users\n"
            "7-Create User\n"
            "8-Delete User\n"
            "9-Exit\n")

    choices = ["1","2","3","4","5","6","7","8","9"]

    while True:
        adminChoice = input("Your choice: ")
        if adminChoice not in choices: print("Invalid option number. Please enter a valid number.\n")
        else: break

    if adminChoice == "1":
        print("*** Offered Courses ***\nCourse Name             Credit")
        for i, j in enumerate(courses, start=1):
            print(str(i)+"-"+j+(25-len(j))*" "+str(courses[j]))
        adminMenu()

    elif adminChoice == "2":
        newCourseName = input("What is the name of the course that you want to add?: ")
        newCredit = input("How many credits this course has?: ")
        print(newCourseName+" will be added "+newCredit+" credits.\n")

        while True:
            anser = input("Are you sure?: ").upper()
            if anser == "Y":
                print(newCourseName+" has been added to courses with "+newCredit+" credits.\n")
                courses[newCourseName] = newCredit
                break
            elif anser == "N":
                print("Ok. Nothing happened.\n")
                break
            else: print("Your answer only can be Y or N.\n")
        adminMenu()

    elif adminChoice == "3":
        print("Course Name             Credit")
        for i, j in enumerate(courses, start=1):
            print(str(i)+"-"+j+(25-len(j))*" "+str(courses[j]))

        while True:
            delCourseName = int(input("Which course do you want to delete?: "))
            if delCourseName <= 0 and delCourseName > len(courses): print("Invalid course number. Please enter again\n")
            else: break

        deletedCourseName = list(courses.keys())[delCourseName-1]
        courses.pop(deletedCourseName)
        for i in users:
            if i == "admin": continue
            elif deletedCourseName in users[i][2]:
                users[i][1] += users[i][2][deletedCourseName] * 100
                users[i][2].pop(deletedCourseName)

        print(deletedCourseName+" has been deleted and money has been transfered back to students accounts\n")

    elif adminChoice == "4":
        showeCourseName = input("Which course do you want to show?: ")
        courseTakers = list()

        if showeCourseName not in courses:
            print("This course doesn't exist, please provide a valid input\n")
        else:
            print("Course Name: "+showeCourseName+"\nStudents taking mathematics:")
            for i in users:
                if i == "admin": continue
                elif showeCourseName in users[i][2]: courseTakers.append(i)

            if len(courseTakers) != 0:
                for i, j in enumerate(courseTakers, start=1):
                    print(str(i)+"-"+j)
            else:
                print("No one is taking this course")
        adminMenu()

    elif adminChoice == "5":
        print("User          Money")
        for i,j in enumerate(users):
            if j == "admin": continue
            print(str(i)+"-"+j+(13-len(j))*" "+str(users[j][1]))
        print("What do you want to do?\n"
                "1-Add money to user\n"
                "2-Subtract money from user\n"
                "3-Back to admin menu\n")

        while True:
            choose = int(input("Your choice: "))
            if choose != 1 and choose != 2 and choose !=3: print("Invalid option. Please enter again")
            else: break

        if choose == 1:
            print("Which user do you want add money to their account?")
            for i, j in enumerate(users):
                if j == "admin": continue
                print(str(i)+"-"+j)

            while True:
                addMoneyName = int(input("Your choice?: "))
                if addMoneyName<1 and addMoneyName>len(users): print("Invalid option. please enter again")
                else: break

            addMoneyName = list(users)[addMoneyName]

            much = int(input("How much money do you want to add?: "))
            print(str(much)+" will be added to "+addMoneyName)

            while True:
                sure = input("Are you sure?: ").upper()
                if sure == "Y":
                    users[addMoneyName][1] += much
                    print(str(much) + " added to " + addMoneyName)
                    break
                elif sure == "N":
                    print("Ok. Nothing happened")
                    break
                else: print("Invalid option. Please enter again.")

            adminMenu()

        elif choose == 2:
            print("Which user do you want subtract money from their account?")
            for i, j in enumerate(users):
                if j == "admin": continue
                print(str(i) + "-" + j)

            while True:
                addMoneyName = int(input("Your choice?: "))
                if addMoneyName < 1 and addMoneyName > len(users):
                    print("Invalid option. please enter again")
                else:
                    break

            addMoneyName = list(users)[addMoneyName]

            much = int(input("How much money do you want to subtract?: "))
            print(str(much) + " will be subtracted from " + addMoneyName)

            while True:
                sure = input("Are you sure?: ").upper()
                if sure == "Y":
                    users[addMoneyName][1] -= much
                    print(str(much) + " subtracted from " + addMoneyName)
                    break
                elif sure == "N":
                    print("Ok. Nothing happened")
                    break
                else:
                    print("Invalid option. Please enter again.")
            adminMenu()

        elif choose == 3:
            adminMenu()

    elif adminChoice == "6":
        print("Current Users:")
        for i,j in enumerate(users):
            if j == "admin": continue
            print(str(i)+"-"+j)
        adminMenu()

    elif adminChoice == "7":
        newUser = input("What is the name of user that you want to create? ")
        newPassword = input("What is the password for account?")
        newBudget = int(input("How much money do you want user to have?"))
        users[newUser] = [newPassword, newBudget, dict()]
        print("The new user has been added successfully!")

        adminMenu()

    elif adminChoice == "8":
        print("Current Users:")
        for i, j in enumerate(users):
            if j == "admin": continue
            print(str(i) + "-" + j)

        while True:
            delete = input("What is the name of user that you want to delete?")

            if delete not in users: print("User doesn't exist. Please enter another user name.")
            elif delete != "admin":
                users.pop(delete)
                print("User succesfully deleted.\n")
                break

        adminMenu()

    elif adminChoice == "9":
        login()

def studentMenu():
    print("\nWelcome "+userId+" What do you want to do?\n"
            "1-Add courses to my courses\n"
            "2-Delete a course from my courses\n"
            "3-Show my courses\n"
            "4-Budget Menu\n"
            "5-Exit\n")

    options = ["1","2","3","4","5"]

    while True:
        choice = input("Your choice: ")
        if choice not in options: print("Invalid option. Please enter again.\n")
        else: break

    if choice == "1":
        print("*** Offered Courses ***\nCourse Name             Credit")
        for i, j in enumerate(courses, start=1):
            print(str(i) + "-" + j + (25 - len(j)) * " " + str(courses[j]))

        while True:
            courseSelect = int(input("Which course do you want to take (Enter 0 to go to main menu)?"))
            if courseSelect == 0: studentMenu()
            elif courseSelect <= 0 and courseSelect > len(courses): print("Invalid course number. Please enter again\n")
            else:
                selectedCourseName = list(courses.keys())[courseSelect - 1]
                if selectedCourseName in users[userId][2]: print("This course is already in your profile\n")
                elif users[userId][1] < courses[selectedCourseName] * 100: print("You dont have enough money to enroll in this class\n")
                else:
                    users[userId][2][selectedCourseName] = courses[selectedCourseName]
                    users[userId][1] -= courses[selectedCourseName] * 100
                    print("\n"+selectedCourseName+" has been successfully added to your courses.")
                    break

        studentMenu()

    elif choice == "2":
        print("Course Name             Credit")
        for i, j in enumerate(users[userId][2], start=1):
            print(str(i) + "-" + j + (25 - len(j)) * " " + str(courses[j]))

        while True:
            number = int(input("Which course do you want to remove?: "))
            if number <= 0 and number > len(users[userId][2]): print("Invalid course number. Please enter again\n")
            else: break

        courseName = list(users[userId][2].keys())[number-1]
        refund = courses[courseName]*100
        print("\nYou have chosen: "+courseName+"\n"+str(refund)+"$ will be returned to your account\n")

        while True:
            anser = input("Are you sure you want to remove this course?: ").upper()
            if anser == "Y":
                users[userId][2].pop(courseName)
                users[userId][1] += refund
                print("Course has been deleted from your profile\n")
                break

            elif anser == "N":
                print("Ok. Nothing happened.\n")
                break

            else:
                print("Your answer only can be Y or N.\n")
        studentMenu()

    elif choice == "3":
        print("Your courses\nCourse Name             Credit")
        for i, j in enumerate(users[userId][2], start=1):
            print(str(i) + "-" + j + (25 - len(j)) * " " + str(users[userId][2][j]))

        studentMenu()

    elif choice == "4":
        print("#### BUDGET MENU #####\nYour budget is: "+str(users[userId][1])+"$\n\n")
        print("What do you want to do?\n"
                "1-Add Money\n"
                "2-Go to main menu\n")

        while True:
            answer = int(input("Your choice: "))
            if answer != 1 and answer != 2: print("Invalid option. Please enter again")
            else: break

        if answer == 1:
            amount = int(input("Amount of money: "))
            users[userId][1] += amount
            print("Your budget has been updated.\n")

            studentMenu()

        elif answer == 2:
            studentMenu()

    elif choice == "5":
        login()

login()
