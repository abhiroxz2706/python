import random

print("welcome to number guessing game")
print("guess a number from 1 to 100")
name=input("enter your name:")
print("hello",name)
print("you have 5 chances to guess the number")
flag=True
while flag:
    computer_choice=random.randint(1,100)
    if computer_choice % 2 == 0:
        print("Hint:the ans is an even number")
    else:
        print("Hint:the ans is an odd number")
    count=0
    for i in range(5):
        count+=1
        user_input=int(input("enter your guess:"))
        if computer_choice == user_input:
            print("your guess is correct")
            break
        else:
            print("your guess is incorrect")
    if count==5:
        print("your chances are over")
        ip=input("Do you want to play again? press Y for continue or press N for exit: ")
        if ip=="y" or ip=="Y":
            flag=True
        else:
            flag=False
            print("Thank you for playing")
