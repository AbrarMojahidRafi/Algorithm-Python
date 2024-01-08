inputFileOpening = open("./input6.txt", "r")

# inputFile = ['9 // Total Elements\n', '10 11 10 6 7 9 8 15 2\n', '4 // Total queries\n', '5\n', '3\n', '2\n', '7']
inputFile = inputFileOpening.readlines()

l = inputFile[1].split(" ")

newList = []     # newList = [10, 11, 10, 6, 7, 9, 8, 15, 2]
for i in l:
    newList.append(int(i))

totalQueries = []        # totlaQueries = [5, 3, 2, 7]
for i in inputFile[3::]:
    totalQueries.append(int(i))

# main work starts from here

ansList = []
# going through each of the N-th position/query
for query in totalQueries:

    dumnyList = [i for i in newList]   # [10, 11, 10, 9, 15]

    # removing all the element that are between 1 to (N-1)th position
    count = 1
    while (count < query):
    
        minimumValue = float('inf')
        for value in dumnyList:
            if value < minimumValue:
                minimumValue = value
        dumnyList.remove(minimumValue)
        
        count += 1

    # finally, finding the N-th position value and append it in the list
    N_thPositionNumber = float('inf')
    for value in dumnyList:
        if value < N_thPositionNumber:
            N_thPositionNumber = value
    ansList.append(N_thPositionNumber)

# output file creating
outputFile = open("Output6.txt", "a")

for i in ansList:
    outputFile.writelines(f"{i}\n")

outputFile.close()
