import random
options=["rock","paper","scissor"]
cc=random.choice(options)
uc=input("enter your choice:rock,paper or scissor:")

if uc==cc:
    print("its a tie")

elif uc=="rock" and cc=="paper":
    print("computer wins")

elif uc=="paper" and cc=="rock":
    print("you win")

elif uc=="paper" and cc=="scissor":
    print("computer wins")

elif uc=="scissor" and cc=="paper":
    print("you win")

elif uc=="scissor" and cc=="rock":
    print("computer wins")

elif uc=="rock" and cc=="scissor":
    print("you win")

else:
    print("invalid input")