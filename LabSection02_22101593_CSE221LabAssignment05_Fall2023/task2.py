with open("./input2.txt", "r") as inputFileOpening:
  inputFile = inputFileOpening.readlines()        # inputFile = ['5 3\n', '3 1\n', '1 2\n', '4 5']
  
graph = {}

# function of detect cycle in a directed graph
def isCyclic():
  for i in range(int(inputFile[0].split(" ")[1])): 
    edgePosition = i + 1
    A, B = map(int, inputFile[edgePosition].split(" "))
    # (A, B)
    # 3 1
    # 1 2
    # 4 5
    if A not in graph:
      graph[A] = [B]
    else: 
      graph[A].append(B)
    
    if B in graph:
      return True  # True means Cycle present
  return False   # False means Cycle is not present 

def topoRecursive(key): 
  visited[key] = True
  if key not in queue: 
    queue.append(key)
  neighbours = sorted(graph[key])      # for "lexicographical order" 
  for neighbour in neighbours: 
    if visited[neighbour] == False: 
      visited[neighbour] = True
      queue.append(neighbour)
  

N = int(inputFile[0].split(" ")[0])
visited = [False]*(N+1)
queue = []

def topologicalSort(graph): 
  for i in graph: 
    topoRecursive(i)
  return queue

if isCyclic(): 
  with open("output2.txt", "w") as outputFile: 
    outputFile.write("IMPOSSIBLE")
else: 
  topological_sorted_list = topologicalSort(graph) 
  
  s = ""
  for i in range(len(topological_sorted_list)):
    lastElement = topological_sorted_list.pop(0)
    s = s + str(lastElement) + " "
  with open("output2.txt", "w") as outputFile: 
    outputFile.write(s) 