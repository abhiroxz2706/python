num=int(input("Enter a number:"))
digits=0
while num > 0:
    digits=digits+1
    num=num//10
print("The number of digits in the number is:",digits)