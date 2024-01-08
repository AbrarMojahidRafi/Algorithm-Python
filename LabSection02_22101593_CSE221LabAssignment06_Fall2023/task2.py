with open('input2_1.txt', 'r') as inputFileOpening:
  inputFile = inputFileOpening.readlines()

N = int(inputFile[0].split(" ")[0])
M = int(inputFile[0].split(" ")[1])

adjacencyList = {}
for i in range(1, N + 1):
    adjacencyList[i] = {}

for i in range(1, len(inputFile)-1):
  node1, node2, edgeValue = map(int, inputFile[i].split(" ")) 
  if node1 not in adjacencyList:
    adjacencyList[node1] = {node2: edgeValue} 
  else: 
    adjacencyList[node1][node2] = edgeValue 
# print(adjacencyList)   # {1: {2: 1}, 2: {3: 2}, 3: {}, 4: {3: 5}}
source_1 = int(inputFile[-1].split(" ")[0])
source_2 = int(inputFile[-1].split(" ")[1])

############################################

# Dijkstra's algorithm that return all the element of the shortest path tree
# if we cant find the path to the vertex, the distance is -1
# import heapq and store the vertices in a min heap

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

alicePath = dijkstra_algo(adjacencyList, source_1)
bobPath = dijkstra_algo(adjacencyList, source_2)

############################################

minTime = float('inf')
flag = False
minVertex = None

for node in alicePath:
    if node in bobPath:
        if minTime > max(alicePath[node], bobPath[node]):
            flag = True
            minVertex = node
            minTime = max(alicePath[node], bobPath[node])
            
with open('output2.txt', 'w') as outputFile: 
    if flag == False:
        outputFile.write("Impossible")
    else:
        outputFile.write("Time " + str(minTime))
        outputFile.write("\n")
        outputFile.write("Node " + str(minVertex))
