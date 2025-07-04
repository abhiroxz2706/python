mc=input("do you have medical condition?y for yes and n for no: ")

if mc=="y":
    print("you are eligible to write exams")
elif mc=="n":
    ap=int(input("enter your attendance percentage:"))
    if ap > 75:
        print("you are eligible to write exams")
else:
    print("you are not eligible to write exams")
