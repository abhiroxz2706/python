word=input("enter the word: ")
letter=input("enter the letter: ")

for i in word:
    if i == letter:
        print("letter found")
        break
else:
    print("letter not found")

    