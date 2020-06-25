import random

allnumbers = []

for i in range(0,10001):
    allnumbers.append(str(i))
    allnumbers.append(str(-i))

falseansw = 0

operations = ["+", "-", "*", "/", "%"]

numbers1 = ["1","2","3","4","5","6","7","8","9","10"]

numbers2 = []

for i in range(1,101):
    numbers2.append(str(i))

print ("Welcome to the random math question game!")

def level1(falseansw):

    strpoint = 0

    inuse = [operations[0]]

    print ("Level1:")

    print ("Possible length of Numbers: 1")

    print ("Possible number of Operators: 1")

    for i in range(5):
        nb1 = random.choice(numbers1)
        nb2 = random.choice(numbers1)
        op = random.choice(inuse)
        cransw = str(eval(nb1 + op + nb2))
        print (strpoint * "*")
        ans = input("what is "+nb1+op+nb2+" ?:")
        while True:
            if  ans not in allnumbers:
                print ("ERROR! Un-acceptable entry detected, try again please!")
                ans = input("what is " + nb1 + op + nb2 + " ?:")
            else:
                break
        if ans == cransw:
            strpoint += 1
            print ("Correct! You gain an additional star! You now have %s out of five stars!" % (strpoint))
        if ans != cransw:
            falseansw+=1
            print ("Wrong! You do not gain any stars for that question!")
            print ("You now have %s out of five stars!" % (strpoint))
    if strpoint<3:
        print ("You do not have enough stars to move on to the next level, this as far as you go!")
        exit()
    elif strpoint>=3:
        print ("You have enough stars this level, time to move on!")
        level2(falseansw)

def level2(falseansw):
    strpoint = 0

    inuse = [operations[0],operations[1]]

    print ("Level2:")

    print ("Possible length of Numbers: 1")

    print ("Possible number of Operators: 2")

    for i in range(5):
        nb1 = random.choice(numbers1)
        nb2 = random.choice(numbers1)
        op = random.choice(inuse)
        cransw = str(eval(nb1 + op + nb2))
        print (strpoint * "*")
        ans = input("what is " + nb1 + op + nb2 + " ?:")
        while True:
            if ans not in allnumbers:
                print ("ERROR! Un-acceptable entry detected, try again please!")
                ans = raw_input("what is " + nb1 + op + nb2 + " ?:")
            else:
                break
        if ans == cransw:
            strpoint += 1
            print ("Correct! You gain an additional star! You now have %s out of five stars!" % (strpoint))
        if ans != cransw:
            falseansw += 1
            print ("Wrong! You do not gain any stars for that question!")
            print ("You now have %s out of five stars!" % (strpoint))
    if strpoint < 3:
        print ("You do not have enough stars to move on to the next level, this as far as you go!")
        exit()
    if strpoint >= 3:
        print ("You have enough stars this level, time to move on!")
        level3(falseansw)

def level3(falseansw):
    strpoint = 0

    inuse = [operations[0], operations[1],operations[2]]

    print ("Level3:")

    print ("Possible length of Numbers: 1")

    print ("Possible number of Operators: 3")

    for i in range(5):
        nb1 = random.choice(numbers1)
        nb2 = random.choice(numbers1)
        op = random.choice(inuse)
        cransw = str(eval(nb1 + op + nb2))
        
        print (strpoint * "*")
        ans = input("what is " + nb1 + op + nb2 + " ?:")
        while True:
            if ans not in allnumbers:
                print ("ERROR! Un-acceptable entry detected, try again please!")
                ans = input("what is " + nb1 + op + nb2 + " ?:")
            else:
                break
        if ans == cransw:
            strpoint += 1
            print ("Correct! You gain an additional star! You now have %s out of five stars!" % (strpoint))
        if ans != cransw:
            falseansw += 1
            print ("Wrong! You do not gain any stars for that question!")
            print ("You now have %s out of five stars!" % (strpoint))
    if strpoint < 3:
        print ("You do not have enough stars to move on to the next level, this as far as you go!")
        exit()
    if strpoint >= 3:
        print ("You have enough stars this level, time to move on!")
        level4(falseansw)

def level4(falseansw):
    strpoint = 0

    inuse = [operations[0], operations[1],operations[2],operations[3]]

    print ("Level4:")

    print ("Possible length of Numbers: 2")

    print ("Possible number of Operators: 4")

    for i in range(5):
        nb1 = random.choice(numbers1)
        nb2 = random.choice(numbers1)
        op = random.choice(inuse)
        cransw = str(eval(nb1 + op + nb2))
        print (strpoint * "*")
        ans = input("what is " + nb1 + op + nb2 + " ?:")
        while True:
            if ans not in allnumbers:
                print ("ERROR! Un-acceptable entry detected, try again please!")
                ans = input("what is " + nb1 + op + nb2 + " ?:")
            else:
                break
        if ans == cransw:
            strpoint += 1
            print ("Correct! You gain an additional star! You now have %s out of five stars!" % (strpoint))
        if ans != cransw:
            falseansw += 1
            print ("Wrong! You do not gain any stars for that question!")
            print ("You now have %s out of five stars!" % (strpoint))
    if strpoint < 3:
        print ("You do not have enough stars to move on to the next level, this as far as you go!")
        exit()
    if strpoint >= 3:
        print ("You have enough stars this level, time to move on!")
        level5(falseansw)

def level5(falseansw):
    strpoint = 0

    inuse = [operations[0], operations[1],operations[2],operations[3],operations[4]]

    print ("Level5:")

    print ("Possible length of Numbers: 2")

    print ("Possible number of Operators: 5")

    for i in range(5):
        nb1 = random.choice(numbers1)
        nb2 = random.choice(numbers1)
        op = random.choice(inuse)
        cransw = str(eval(nb1 + op + nb2))
        print (strpoint * "*")
        ans = input("what is " + nb1 + op + nb2 + " ?:")
        while True:
            if ans not in allnumbers:
                print ("ERROR! Un-acceptable entry detected, try again please!")
                ans = input("what is " + nb1 + op + nb2 + " ?:")
            else:
                break
        if ans == cransw:
            strpoint += 1
            print ("Correct! You gain an additional star! You now have %s out of five stars!" % (strpoint))
        if ans != cransw:
            falseansw += 1
            print ("Wrong! You do not gain any stars for that question!")
            print ("You now have %s out of five stars!" % (strpoint))
    if strpoint < 3:
        print ("You do not have enough stars to move on to the next level, this as far as you go!")
        exit()
    if strpoint >= 3:
        print ("You have enough stars this level, time to move on!")
        print ("Amazing! You beat the game! You answered a total of %s answers wrong this attempt" % (falseansw))
        exit()

level1(falseansw)
