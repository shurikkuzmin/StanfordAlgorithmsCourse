import numpy

def partition(arr, left, right):
    leftelem = arr[left]
    rightelem = arr[right-1]
    if (right - left) % 2 == 1:
        indmiddle = (right + left - 1)/2
        middleelem = arr[indmiddle]
    else:
        indmiddle = (right + left)/2 - 1
        middleelem = arr[indmiddle]

    indexch = left
    if middleelem > min(leftelem, rightelem) and middleelem < max(leftelem, rightelem):
        indexch = indmiddle

    if (rightelem > min(leftelem, middleelem) and rightelem < max(leftelem, middleelem)):
        indexch = right -1

    temp = arr[left]
    arr[left] = arr[indexch]
    arr[indexch] = temp 

    elem = arr[left]
    i = left +1
    for j in range(left + 1, right):
        if arr[j] < elem:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
            i = i + 1
    temp = arr[left]
    arr[left] = arr[i-1]
    arr[i-1] = temp 
    return i-1, right - left - 1

def quicksort(arr, left, right):
    if right <= left+1:
        return 0;
    middle, num_part = partition(arr, left, right)
    num_left = 0
    num_right = 0

    if middle - 1 > left:
        num_left = quicksort(arr, left, middle)
    if middle + 1 < right:
        num_right = quicksort(arr, middle + 1, right)
        
    return num_left + num_right + num_part


arr = numpy.loadtxt("QuickSort.txt", dtype = int)

