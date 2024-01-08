inputFileOpening = open("./input3.txt", "r")

# inputFile = ['6\n', '1 3\n', '2 5\n', '3 7\n', '4 6\n', '6 8\n', '7 9']
inputFile = inputFileOpening.readlines()

inputFileSize = int(inputFile[0])

scheduleList = []          # scheduleList = [[1, 4], [2, 5], [6, 7], [4, 8], [3, 6]]
for i in range(1, len(inputFile)):
    var = inputFile[i].split(" ")
    scheduleList.append([int(var[0]), int(var[1])])

# scheduleList ke end time er upor base kore sort korlam.
lastInterval = []
for i in scheduleList:
    lastInterval.append(i[1])

lastInterval.sort()   # lastInterval = [3,5,6,7,8,9]

intervals = []      # intervals = [[1, 4], [2, 5], [3, 6], [6, 7], [4, 8]]
for i in lastInterval:
    # i = 3
    for j in scheduleList:   # j = [1, 4]
        if i == j[1]:
            intervals.append(j)

# selecting the time slot from the sorted intervals...
pointer1 = 0
selectedSchedule = [intervals[0]]
for pointer2 in range(1, len(intervals)):
    if intervals[pointer1][1] <= intervals[pointer2][0]:   # 0=startingTime; 1=endingTime
        selectedSchedule.append(intervals[pointer2])
        pointer1 = pointer2

# print(selectedSchedule)

# Output file creating
outputFile = open("Output3.txt", "a")

outputFile.writelines(f"{len(selectedSchedule)}\n")
for i in selectedSchedule:
    outputFile.writelines(f"{i[0]} {i[1]}\n")

outputFile.close()
