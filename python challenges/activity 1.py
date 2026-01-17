import random

computer_choice=random.randint(7,20)


print("guess the number from 7 to 20")
if computer_choice % 2 == 0:
    print("Hint:the ans is an even number")
else:
    print("Hint:the ans is an odd number")
user_input=int(input("enter your guess:"))

if computer_choice == user_input:
    print("your guess is correct")
else:
    print("your guess is incorrect")
    print("the correct ans is:",computer_choice)
