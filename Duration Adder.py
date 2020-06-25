dur = list()
while True:
    ask = input("How many durations you want to add?:")
    if ask.isdigit() == False:
        print ("The duration must be integer not string. Please enter again.")
    else:
        break
for i in range(int(ask)):
    while True:
        durations = input("{}. video's duration:".format(i+1))
        seg = durations.split(".")
        for i in range(len(seg)):
            if seg[i].isdigit() == False:
                print("The duration must be integer not string. Please enter again.")
            elif len(seg) >3:
                print ("Invalid input. Please enter again")
            else:
                pass
        break
    dur.append(durations)
def Counter(dur):
    sec = list()
    min = list()
    hour = list()
    for i in dur:
        seg = i.split(".")
        if len(seg) == 3:
            hour.append(int(seg[0]))
            min.append(int(seg[1]))
            sec.append(int(seg[2]))
        if len(seg) == 2:
            min.append(int(seg[0]))
            sec.append(int(seg[1]))
        if len(seg) == 1:
            min.append(int(seg[0]))
    quotient_sec = sum(sec)//60
    second = sum(sec)%60
    quotient_min = (sum(min)+quotient_sec)//60
    minute = (sum(min)+quotient_sec)%60
    hour = (sum(hour)+quotient_min)
    print ("\n{}.{}.{}\n".format(hour,minute,second))
    input("Press enter to exit")
Counter(dur)
