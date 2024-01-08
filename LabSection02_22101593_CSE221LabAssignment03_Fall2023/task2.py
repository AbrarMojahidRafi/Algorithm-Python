inputFileOpening = open("./input2.txt", "r")

inputFile = inputFileOpening.readlines()    # inputFile = ['8\n', '1 7 13 4 5 7 13 12']

l = inputFile[1].split(" ")

newList = []     # newList = [1, 7, 13, 4, 5, 7, 13, 12]
for i in l:
    newList.append(int(i))

# work with the DIVIDE AND CONQUERE concept

def divide(arr): 
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        a1 = divide(arr[:mid])  # write the parameter
        a2 = divide(arr[mid:])  # write the parameter
        return conquere(a1, a2)          # complete the merge function above 

def conquere(a1, a2):
    if a1[0] < a2[0]:
        return a2
    else: 
        return a1 
    
maxValue = divide(newList)

# output file creating
outputFile = open("Output2.txt", "a")
outputFile.writelines(f"{maxValue[0]}")
outputFile.close()