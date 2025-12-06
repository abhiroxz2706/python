test_dictionary={"codingal":3,"is":2,"'best":2,"for":2,"coding":1}
user_input=int(input("enter the number to check:"))
num_times=0

for key in test_dictionary:
    if test_dictionary[key]==user_input:
        num_times+=1

print(num_times)