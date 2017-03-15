import numpy
import resource, sys
#resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

finishing_time = 1
leader = 0
counter = 0
max_counter = 0
def dfs(indarr, array, indicesprocessed, arrfinish, leaders):
    global finishing_time
    global leader
    global counter, max_counter
    counter = counter + 1
    if counter > max_counter:
        max_counter = counter
        print max_counter
    if indarr in indicesprocessed:
        return
    indicesprocessed.append(indarr)
    leaders.append(leader)
    for index in array[indarr]:
        if index in indicesprocessed:
            continue
        dfs(index, array, indicesprocessed, arrfinish, leaders)
    counter = counter - 1
    arrfinish.append([indarr,finishing_time])
    finishing_time = finishing_time + 1

f = open("scc.txt", "r")
#f = open("test.txt", "r")

direct = [[] for ind in range(0, 875714)]
reverse = [[] for ind in range(0, 875714)]
#direct = [[] for ind in range(0, 9)]
#reverse = [[] for ind in range(0, 9)]
for line in f:
    edge = line.split()
    indexdir = int(edge[0]) - 1
    indexrev = int(edge[1]) - 1

    if indexdir == indexrev:
        continue

    direct[indexdir].append(indexrev) 
    reverse[indexrev].append(indexdir)

#print "Direct = ", direct
#print "Reverse = ", reverse

# Depth first search
indicesprocessed = []
arrfinish = []
leaders = []
for index in range(0, 875714):
    dfs(index, reverse, indicesprocessed, arrfinish, leaders)

print arrfinish

#indicesprocessed = []
#arrfinish2 = []
#leaders = []
#for ind in range(875713,-1,-1):
#    find = arrfinish[ind][0]
#    leader = find
#    dfs(find, direct, indicesprocessed, arrfinish2, leaders)

#leaders.sort()
#iold = -1
#for i in leaders:
#    if i != iold:
#        print i,leaders.count(i)
#        iold = i

#print indicesprocessed, arrfinish, leaders
