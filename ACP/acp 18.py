try:
    age_input=int(input("Enter your age:"))
    if age_input == int:
        even_check= age_input % 2 == 0
        print("Provided age is an even number")
    
    else:
        odd_check= age_input % 2 != 0
        print("Provided age is an odd number")

except ValueError:
    print("Entered value is not an integer. User should not enter decimal or letters.")

