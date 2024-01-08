input_file = open("input3.txt", "r")
output_file = open("output3.txt", "w")

N, M = input_file.readline().split()
N, M = int(N), int(M)

graph = {}

for i in range(1, N + 1):
  graph[i] = []
for i in range(M):
  n_1, n_2 = input_file.readline().split() 
  n_1, n_2 = int(n_1), int(n_2)
  graph[n_1].append(n_2)

###########################################################

def DFS(node, vertex, visited, topologicalOrder):
  visited[vertex] = True
  for neighbor in node[vertex]:
    if not visited[neighbor]:
      DFS(node, neighbor, visited, topologicalOrder)
  topologicalOrder.append(vertex)
  return topologicalOrder

###########################################################

def transpose(node):
  new_form = {}
  for vertex in node:
    new_form[vertex] = []
  for vertex in node:
    for n in node[vertex]:
      new_form[n].append(vertex)
  return new_form

###########################################################

def strongly_connected_component(graph, topological_order, transposed_node):
  visited = {vertex: False for vertex in graph}
  ans = []
  while topological_order:
    node = topological_order.pop()
    if not visited[node]:
      components = []
      DFS(transposed_node, node, visited, components)
      ans.append(components)
  for node in graph:
    if not visited[node]:
      components = []
      DFS(transposed_node, node, visited, components)
      ans.append(components)
          
  return ans

###########################################################

transposed_graph = transpose(graph)

stack = []

visited = {vertex: False for vertex in graph}
# {0: False, 1: False}

serial = DFS(graph, 1, visited, stack)

strongly_connected_components = strongly_connected_component(graph, serial, transposed_graph)

########################################################### 
# [[1,2,3],[4],[5],[7,8]]
for i in range(len(strongly_connected_components)):
  for j in range(len(strongly_connected_components[i])):
    strongly_connected_components[i][j] = str(strongly_connected_components[i][j])
    output_file.write(strongly_connected_components[i][j] + " ")
  output_file.write("\n")
