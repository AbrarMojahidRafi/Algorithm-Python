inputFileOpening = open("./input3.txt", "r")

inputFile = inputFileOpening.readlines()    # inputFile = ['5\n', '1 2 3 4 5']

l = inputFile[1].split(" ")

newList = []     # newList = [1, 2, 3, 4, 5]
for i in l:
    newList.append(int(i))

# O(n)
count = 0
pointer1 = 0
pointer2 = pointer1 + 1

while (pointer1 < len(newList)-2):

    if pointer2 >= len(newList):
        pointer1 += 1
        pointer2 = pointer1 + 1

    if newList[pointer1] > newList[pointer2]:
        count += 1
    pointer2 += 1

# output file creating
outputFile = open("Output3.txt", "a")
outputFile.writelines(f"{count}")
outputFile.close()
