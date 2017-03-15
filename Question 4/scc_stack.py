import numpy

f = open("scc.txt", "r")
num = 875714

#f = open("test.txt", "r")
#num = 9

#f = open("test2.txt", "r")
#num = 9

#f = open("test3.txt", "r")
#num = 11

#f = open("test4.txt", "r")
#num = 11

#f = open("test5.txt", "r")
#num = 5

direct = [[] for ind in range(0, num)]
reverse = [[] for ind in range(0, num)]
for line in f:
    edge = line.split()
    indexdir = int(edge[0]) - 1
    indexrev = int(edge[1]) - 1

    if indexdir == indexrev:
        continue

    direct[indexdir].append(indexrev) 
    reverse[indexrev].append(indexdir)

rstack = []
rorder = []

rprocessed = [1 for ind in range(0, num)]
for rind in range(0, num):
    if rprocessed[rind] == 0:
        continue

    rprocessed[rind] = 0
    rorder.insert(0,rind)
    
    rpos=0
    while rpos != -1:
        ind = rorder[rpos]
        flag = True

        for ind2 in reverse[ind]:
            if rprocessed[ind2] == 0:
                continue
            flag = False
            rpos = rpos + 1
            rprocessed[ind2] = 0
            rorder.insert(rpos,ind2)

        if flag:
            rpos = rpos-1
        #print rorder
            
print "Done with reverse!"
#print rorder
rorder.reverse()

dstack = []
leaders = []
leaders2 = []

dprocessed = [1 for ind in range(0, num)]
for find in range(num-1,-1,-1):
    dind = rorder[find]
    if dprocessed[dind] == 0:
        continue
    dprocessed[dind] = 0
    dstack.append(dind)
    leaders.append(dind)
    leaders2.append([dind,dind])
    while len(dstack) != 0:
        ind = dstack[0]
        dstack.remove(dstack[0])
        for ind2 in direct[ind]:
            if dprocessed[ind2] == 0:
                continue

            dprocessed[ind2] = 0
            dstack.insert(0, ind2)
            leaders.append(dind)
            leaders2.append([ind2,dind])

#print "Leaders=",leaders
#print "Leaders2=",leaders2

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

values = sorted(values,key=lambda arr: arr[0])
#print values[]


#print "Order=",rorder
#print "Processed=",rprocessed
#print "Finish=",rfinish
#print "Leaders=",leaders
