def cube(num):
    return num**3

def div(num):
    if num % 3==0:
        return cube(num)
    else:
        return False
    
number=int(input("enter the number:"))
ans=div(number)
print("Answer:",ans)