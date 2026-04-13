class Student:
    __schoolName='XYZ school' #private variable
    def __init__(self,name,age):
        self.__name=name #private instance attribute
        self.age=age
    def __display(self): #private method
        print("This is private method")


std=Student("Bill",25)
print(std.__schoolName)
std.display()