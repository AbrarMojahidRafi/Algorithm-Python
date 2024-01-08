inputFileOpening = open("./input5.txt", "r")

# inputFile = ['8\n', '9 5 4 6 1 3 2 9']
inputFile = inputFileOpening.readlines()

l = inputFile[1].split(" ")

newList = []     # newList = [9, 5, 4, 6, 1, 3, 2, 9]
for i in l:
    newList.append(int(i))

# Quick Sort

def quickSort(arr, low, h):
    if low < h:
        # calling the partition function
        pivotPosition = partition(arr, low, h)
        # recursive call on left side
        quickSort(arr, low, pivotPosition - 1)
        # recursive call on right side
        quickSort(arr, pivotPosition + 1, h)

def partition(arr, left, right):
    pivot = arr[left]
    l = left
    r = right
    while True:

        # moving the l towards right.
        while (l <= r) and (arr[l] <= pivot):
            l += 1
        # moving the r towards left.
        while (l <= r) and (arr[r] >= pivot):
            r -= 1

        # checking if l and r crossed or not.
        if (l <= r):
            arr[l], arr[r] = arr[r], arr[l]
        else:
            # breaking, because in that case the l > r.
            break

    # putting the pivot in its perfect position.
    arr[left], arr[r] = arr[r], arr[left]
    # returning the pivot position
    return r

quickSort(newList, 0, len(newList)-1)

# print(newList)

# output file creating
outputFile = open("Output5.txt", "a")

# list to string
s = ""
for i in newList:
    s = s + str(i) + " "

outputFile.writelines(f"{s}")
outputFile.close()
