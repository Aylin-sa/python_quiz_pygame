import os
from dotenv import load_dotenv
from question import questions

load_dotenv()
admin_password = os.getenv("QUIZ_AMSIN_PASSWORD")

open_admin = input("do u want to open admin made ? yes/no : ")

if open_admin.lower() == "yes":
    entered_password = input("enter admin password : ")
    if entered_password == admin_password:
        print("admin! hi....")
    else:
        print("")

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