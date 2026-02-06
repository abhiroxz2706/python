class dog:
    animal="dog"

    def __init__(self,breed,color):
        self.breed=breed
        self.color=color


ob_1=dog("german sheperd","")
ob_2=dog("border collie","")

print("The breed of dog 1 is",ob_1.breed)
print("The breed of dog 2 is",ob_2.breed)