import random

numbers = list()

for i in range(40): numbers.append(str(i))

while True:
    ans = input("How many password do you want?:")

    if ans not in numbers: print("Your integer must be between 8 and 40. Please enter a valid number.")
    else: break

while True:
    leng = input("How long do you want your password to be?:")

    if leng not in numbers: print("Your integer must be between 8 and 40. Please enter a valid number.")
    else: break

for i in range(int(ans)):
    pas = list()

    C = random.sample("ABCDEFGHIJKLMNOPQRSTUVWXYZ", int(leng)//4)
    CH = random.sample("!'#+%&/*?-_@,.:;", int(leng) // 4)
    NUM = random.sample("0123456789", int(leng) // 4)
    SML = random.sample("abcdefghijklmnopqrstuvwxyz", int(leng)-int(leng)//4*3)

    for i in C: pas+= i
    for i in CH: pas+= i
    for i in NUM: pas+= i
    for i in SML: pas+= i

    random.shuffle(pas)
    password = "".join(pas)
    print (password)

input("Press enter to exit")

