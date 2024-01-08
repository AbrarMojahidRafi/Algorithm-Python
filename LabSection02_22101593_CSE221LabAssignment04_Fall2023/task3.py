with open("./input3.txt", "r") as inputFileOpening:
  inputFile = inputFileOpening.readlines()
  
graph = {}
for i in inputFile[1::]:
  elements = i.split(" ")
  if int(elements[0]) not in graph:
    graph[int(elements[0])] = [int(elements[1])]
    graph[int(elements[1])] = [int(elements[0])]
  else: 
    graph[int(elements[0])].append(int(elements[1]))
    if int(elements[1]) not in graph:
      graph[int(elements[1])] = [int(elements[0])]
    else: 
      graph[int(elements[1])].append(int(elements[0]))

# graph = {
#   1: [3, 4, 7],
#   3: [2], 
#   2: [5],
#   5: [6], 
#   7: [6]
#   }

visited = []
stack = []

def dfs(graph, startCity):
  
  visited.append(startCity)
  stack.append(startCity) 
  
  p = stack.pop(0) 
  
  with open("output3.txt", "a") as outputFile:
    outputFile.writelines(f"{p} ")
  
  if p in graph: 
    for j in graph[p]: 
      if j not in visited:
        dfs(graph, j)
    
dfs(graph, 1)
