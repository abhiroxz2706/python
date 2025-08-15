def add(n,m):
    c=n+m
    return c

def sub(n,m):
    c=n-m
    return c

def mul(n,m):
    c=n*m
    return c

def div(n,m):
    c=n/m
    return c


a=int(input("enter the no:"))
b=int(input("enter the no:"))
answer=add(a,b)
print("sum:",answer)
answer=sub(a,b)
print("difference:",answer)
answer=mul(a,b)
print("product:",answer)
answer=div(a,b)
print("quotient:",answer)