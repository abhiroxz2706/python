from abc import ABC

class Animal(ABC):
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk and run")

class Snake(Animal):
    def move(self):
        print("I can crawl")

R=Human()
K=Snake()

for i in (R,K):
    i.move()
