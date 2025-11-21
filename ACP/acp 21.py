num_1=int(input("Enter the number:"))
num_2=int(input("Enter the number:"))
lst=[]

for i in range(num_1,num_2):
        lst.append(i*i)
print(lst)
lst_even=[]
lst_odd=[]

for i in range(num_1,num_2):
        if (i*i) % 2 == 0:
            lst_even.append(i*i)
        else:
            lst_odd.append(i*i)

print("even numbers:",lst_even)
print("odd numbers:",lst_odd)            