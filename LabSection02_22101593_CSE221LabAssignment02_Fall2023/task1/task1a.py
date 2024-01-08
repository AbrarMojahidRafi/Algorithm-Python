fileOpening = open("./input1a.txt", "r")

fileInList = fileOpening.readlines()     # fileInList = ['4 10\n', '1 3 5 7']

# work with 0 index
totalNumOfElement, sum = fileInList[0].split(" ")

totalNumOfElement = int(totalNumOfElement)
sum = int(sum)

# work with 1 index
l = fileInList[1].split(" ")      # l = ['1', '3', '5', '7']

newL = []       # newL = [1, 3, 5, 7]
for i in l:
    newL.append(int(i))

# output file creating...
outputFileCreating = open("Output1a.txt", "a")

# -------------------------------------------------
# main kaj shuru

for i in range(len(newL)):
    for j in range(len(newL)-1, i, -1):
        if newL[i] + newL[j] == sum:
            outputFileCreating.writelines(f"{i+1} {j+1}")

outputFileCreating.close()
