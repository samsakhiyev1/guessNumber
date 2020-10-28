import random

number = random.randint(0, 1001)

while True:
    answer = input("Enter the number: ")
    if not answer or answer == "exit":
        break

    if not answer.isdigit():
        print("Enter integer number")
        continue
    user_answer = int(answer)

    if user_answer > number:
        print ("Number is lower")
    elif user_answer < number:
        print("Number is higher")
    else:
        print("BINGO!!!")
        break
