fileOpening = open("./input1b.txt", "r")

fileInList = fileOpening.readlines()     # fileInList = ['4 10\n', '1 3 5 7']
                                                 #          0          1 
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
outputFileCreating = open("Output1b.txt", "a")

# -------------------------------------------------

pointerIdx = 0
lastIdx = len(newL)-1
flag = False

for i in range(totalNumOfElement):
    # amra same position ke pointerIdx and lastIdx diye point krte parbo na....
    if pointerIdx != lastIdx:
        if newL[pointerIdx] + newL[lastIdx] == sum:
            outputFileCreating.writelines(f"{pointerIdx+1} {lastIdx+1}")
            flag = True
            break
        else:
            if newL[pointerIdx] + newL[lastIdx] < sum:
                pointerIdx += 1
            else:
                lastIdx -= 1

if flag == False:   # amar loop ta chole sesh hoye gelo, but kokhonoi ami emon duita num paini jader summation sum er soman hoy.....
    outputFileCreating.writelines("IMPOSSIBLE")

outputFileCreating.close()
