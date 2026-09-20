print("welcome")

score = 0

answer_1 = input("what languge are we using : ") 
if answer_1.lower() == "Python":
    print("bravo")
    score += 1
answer_2 = input("what command start a git : ") 
if answer_2.lower() == "git init":
    print("bravo")
    score += 1




else : 
    print("wrong")

print("your score is : ", score)