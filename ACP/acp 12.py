n=int(input("Enter the no:"))
binary=''
temp=n
while temp > 0:
    binary=str(temp % 2) + binary
    temp=temp // 2
print(binary)