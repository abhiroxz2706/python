import random
class FruitQuiz:
    def __init__(self):
        self.fruits={"apple":"red","orange":"orange","watermelon":"green","banana":"yellow"}
    def quiz(self):
        flag=True
        while flag:
            fruit, color=random.choice(list(self.fruits.items()))
            print("What is the colour of {}".format(fruit))
            user_answer=input()
            if (user_answer.lower()==color):
                print("correct answer")
            else:
                print("wrong answer")

            option=int(input("enter 0 to quit, otherwise enter 1:"))
            if (option==0):
                flag=False
           
print("welcome to fruit quiz")
fq = FruitQuiz()
fq.quiz()