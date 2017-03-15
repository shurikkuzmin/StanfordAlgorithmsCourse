import numpy

f = open("dijkstraData.txt", "r")
num = 200
arr = numpy.zeros((num, num), dtype = int)

for line in f:
    edge = line.split()
    row = int(edge[0]) - 1
    edge = edge[1:]

    for pair in edge:
        numbers=pair.split(",")
        column = int(numbers[0]) - 1 
        arr[row, column] = numbers[1]


# Dijkstra algorithm
processed = [0]
distances = [0]

toContinue = True
while toContinue:
    minLen = 10**10
    minNode = -1
    for indNode1, node1 in enumerate(processed):
        for node2 in range(0, num):
            edge = arr[node1, node2]
            if edge != 0:
                if not (node2 in processed):
                    if distances[indNode1] + edge < minLen:
                        minLen = distances[indNode1] + edge
                        minNode = node2

        # Grow network by minNode
    if minNode == -1:
        toContinue = False
    else:
        toContinue = True
        processed.append(minNode)
        distances.append(minLen)

    print "Processed ",minNode 

