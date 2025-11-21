t=(1,0,0,0,1,1,1,0,1) #0 sunny 1 rainy
sc=0
rc=0
for i in (t):
    if i==1:
        rc=rc+1
    else:
        sc=sc+1
if sc > rc:
    print("sunny day")
else:
    print("rainy day")