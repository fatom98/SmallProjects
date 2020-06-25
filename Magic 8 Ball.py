import random

question = None
while question != "":

    question = input("Ask the magic 8 ball a question (press enter to quit):\n")

    answers = random.randint(1, 8)

    if answers == 1:
        print ("It is certain")

    elif answers == 2:
        print ("Outlook good")

    elif answers == 3:
        print ("You may rely on it")

    elif answers == 4:
        print ("Ask again later")

    elif answers == 5:
        print ("Concentrate and ask again")

    elif answers == 6:
        print ("Reply hazy, try again")

    elif answers == 7:
        print ("My reply is no")

    elif answers == 8:
        print ("My sources say no")