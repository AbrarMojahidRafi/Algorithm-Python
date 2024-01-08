with open("input5.txt", "r") as inputFileOpening:
  inputFile = inputFileOpening.readlines()

N, M, D = inputFile[0].split(" ")
N = int(N)
M = int(M)
d = int(D)

graph = {}
for i in range(N + 1):
  graph[i] = []

for i in inputFile[1::]:
  elements = i.split(" ")
  graph[int(elements[0])].append(int(elements[1]))
  graph[int(elements[1])].append(int(elements[0]))

#############################################

def dfs(graph, start, end, visitedNode, path, shortestPath):
  
  visitedNode[start] = True
  path.append(start)

  if start != end:
    for neighbourNode in graph[start]:
      if not visitedNode[neighbourNode]:
        dfs(graph, neighbourNode, end, visitedNode, path, shortestPath)
  else:
    if len(path) < len(shortestPath):
      shortestPath[:] = path[:]

  path.pop()
  visitedNode[start] = False

def find_the_shortest_path(graph, start, end):
    visitedNode = {} 
    for eachNode in graph:
        visitedNode[eachNode] = False
    # {0: False, 1: False,...........}
    shortestPath = [] 
    dfs(graph, start, end, visitedNode, [], shortestPath)
    return shortestPath

#############################################

finalPath = find_the_shortest_path(graph, int(d), 1)

if len(finalPath) == 0:
  with open("output5.txt", "w") as outputFile:
    outputFile.write("IMPOSSIBLE")
else:
  with open("output5.txt", "w") as outputFile: 
    outputFile.write(f"Time: {str(len(finalPath) - 1)}\n")
    outputFile.write("Shortest Path: ")
    for i in range(len(finalPath) - 1, -1, -1):
      outputFile.write(f"{str(finalPath[i])} ")
      