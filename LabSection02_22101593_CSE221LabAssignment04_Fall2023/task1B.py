with open("./input1_B.txt", "r") as inputFileOpening: 
  inputFile = inputFileOpening.readlines() 
  # inputFile = ['4 3\n', '1 3 8\n', '3 2 5\n', '1 4 2'] 
  
vertices = int(inputFile[0].split(" ")[0])

adjacencyList = [0]*(vertices+1)

for i in inputFile[1:]:
  elements = i.split(" ")   # i = '1 3 8\n'    ->elements =  ["1","3","8\n"]
  if adjacencyList[int(elements[0])] == 0:
    adjacencyList[int(elements[0])] = [(int(elements[1]), int(elements[2]))]
  else: 
    adjacencyList[int(elements[0])].append((int(elements[1]), int(elements[2])))
# adjacencyList = [0, [(3, 8), (4, 2)], 0, [(2, 5)], 0] 

# generating the output
with open("output1_B.txt", "a") as outputFile:
  for i in range(len(adjacencyList)):
    if adjacencyList[i] == 0:
      outputFile.writelines(f"{i} : ") 
    else: 
      outputFile.writelines(f"{i} : ") 
      for eachTuple in adjacencyList[i]: 
        outputFile.writelines(f"{eachTuple} ") 
    outputFile.writelines("\n")