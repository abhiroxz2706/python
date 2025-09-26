import random
print("Welcome to number guessing game")
print("Guess a number from 1 to 10")
computer_choice=random.randint(1,10)
user_choice=int(input("Enter your guess:"))

if computer_choice==user_choice:
    print("You win")

else:
    print("Your guess is wrong.You lose")
    print("Computer choice was:",computer_choice)