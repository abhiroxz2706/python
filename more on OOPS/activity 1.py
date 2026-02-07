class IOString:
    def __init__(self):
        self.str1=''
    def getip(self):
        self.str1=input("enter the word:")
    def change(self):
        print("upppercase=",self.str1.upper())

obj=IOString()
obj.getip()
obj.change()