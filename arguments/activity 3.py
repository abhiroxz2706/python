n=int(input("enter the number:"))

if n==0 or n==1:
    print("Answer:",1)

else:
    ans=1
    for i in range(1,n+1):
        ans=ans*i
    print("Answer:",ans)