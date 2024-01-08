inputFileOpening = open("./input4.txt", "r")

# inputFile = ['5 2\n', '1 10\n', '2 10\n', '6 7\n', '4 8\n', '3 6']
inputFile = inputFileOpening.readlines()

scheduleList = []          # scheduleList = [[1, 10], [2, 10], [6, 7], [4, 8], [3, 6]]
for i in range(1, len(inputFile)):
    var = inputFile[i].split(" ")
    scheduleList.append([int(var[0]), int(var[1])])

# scheduleList ke end time er upor base kore sort korlam.
lastInterval = []
for i in scheduleList:
    lastInterval.append(i[1])

lastInterval.sort()        # lastInterval = [6, 7, 8, 10, 10]

intervals = []      # intervals = [[3, 6], [6, 7], [4, 8], [1, 10], [2, 10]]
for i in lastInterval:
    for j in scheduleList:
        if i == j[1]:
            if j not in intervals:
                intervals.append(j)

# part1: moving forward, and trying to count the best suitable intervals


def forward(intervals):
    # selecting the time slot from the sorted intervals...

    people = int(inputFile[0].split(" ")[1])

    selectedSchedule = []

    for i in range(people):
        pointer1 = 0
        dumny = [intervals[pointer1]]
        for j in range(1, len(intervals)):
            if intervals[pointer1][1] <= intervals[j][0]:
                dumny.append(intervals[j])
                pointer1 = j
        selectedSchedule.append(dumny)

        for i in dumny:
            intervals.remove(i)

    # print(selectedSchedule)

    # count the maximum number of activities that can be completed
    count = 0
    for i in selectedSchedule:
        count += len(i)
    return count


dumnyForward = [i for i in intervals]
forwardCount = forward(dumnyForward)

# part1: moving backward, and trying to count the best suitable intervals


def backward(intervals):

    people = int(inputFile[0].split(" ")[1])

    selectedSchedule = []

    for i in range(people):
        pointer1 = len(intervals) - 1
        dumny = [intervals[pointer1]]
        for j in range(len(intervals)-1-1, -1, -1):
            if intervals[pointer1][0] >= intervals[j][1]:
                dumny.append(intervals[j])
                pointer1 = j
        selectedSchedule.append(dumny)

        for i in dumny:
            intervals.remove(i)

    # print(selectedSchedule)

    # count the maximum number of activities that can be completed
    count = 0
    for i in selectedSchedule:
        count += len(i)
    return count


dumnyBackward = [i for i in intervals]
backwardCount = backward(dumnyBackward)

maximumNumOfActivity = None
if forwardCount > backwardCount:
    maximumNumOfActivity = forwardCount
else:
    maximumNumOfActivity = backwardCount

# Output file creating
outputFile = open("Output4.txt", "a")

outputFile.writelines(f"{maximumNumOfActivity}")

outputFile.close()
