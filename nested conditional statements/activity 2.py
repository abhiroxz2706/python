uc=int(input("enter the units consumed:"))

if uc < 50:
    amount=uc*2.60+25
elif uc >= 50 and uc < 100:
    amount=uc*3.25+35
elif uc >= 100 and uc < 200:
    amount=uc*5.26+45
else:
    amount=uc*8.45+75

print("electricity bill is:", amount)