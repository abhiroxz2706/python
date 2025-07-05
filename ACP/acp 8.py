#with temporary variable
num_1=int(input("enter a number:"))
num_2=int(input("enter a number:"))

temp=num_1
swap_1=num_2
swap_2=temp

print(swap_1)
print(swap_2)

#without temporary variable
num_3=int(input("enter a number:"))
num_4=int(input("enter a number:"))

swap_3,swap_4=num_4,num_3

print(swap_3,swap_4)