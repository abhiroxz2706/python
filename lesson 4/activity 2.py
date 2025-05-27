amount=int(input("Enter amount:"))

note_100=amount//100
note_50=(amount%100)//50
note_10=((amount%100)%50)//10

print("total number of rs100 notes is",note_100)
print("total number of rs50 notes is",note_50)
print("total number of rs10 notes is",note_10)