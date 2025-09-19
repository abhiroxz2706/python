try:
    a,b=eval(input("enter two numbers seperated by comma:"))
    c=a + b
    print("answer=",c)

except SyntaxError:
    print("give numbers like 7,8")