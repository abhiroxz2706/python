student={"id1":99,"id2":98,"id3":99,"id4":97,"id5":96,"id6":98,"id7":100,"id8":97,"id1":99}
result={}

for key,mark in student.items():
    if mark not in result.values():
        result[key]=mark

print("without dupicates:",result)