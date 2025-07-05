a=input("Enter a alphabet:")

if a >= "a" and a <= "z":
  b=ord(a)
  print(b)
elif a >= "A" and a <= "Z":
  b=ord(a)
  print(b)
else:
  print("Enter a valid alphabet")