inputFileOpening = open("./input4.txt", "r")

inputFile = inputFileOpening.readlines()    # inputFile = ['8\n', '5 10 4 -3 1 6 -10 2']

l = inputFile[1].split(" ")

newList = []     # newList = [5, 10, 4, -3, 1, 6, -10, 2]
for i in l:
    newList.append(int(i))

# O(n)
sum = 0
pointer1 = 0
pointer2 = pointer1 + 1

while (pointer1 < len(newList)-2):

    if pointer2 >= len(newList):
        pointer1 += 1
        pointer2 = pointer1 + 1

    if (newList[pointer1] + newList[pointer2]**2) > sum:
        sum = newList[pointer1] + newList[pointer2]**2
    pointer2 += 1

# output file creating
outputFile = open("Output4.txt", "a")
outputFile.writelines(f"{sum}")
outputFile.close()
