c1=int(input("enter speed of cyclist 1:"))
c2=int(input("enter speed of cyclist 2:"))
c3=int(input("enter speed of cyclist 3:"))

average=(c1+c2+c3)/3
print("average speed of cyclists is:", average)

if c1 < average:
    print("cyclist 1 is below average speed")
if c2 < average:
    print("cyclist 2 is below average speed")
if c3 < average:
    print("cyclist 3 is below average speed")