sentence=input("Enter a sentence: ")
word=input("Enter a word: ")
if word in sentence:
    print(word,"is present in the",sentence)
else:
    print(word,"is not present in the",sentence)