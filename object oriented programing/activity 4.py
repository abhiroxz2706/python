class parrot:
    species="bird"

    def __init__(self,name,age):
        self.name=name
        self.age=age

obj=parrot("parrot",4)

print(obj.species)
print(obj.name,obj.age)
