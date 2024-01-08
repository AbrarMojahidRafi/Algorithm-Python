inputFileOpening = open("./input1.txt", "r")

# inputFile = ['8\n', '9 5 4 6 1 3 2 9']
inputFile = inputFileOpening.readlines()

l = inputFile[1].split(" ")

newList = []      # newList = [9, 5, 4, 6, 1, 3, 2, 9]
for i in l:
    newList.append(int(i))

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        a1 = mergeSort(arr[:mid])  # write the parameter
        a2 = mergeSort(arr[mid:])  # write the parameter
        return merge(a1, a2)          # complete the merge function above

def merge(a, b):
    # write your code here
    # Here a and b are two sorted list
    dumnyList = []

    i = j = 0

    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            dumnyList.append(b[j])
            j += 1
        else:
            dumnyList.append(a[i])
            i += 1

    while (i < len(a)):
        dumnyList.append(a[i])
        i += 1

    while (j < len(b)):
        dumnyList.append(b[j])
        j += 1

    return dumnyList
    # merge function will return a sorted list after merging a and b


mergeArray = mergeSort(newList)

s = ""      # s = 1 2 3 4 5 6 9 9
for i in mergeArray:
    s = s + str(i) + " "

# creating output file
outputFile = open("Output1.txt", "a")
outputFile.writelines(s)
outputFile.close()
