# Openning the input file
inputFileOpenning = open("./input3_textCase1.txt", "r")
inputFile = inputFileOpenning.readlines()

# doing string to int of an array


def stringToIntegerConverterOfAnArray(dumnyArr):
    arr = [0]*len(dumnyArr)
    for i in range(len(arr)):
        arr[i] = int(dumnyArr[i])
    return arr


id = stringToIntegerConverterOfAnArray(inputFile[1].split(" "))
marks = stringToIntegerConverterOfAnArray(inputFile[2].split(" "))

print("Before sorting", id)
print("Before sorting", marks)

# perform selection sort in the marks along with the id.
i = 0
while (i < len(marks)):

    pointer = marks[i]
    selectedIndex = i

    for j in range(i+1, len(marks)):
        if marks[j] > pointer:
            selectedIndex = j
            pointer = marks[j]
    temp = marks[i]
    marks[i] = marks[selectedIndex]
    marks[selectedIndex] = temp

    temp = id[i]
    id[i] = id[selectedIndex]
    id[selectedIndex] = temp

    i += 1

# now creating dictionary for sorted id
dictionary = {}

for i in range(len(id)):
    if marks[i] not in dictionary:
        dictionary[marks[i]] = f"{id[i]}"
    else:
        for index in range(-1, -(len(dictionary[marks[i]]))-1, -1):
            if f"{id[i]}" not in dictionary[marks[i]]:
                if int(dictionary[marks[i]][index]) < id[i]:
                    dictionary[marks[i]] = dictionary[marks[i]] + f"{id[i]}"
                else:
                    dictionary[marks[i]] = f"{id[i]}" + dictionary[marks[i]]

print(dictionary)
print("after sorting", marks)
print("after sorting", id)

# write the output in a text file
outputFile = open("output3.txt", "a")

for k, v in dictionary.items():
    for value in v:
        outputFile.writelines(f"ID: {value} Mark: {k}\n")
        # print(f"ID: {value} Mark: {k}")
outputFile.close()
