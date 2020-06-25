myGrades = {
"chemistry": ["a-", 3], "calculus1":["a", 4], "phys1": ["b+", 4], "phys1L": ["a-", 1], "tur1": ["c+", 3], "economy": ["a", 3],
"biology": ["c+", 3], "calculus2": ["b+", 4], "phys2": ["b", 4], "phys2L": ["a", 1], "istanbul": ["c+", 3], "tur2": ["c+", 3],
"system": ["b+", 4], "discrete": ["a-", 3], "programming1": ["b-", 3], "algebra": ["a-", 3], "diff": ["b+", 3], "civ": ["c+", 3],
"digitalcom": ["b-", 4], "signal": ["b-", 3], "logic": ["b+", 3], "prob": ["d+", 3], "culture": ["a-", 3],
"devices": ["c", 3], "text": ["b", 3], "form": ["c-", 3], "art": ["a-", 3], "arc": ["c-", 3],
"circuit": ["b", 4], "micro1": ["b-", 4], "text2": ["b", 3], "form2": ["b", 3], "data": ["c", 3],
"com": ["a-", 3], "wave": ["b", 3], "ml": ["c", 3], "vision": ["c", 3], "robot": ["b+", 3], "practice": ["a", 3], "global1": ["b-", 3]
, "management": ["a-", 3], "structure": ["c+", 3], "software": ["c", 3], "oop": ["c-", 3],
"Nature and Knowledge": ["a-", 3], "algo2": ["b", 3], "Network": ["a-", 3], "computerSystems": ["a-", 3], "nano": ["c+", 3]
, "micro2":["b", 4], "cyber": ["c", 3], "os": ["a-", 3], "global2": ["b+", 3],"religion": ["b+", 3], "db" :["b", 3], "magnet": ["a", 3]
#Guess
, "control": ["b-", 3]

}
letterGrade = {"A+":4.1,"A":4.0,"A-":3.7,"B+":3.3,"B":3.0,"B-":2.7,"C+":2.3,"C":2.0,"C-":1.7,"D+":1.3,"D":1.0,"D-":0.5,"F":0.0,"IA":0.0}


def calculateGPA():
    totalScore = 0
    totalCredit = 0

    for lecture in myGrades:
        totalScore += letterGrade[myGrades[lecture][0].upper()] * myGrades[lecture][1]
        totalCredit += myGrades[lecture][1]

    gpa = totalScore/totalCredit

    return round(gpa, 2)

print(calculateGPA())

input("")
