try:
    num1=int(input("enter the numerator:"))
    num2=int(input("enter the denominator:"))
    ans=num1 / num2
    print("answer=",ans)

except ZeroDivisionError:
    print("the denominator should not be zero")