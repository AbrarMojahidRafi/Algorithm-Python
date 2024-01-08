with open('input4_2.txt', 'r') as inputFileOpening: 
  inputFile = inputFileOpening.readlines()

N, M = map(int, inputFile[0].split(" "))

edgeList = []
weightList = []

for i in range(1, M+1):
    u, v, w = map(int, inputFile[i].split(" "))
    edgeList.append((u, v))
    weightList.append(w)

for i in range(M):
  for j in range(M - 1):
    if weightList[j + 1] < weightList[j]:
      weightList[j], weightList[j + 1] = weightList[j + 1], weightList[j]
      edgeList[j], edgeList[j + 1] = edgeList[j + 1], edgeList[j]

ranks = []
for i in range(N + 1): 
  ranks.append(i)
  
parent = []
for i in range(N + 1):
  parent.append(i)
  
def find(x):
    if x == parent[x]:
        return x
    return find(parent[x])

def union(x, y):
  
  X_root = find(x)
  Y_root = find(y)

  if X_root == Y_root:
    return

  if ranks[X_root] < ranks[Y_root]:
    parent[X_root] = Y_root

  elif ranks[X_root] > ranks[Y_root]:
    parent[Y_root] = X_root

  else:
    ranks[X_root] += 1
    parent[Y_root] = X_root
        
def kruskal_algorithm():
  emptyList = []
  i = 0
  e = 0

  while e < N- 1:
    u, v = edgeList[i]
    i += 1
    x = find(u)
    y = find(v)

    if x != y:
      emptyList.append((u, v))
      union(x, y)
      e += 1
      
  return emptyList


emptyList = kruskal_algorithm()

ans = 0
for u, v in emptyList:
    ans = ans + weightList[edgeList.index((u, v))]
with open('output4.txt', 'w') as outputFile: 
  outputFile.writelines(f"{ans}")
