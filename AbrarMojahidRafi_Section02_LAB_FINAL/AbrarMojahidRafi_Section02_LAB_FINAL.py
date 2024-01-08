with open("./AbrarMojahidRafi_Section02_LAB_FINAL.txt", "r") as inputFileOpening: 
  inputFile = inputFileOpening.readlines()
  
# print(inputFile)    # inputFile = ['a d 2\n', 'a c 1\n', 'c e 9\n', 'b c 1\n', 'b f 2\n', 'd i 4\n', 'd g 3\n', 'e h 2\n', 'f h 13\n', 'f k 4\n', 'i g 1\n', 'g e 4\n', 'g j 7\n', 'j i 8\n', 'j h 1\n', 'k h 8\n', 'k j 2\n'] 

graph = {}
totalNodes = []
for edge in inputFile: 
  elements = edge.split(" ")   # elements = ["a", ("d", "2\n")]
  if elements[0] not in totalNodes:
    totalNodes.append(elements[0])
  if elements[1] not in totalNodes:
    totalNodes.append(elements[1])
  
  if elements[0] not in graph: 
    graph[elements[0]] = [(elements[1], int(elements[2]))]
  else: 
    graph[elements[0]].append((elements[1], int(elements[2])))

# print(totalNodes, len(totalNodes))     # totalNodes = ['a', 'd', 'c', 'e', 'b', 'f', 'i', 'g', 'h', 'k', 'j'] 11

# print(graph)   # graph = {'a': [('d', 2), ('c', 1)], 'c': [('e', 9)], 'b': [('c', 1), ('f', 2)], 'd': [('i', 4), ('g', 3)], 'e': [('h', 2)], 'f': [('h', 13), ('k', 4)], 'i': [('g', 1)], 'g': [('e', 4), ('j', 7)], 'j': [('i', 8), ('h', 1)], 'k': [('h', 8), ('j', 2)]} 

# Q3: 

with open("Q3.txt", "r") as inputFile_Q3: 
  inputFile_Q3 = inputFile_Q3.readlines()

# print(inputFile_Q3)   # inputFile_Q3 = ['11 17\n', 'a*d*2\n', 'a*c*1\n', 'd*i*4\n', 'd*g*3\n', 'c*e*9\n', 'b*c*1\n', 'b*f*2\n', 'e*h*2\n', 'i*g*1\n', 'g*e*4\n', 'g*j*7\n', 'f*h*13\n', 'f*k*4\n', 'k*h*8\n', 'k*j*2\n', 'j*h*1\n', 'j*i*8\n', 'a b h\n'] 

graph_Q3 = {}
for i in range(1, len(inputFile_Q3)-1):
  edge = inputFile_Q3[i]
  elements = edge.split("*")
  if elements[0] not in graph_Q3: 
    graph_Q3[elements[0]] = [(elements[1], int(elements[2]))]
  else: 
    graph_Q3[elements[0]].append((elements[1], int(elements[2])))
# print(graph_Q3)
def FindTravelTime():
  stewie_start = inputFile_Q3[len(inputFile_Q3)-1].split(" ")[0]
  brain_start = inputFile_Q3[len(inputFile_Q3)-1].split(" ")[1] 
  destination = inputFile_Q3[len(inputFile_Q3)-1].split(" ")[2]
  
  distance_stewie = 0
  count_time_stewie = 0
  visited = []
  for i in range(int(inputFile_Q3[0].split(" ")[0])):
    if stewie_start != destination:
      break
    if stewie_start in graph_Q3: 
      # finging the lowest edge value, my neigh
      distance = [] 
      for i in graph_Q3[stewie_start]:
        distance.append(int(i[1]))
      # print(distance) 
      distance.sort()
      # print(distance) 
      
      for i in graph_Q3[stewie_start]: 
        if distance[0] == int(i[1]): 
          # print(i)
          distance_stewie += distance[0] 
          visited.append(stewie_start)
          stewie_start = i[0]
          count_time_stewie += 1
    
  with open("ansQ3.txt", "w") as outputFile: 
    outputFile.writelines(f"{distance_stewie}")

FindTravelTime()

