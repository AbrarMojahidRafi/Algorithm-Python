with open("./input4.txt", "r") as inputFileOpening:
  inputFile = inputFileOpening.readlines()

vertices = int(inputFile[0].split(" ")[0])

graph = {}
for i in range(vertices+1):
  graph[i] = []

for i in inputFile[1::]:
  elements = i.split(" ")
  graph[int(elements[0])].append(int(elements[1]))
  
# graph = {0: [], 1: [4], 2: [], 3: [1, 2], 4: [3]}

outputFile = open('output4.txt', 'w')

def dfs(vertices):
  
    visited.append(vertices)
    path.append(vertices)
    
    for neighbor in graph[vertices]:
      if neighbor in path:
        return True  # Cycle found

      if neighbor not in visited:
        if dfs(neighbor):
          return True  # Cycle found

    # If we have reached here, then there is no cycle in the path from vertices to any of its descendants.

    path.remove(vertices)
    return False


visited = []
path = []

def hasCycle(graph):
  for vertices in graph:
    if vertices not in visited:
      if dfs(vertices):
        return True  # Cycle found
  return False  # No cycle found

result = hasCycle(graph)
if result:
    outputFile.writelines("YES")
else:
    outputFile.writelines("NO")