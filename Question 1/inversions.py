import numpy

def countInversions(arr):
    if len(arr) ==1:
        return 0, arr

    length = len(arr)
    numLeft, left = countInversions(arr[0:length/2])
    numRight, right = countInversions(arr[length/2:])


    final = [0 for i in range(0,length)]
    i = 0
    j = 0
    num = numLeft + numRight
    for ind in range(0,length):
        if i == len(left):
            final[ind] = right[j]
            j = j + 1
            continue

        if j == len(right):
            final[ind] = left[i]
            i = i + 1
            continue

        if left[i] < right[j]:
            final[ind] = left[i]
            i = i + 1
        else:
            num = num + len(left) - i
            final[ind] = right[j]
            j = j + 1

    return num,final
if __name__=="__main__":

    arr = numpy.loadtxt("IntegerArray.txt")
    num,final = countInversions(arr)
    print num