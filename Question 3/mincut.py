import numpy
import random

fname = "kargerMinCut.txt"
#fname = "test.txt"
#fname = "test2.txt"

for main in range(0,100):
    indices = []
    connections = []

    with open(fname, "r") as ins:
        for line in ins:
            nums = [int(x)  for x in line.split()]
            indices.append(nums[0])
            connections.append(nums[1:])
            

    # Min cut algorithm
    # Pick up a random edge
    random.seed()

    while len(indices) > 2:
        rind = random.randint(0, len(indices) - 1)
        cind = random.randint(0, len(connections[rind]) - 1)

        elem1 = indices[rind]
        conn1 = connections[rind]
     
        elem2 = conn1[cind]   
        rind2 = indices.index(elem2) 
        conn2 = connections[rind2]

        # Delete references to each other
        while(conn1.count(elem2) != 0):
            conn1.remove(elem2)

        while(conn2.count(elem1) != 0):
            conn2.remove(elem1)

        for i in conn2:
            j = indices.index(i)

            for kind, k in enumerate(connections[j]):
                if k == elem2:
                    connections[j][kind] = elem1

        # Now merge two lists
        for i in range(0, len(conn2)):
            conn1.append(conn2[i])

        # Remove the second node
        indices.remove(elem2)
        connections[rind2] = [-9999]
        connections.remove([-9999])

    print "Num = ", len(connections[0])
