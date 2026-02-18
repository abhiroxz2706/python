class Circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        return 3.14*self.r*self.r
    def perimeter(self):
        return 2*3.14*self.r

ob=Circle(5.6)
print(ob.area())
print(ob.perimeter())