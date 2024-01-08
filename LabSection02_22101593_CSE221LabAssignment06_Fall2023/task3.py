with open('input3_2.txt', 'r') as inputFileOpening: 
  inputFile = inputFileOpening.readlines()
  
###############################################

people_num = int(inputFile[0].split(" ")[0])
tasks_num = int(inputFile[0].split(" ")[1])

queries = []
for i in range(1, tasks_num+1): 
  p1, p2 = map(int, inputFile[i].split())
  queries.append([p1, p2])
# print(queries)

###############################################

size_list = [1] * (people_num + 1)
parent_list = [None] * (people_num + 1)

def find_function(x):
    if parent_list[x] == x:
        return x
    else:
        return find_function(parent_list[x])

def union_function(x, y):
    x = find_function(x)
    y = find_function(y)
    if x != y:
        parent_list[y] = x
        size_list[x] += size_list[y]

def making_set(x):
    parent_list[x] = x

for i in range(people_num + 1):
    making_set(i)

with open('output3.txt', 'w') as outputFile: 
  for i in range(tasks_num):
      union_function(queries[i][0], queries[i][1])
      outputFile.writelines(str(size_list[find_function(queries[i][0])]))
      outputFile.writelines('\n')
