class vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
    def display(self):
        print("drive carefully")

class bus(vehicle):
    def __init__(self,name,max_speed,mileage,sleeper):
        vehicle.__init__(self,name,max_speed,mileage)
        self.sleeper=sleeper
    

ob=vehicle("Ford",200,25)
print("name:",ob.name)
print("max speed:",ob.max_speed)
print("mileage:",ob.mileage)

ob=bus("Volvo",180,20,"yes")
print("Name:", ob.name)
print("max speed:",ob.max_speed)
print("mileage:",ob.mileage)
print("sleeper:",ob.sleeper)