student={"id1":99,"id2":98,"id3":99,"id4":97,"id5":96,"id6":98,"id7":100,"id8":97,"id1":99}
K=int(input("enter the number to check:"))
result=0

for key in student:
    if student[key]==K:
        result+=1

print("number of times",K,"is present in the dictionary:",result)
