height=int(input("Enter your height in cm: "))
weight=int(input("Enter your weight in kg: "))
bmi=weight/(height/100)**2

if bmi<=18.5:
    print("You are underweight")
elif bmi<=24.9:
    print("You are healthy")
elif bmi<=34.5:
    print("You are overweight")
elif bmi<=39.9:
    print("You are obese")
else:
    print("You are extremely obese")