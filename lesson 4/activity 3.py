print("enter your marks in each subjects out of 100")
maths=int(input("maths:"))
science=int(input("science:"))
social=int(input("social:"))
english=int(input("english:"))

sum=maths+science+social+english
print("total marks:",sum)

perc=sum/400*100
print("percentage obtained is",perc)
