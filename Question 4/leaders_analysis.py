import numpy

leaders=numpy.loadtxt("leaders.txt")
leaders=leaders.astype(int)
print leaders[:10]

values = []
iold = -1
i = 0
while i < len(leaders):
    if leaders[i]!=iold:
        iold = leaders[i]
        counter = 0
        while i < len(leaders):
            if leaders[i] != iold:
                break
            counter = counter + 1
            i = i+1
        values.append([counter,iold])
    else:
        i=i+1
#values=sort(values)
values = sorted(values,key=lambda arr: arr[0])
print values[-10:]
        
