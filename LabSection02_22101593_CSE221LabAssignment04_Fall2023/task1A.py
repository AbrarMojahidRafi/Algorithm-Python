with open("./input1_A.txt", "r") as inputFileOpening: 
  inputFile = inputFileOpening.readlines() 
  # inputFile = ['4 3\n', '1 3 8\n', '3 2 5\n', '1 4 2'] 

vertices = int(inputFile[0].split(" ")[0])

adjacencyMatrix = []      # adjacencyMatrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
for i in range(vertices + 1):
  l = [0]*(vertices + 1)   # l = [0, 0, 0, 0, 0]
  adjacencyMatrix.append(l)

for i in inputFile[1:]:
  elements = i.split(" ")    # i = '1 3 8\n'    ->elements =  ["1","3","8\n"]
  adjacencyMatrix[int(elements[0])][int(elements[1])] = int(elements[2])

# generating the output
with open("output1_A.txt", "a") as outputFile:
  for i in range(len(adjacencyMatrix)): 
    for j in range(len(adjacencyMatrix[i])): 
      outputFile.writelines(f"{adjacencyMatrix[i][j]} ")
    outputFile.writelines("\n")