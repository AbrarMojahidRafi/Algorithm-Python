# graph = {
#   1 : [3, 4, 7],
#   3 : [2], 
#   2 : [5], 
#   5: [6], 
#   7 : [6]
# }

with open("./input2.txt", "r") as inputFileOpening:
  inputFile = inputFileOpening.readlines()
  
graph = {}
for i in inputFile[1::]:
  elements = i.split(" ")   # elements =  ["1","3"]
  # this conditions is for making an undirected graph. 
  if int(elements[0]) not in graph:
    graph[int(elements[0])] = [int(elements[1])]
    graph[int(elements[1])] = [int(elements[0])]
  else: 
    graph[int(elements[0])].append(int(elements[1]))
    if int(elements[1]) not in graph:
      graph[int(elements[1])] = [int(elements[0])]
    else: 
      graph[int(elements[1])].append(int(elements[0]))

queue = []
visited = [] 

def bfs(graph, root):
  
  queue.append(root)
  visited.append(root)
  
  for loopCounter in range(int(inputFile[0].split(" ")[0])):
    
    m = queue.pop(0) 
    
    with open("output2.txt", "a") as outputFile:
       outputFile.writelines(f"{m} ")
       
    if m in graph: 
      for i in graph[m]:
        if i not in visited: 
          queue.append(i)
          visited.append(i)

bfs(graph, 1)