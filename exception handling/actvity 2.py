try:
    m=int(input("enter the account number:"))
    print("account number:",m)

except ValueError:
    print("give valid numbers like 7878387,33788787 etc.Account numbers should not have letters")