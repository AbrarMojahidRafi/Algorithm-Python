with open('input1_1.txt', 'r') as inputFileOpening:
  inputFile = inputFileOpening.readlines()

N = int(inputFile[0].split(" ")[0])
M = int(inputFile[0].split(" ")[1])

adjacencyList = {}
for i in range(1, len(inputFile)-1):
  node1, node2, edgeValue = map(int, inputFile[i].split(" ")) 
  if node1 not in adjacencyList:
    adjacencyList[node1] = {node2: edgeValue} 
  else: 
    adjacencyList[node1][node2] = edgeValue 

source = int(inputFile[-1])
# print(adjacencyList)

############################################
############################################

import heapq

def dijkstra_algo(graph, sourceElem):

  path = {}
  previousElem = {}

  for eachVertices in graph:
    path[eachVertices] = float('inf')
    previousElem[eachVertices] = None

  path[sourceElem] = 0

  pq = []
  heapq.heappush(pq, (path[sourceElem], sourceElem))

  while pq:
    minimumVertex = heapq.heappop(pq)[1]
    for eachNeighbour in graph[minimumVertex]:
      if path[minimumVertex] + graph[minimumVertex][eachNeighbour] < path[eachNeighbour]:
        previousElem[eachNeighbour] = minimumVertex
        path[eachNeighbour] = path[minimumVertex] + graph[minimumVertex][eachNeighbour]
        heapq.heappush(pq, (path[eachNeighbour], eachNeighbour))

  return path

############################################

ans = dijkstra_algo(adjacencyList, source)
with open('output1.txt', 'w') as outputFile: 
  for node in ans:
    if ans[node] == float('inf'):
      outputFile.writelines(str(-1) + ' ')
    else:
      outputFile.writelines(str(ans[node]) + ' ')

