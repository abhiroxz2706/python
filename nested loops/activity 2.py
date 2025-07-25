word=input("enter the word:")
letter=input("enter the letter:")
count=0
for i in word:
    if i==letter:
        count=count+1
print("the letter",letter,"is present",count,"times in the word",word)