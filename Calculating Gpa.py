yes_no = ["yes","no","y","n"]
numbers = list()
info = dict()
for i in range(12):
    numbers.append(str(i))
print ("Hmmm i think you are in trouble if you are using this but i think i can help you. Lets calculate your GPA.")
letter_grade = {"A+":4.1,"A":4.0,"A-":3.7,"B+":3.3,"B":3.0,"B-":2.7,"C+":2.3,"C":2.0,"C-":1.7,"D+":1.3,"D":1.0,"D-":0.5,"F":0.0,"IA":0.0}
def General():
    total = 0
    totalCredit = 0
    while True:
        lesson_number = input("how many lessons have you enrolled?:")
        if lesson_number not in numbers:
            print("please enter an integer.")
        else:
             break
    for i in range(int(lesson_number)):
            name = input("what is your {}lesson's name?:".format(str(i+1)+"."))
            while True:
                credit = input("what is the credit for {}?:".format(name))
                if credit not in numbers:
                    print("Please enter an integer.")
                else:
                    break
            while True:
                grade = input("What is the grade that you got?:").upper()
                if grade not in letter_grade:
                    print("Please enter a valid letter grade.")
                else:
                    break
            info[name] = [int(credit),grade]
    print(info)
    for i in info:
        total += (info[i][0]*letter_grade[info[i][1]])
        totalCredit += info[i][0]
    gpa = total / totalCredit
    gpa = float("{:.2f}".format(gpa))
    print(gpa)
    while True:
        ask = input("Do you want to keep chancing your grade (y or n)?:").lower()
        if ask not in yes_no:
            print("Please answer the question either yes or no.")
        else:
            Modified(info)

def Modified(info):
    total = 0
    tc = 0
    for i in info:
        while True:
            grade = input("What is the grade that you got from {}?:".format(i)).upper()
            if grade not in letter_grade:
                print("Please enter a valid letter grade")
            else:
                info[i][1] = grade
                break
    print(info)
    for i in info:
        total += (info[i][0]*letter_grade[info[i][1]])
        tc += info[i][0]
    gpa = total/tc
    gpa = float("{:.2f}".format(gpa))
    print(gpa)
    while True:
        ask = input("Do you want to keep chancing your grade (y or n)?:").lower()
        if ask not in yes_no:
            print("Please answer the question either yes or no.")
        elif ask == "n":
            exit()
        else:
            Modified(info)

General()