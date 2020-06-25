import random
questions = {"Q1": {"Question": "What color are Zebras?", "ans1": ["White with black stripes", "True"],
                    "ans2": ["Black with white stripes", "False"], "ans3": ["Black with red stripes", "False"]},
             "Q2": {"Question": "Where was the old Campus of Sehir University?", "ans1": ["Altunizade", "True"],
                    "ans2": ["Levent", "False"], "ans3": ["Maltepe", "False"]}}
users = {"5577": ["abbas", 5.4], "5551": ["omer", 6.4], "5466": ["betul", 3.2]}

new_users = {"abbas":["5577",5.4],"omer":["5551",6.4],"betul":["5466",3.2]}

prize = 10000

def main_menu(prize,questions,users):

    print "--- Welcome to Sehir Hadi :) ---"

    PhoneNb = raw_input("Please type your phone number in order to sign in:")

    while True:

        if PhoneNb =="**":
            admin_menu(prize,questions,users)
            break

        if PhoneNb not in users:
            print "Checking ",PhoneNb," ...."
            print PhoneNb," is not a valid phone number, please try again!"
            PhoneNb = raw_input("Please type your phone number in order to sign in:")

        else:
            print "Checking ",PhoneNb," ...."
            print "Welcome ",users[PhoneNb][0]

            Logic(prize,new_users,PhoneNb,users)
            break

def admin_menu(prize,questions,users):# this is the main menu function that plays the content of the sub menu.
    k = 3
    new_question = 3
    arr = ["1","2","3","4","5","6"]
    print "Welcome Sehir Hadi Admin Section, please choose one of the following options:"
    print "1 - Set prize for the next competition."
    print "2 - Display questions for the next competition."
    print "3 - Add new question to the next competition."
    print "4 - Delete a question from the next competition."
    print "5 - See users data."
    print "6 - Log out."


    menu_choice = raw_input("Please choose a menu number:")

    while True:
        if menu_choice not in arr:
            print "Invalid menu number. Please choose a menu number: "
            menu_choice = raw_input("Please choose a menu number:")
        else:
            break

    if menu_choice == "1": # to setting prize the menu
        prize_value = raw_input("Please type the total prize of the next competition:")
        print "Setting prize...\n" \
              "Going back to Admin Menu..."
        prize = prize_value
        admin_menu(prize,questions,users)

    if menu_choice == "2": # to see the question.
        for item in questions:
            print "--- ",item," : ",questions[item]["Question"]," ---"
            print "ans 1. ",questions[item]["ans1"][0]," >",questions[item]["ans1"][1]
            print "ans 2. ",questions[item]["ans2"][0]," >",questions[item]["ans2"][1]
            print "ans 3. ",questions[item]["ans3"][0]," >",questions[item]["ans3"][1]
        print "Going back to admin menu"
        admin_menu(prize,questions,users)

    if menu_choice == "3": # to add  a new question.
        question_number = "Q" + str(len(questions) + 1)
        temporary = {question_number: {"Question": raw_input("Please type the question:"),
                                       "ans1": [raw_input("Please type the CORRECT answer:"), "True"],
                                       "ans2": [raw_input("Please type an incorrect answer:"), "False"],
                                       "ans3": [raw_input("Please type an incorrect answer:"), "False"]}}
        questions.update(temporary)
        print "Adding to the questions database....."
        print "Done..."
        print "Going back to admin menu"
        admin_menu(prize, questions, users)

    if menu_choice == "4": #to delete question
        array = list()

        for i in range(len(questions)):
            array.append(str(i+1))

        for i in questions:
            print i+". "+questions[i]["Question"]

        to_be_deleted = raw_input("Please type the number of the question to be deleted:")

        while True:
            if to_be_deleted not in array:
                print "Invalid choice. Please type the number of the question to be deleted:"
                to_be_deleted = raw_input("Please type the number of the question to be deleted:")
            else:
                index = "Q"+str(to_be_deleted)
                questions.pop(index)
                print questions
                print index+" has been deleted successfully!!"
                print "Going back to the Admin menu.."
                admin_menu(prize,questions,users)

    if menu_choice == "5": # to see the users' datas.
        for i in users:
            print users[i][0]+", Balance:"+str(users[i][1])+", Phone Number:"+i

        print "Going back to the Admin menu.."
        admin_menu(prize,questions,users)

    if menu_choice == "6": # this is the beginning function of the game ,  starting game
        main_menu(prize,questions,users)

def Logic(prize,new_users,PhoneNb,users):

    use = list() # taken random players

    user1 = users[PhoneNb][0] # main player

    users.pop(PhoneNb)

    for i in users:

        use.append(users[i][0])

    user2 = random.choice(use) # a random player

    use.remove(user2)

    user3 = random.choice(use) # another random player

    #user status exist for the eliminated players

    user1_status = 1

    user2_status = 1

    user3_status = 1

    chrs = ["1","2","3"] # chrs exist fot the to choose a answer randomly by the players

    print "The Game Is Starting. Please Fasten Your Seat Belt :)."

    for item in questions:

        print "************************* Total Players: " + str(len(new_users))

        total_ans = {"ans1": 0, "ans2": 0, "ans3": 0}

        if user2_status == 1:

            user2_choice = random.choice(chrs)

            answer = "ans" + user2_choice

            total_ans[answer]+=1

            if questions[item][answer][1] == "True":
                pass
            else:
                user2_status = 0
                new_users.pop(user2)

        if user3_status == 1:

            user3_choice = random.choice(chrs)

            answer = "ans" + user3_choice

            total_ans[answer]+=1

            if questions[item][answer][1] == "True":
                pass
            else:
                user3_status = 0
                new_users.pop(user3)

        if user1_status == 1:

            print "--- ", item, " : ", questions[item]["Question"], " ---"
            print "ans 1. ", questions[item]["ans1"][0]
            print "ans 2. ", questions[item]["ans2"][0]
            print "ans 3. ", questions[item]["ans3"][0]
            answ = raw_input("Your answer:")
            ques = "ans"+answ

            total_ans[ques]+=1

            if questions[item][ques][1] == "True":
                print "Correct"
                pass
            else:
                print "Incorrect"
                user1_status = 0
                new_users.pop(user1)

            print "Evaluating the responses of the other competitors...."
            print "ans 1. ", questions[item]["ans1"][0]+"... total answers:"+str(total_ans["ans1"])
            print "ans 2. ", questions[item]["ans2"][0]+"... total answers:"+str(total_ans["ans2"])
            print "ans 3. ", questions[item]["ans3"][0]+"... total answers:"+str(total_ans["ans3"])

        else:

            print "--- ", item, " : ", questions[item]["Question"], " ---"
            print "ans 1. ", questions[item]["ans1"][0]+"... total answers:"+str(total_ans["ans1"])
            print "ans 2. ", questions[item]["ans2"][0]+"... total answers:"+str(total_ans["ans2"])
            print "ans 3. ", questions[item]["ans3"][0]+"... total answers:"+str(total_ans["ans3"])

            print "Evaluating the responses of the other competitors...."
            print "ans 1. ", questions[item]["ans1"][0] + "... total answers:" + str(total_ans["ans1"])
            print "ans 2. ", questions[item]["ans2"][0] + "... total answers:" + str(total_ans["ans2"])
            print "ans 3. ", questions[item]["ans3"][0] + "... total answers:" + str(total_ans["ans3"])


    print "-- Total Winners:"+str(len(new_users))

    print "-- Total distributed prize:"+str(prize)

    for i in new_users:

       print  i+" -->"+ str(int(prize)/len(new_users))+" - Current Balance:"+ str(new_users[i][1]+prize/len(new_users))


    print "See you later :)"

    main_menu(prize,questions,users)




main_menu(prize,questions,users)

















