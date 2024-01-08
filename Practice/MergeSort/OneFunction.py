# sample input: 3 7 2 8 1 9 6 5
# sample output: [1, 2, 3, 5, 6, 7, 8, 9]


userInput = input("Enter list elements which are ONLY seperated by SPACE: ")

userInput = userInput.split(" ")

userList = []
for i in userInput:
    userList.append(int(i))


def mergeSort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    leftSide = mergeSort(arr[:mid])
    rightSide = mergeSort(arr[mid:])

    if leftSide and rightSide:
        l1 = l2 = 0
        arrayIndex = 0
        while l1 < len(leftSide) and l2 < len(rightSide):
            if leftSide[l1] < rightSide[l2]:
                arr[arrayIndex] = leftSide[l1]
                l1 += 1
                arrayIndex += 1
            else:
                arr[arrayIndex] = rightSide[l2]
                l2 += 1
                arrayIndex += 1

        while l1 < len(leftSide) and l2 >= len(rightSide):
            arr[arrayIndex] = leftSide[l1]
            l1 += 1
            arrayIndex += 1

        if l2 < len(rightSide) and l1 >= len(leftSide):
            arr[arrayIndex] = rightSide[l2]
            l2 += 1
            arrayIndex += 1

        # this return is required, Because it returns the sorted list which length have more than 1(1<). And by using this return our code can be able to get a list(which length have more than 1(1<)), and then again it is start doing to combine the lists.
        return arr


print("Before sort operation", userList)
mergeSort(userList)
print("After sort operation", userList)
