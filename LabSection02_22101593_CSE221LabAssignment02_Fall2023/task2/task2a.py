inputFileOpen = open("./input2a.txt", "r")

# inputFile = ['4\n', '1 3 5 7\n', '4\n', '2 2 4 8']
#                0         1         2         3 
inputFile = inputFileOpen.readlines()

# making list1
l1 = inputFile[1].split(" ")    # l1 = ['1', '3', '5', '7\n']

list1 = []        # list1 = [1, 3, 5, 7]
for i in l1:
    list1.append(int(i))

# making list2
l2 = inputFile[3].split(" ")

list2 = []        # list2 = [2, 2, 4, 8]
for i in l2:
    list2.append(int(i))

# Merge the lists.....
myList = []       # myList = [1, 3, 5, 7, 2, 2, 4, 8]
#                   index =   0  1  2  3  4  5  6  7
for i in list1:
    myList.append(i)
for i in list2:
    myList.append(i)

# Merge sort


def mergeSort(arr):
    if len(arr) == 1:
        return arr
    elif len(arr) > 1:
        mid = len(arr)//2
        # print(arr, mid)
        firstHalf = mergeSort(arr[0:mid])
        # print(arr, mid)
        secondtHalf = mergeSort(arr[mid:])

        # newList = [0]*(len(arr))

        i = j = newListIndex = 0

        while (i < len(firstHalf)) and (j < len(secondtHalf)):
            if firstHalf[i] > secondtHalf[j]:
                arr[newListIndex] = secondtHalf[j]
                j += 1
            else:
                arr[newListIndex] = firstHalf[i]
                i += 1
            newListIndex += 1
    
        while (i < len(firstHalf)):
            arr[newListIndex] = firstHalf[i]
            i += 1
            newListIndex += 1

        while (j < len(secondtHalf)):
            arr[newListIndex] = secondtHalf[j]
            j += 1
            newListIndex += 1

        # print(arr, firstHalf, secondtHalf, arr)
        return arr


sortedList = mergeSort(myList)

# Generating the output

s = ""
for i in sortedList:
    s = s + str(i) + " "

outputFileCreating = open("output2a.txt", "a")
outputFileCreating.writelines(s)
outputFileCreating.close()
