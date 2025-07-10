# word=input("Enter the word:")
# print(word[::-1])

word=input("Enter the word:")
rev=""
for i in word:
    rev=i+rev
print("Reverse:",rev)