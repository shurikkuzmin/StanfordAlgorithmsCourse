import numpy

arr = numpy.loadtxt("algo1-programming_prob-2sum.txt",dtype=int)

stuff = dict()
for ind,num in enumerate(arr):
    stuff[num] = ind    

values=[]
for t in range(-10000,10001):
    for val in stuff:
        if (t-val in stuff) and (t-val != val):
            values.append(t)
            print t
            break