a={"red","orange","pink","black","blue"}
b={"pink","black","grey","white","purple"}
print(a.union(b))#all colors
print(a.intersection(b))#common colors
print(a.difference(b))
print(b.difference(a))
print(a.symmetric_difference(b))