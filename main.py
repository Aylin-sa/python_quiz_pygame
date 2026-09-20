from question import questions
name = input("whats your name : ")

print("welcome")

score = 0
for item in questions:
    answer = input(item["question"])

    if answer.lower() == item["answer"]:
        print("correct")
        score += 1
    else: 
        print("wrong")

print("your score is : ", score, "out of", len(questions))

if score == len(questions):
    print("exellent job" , name)
elif score == len(questions):
    print("exellent job" , name)
else:
    print("keep peacticing", name)

with open("rezult.txt", "a") as file:
    file.write(f"{name} - {score}/{len(questions)}\n")