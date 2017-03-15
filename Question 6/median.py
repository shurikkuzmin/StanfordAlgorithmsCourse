import numpy
import heapq


arr=numpy.loadtxt("Median.txt", dtype = int)

heap=[]
medians=[]
#for i in range(len(arr)):
for i in range(0,len(arr)):
    heapq.heappush(heap,arr[i])
    if (i % 2) == 0:
        val=heapq.nsmallest(i/2 + 1,heap)[-1]
        medians.append(val)
    else:
        val=heapq.nsmallest((i + 1)/2,heap)[-1]
        medians.append(val)

medians = numpy.array(medians)
print numpy.sum(medians) % 10000