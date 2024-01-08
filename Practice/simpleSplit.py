fileInput = open("./simpleSplit.txt", "r")

fileInput = fileInput.readlines()       # ['0:15 - directed graph\n', '0:34 - undirected graph\n', '0:40 - adjacent vertices\n', '1:03 - degree of a vertex\n', '2:11 - path bw two vertices\n', '3:00 - connected vs disconnected graph\n', '3:45 - connected components\n', '4:20 - cycles in a graph\n', '4:51 - cyclic vs acyclic graph\n', '5:38 - tree\n', '6:16 - DAG\n', '6:43 - complete graph\n', '7:45 - weighted graph']

finalList = []

for i in fileInput:
    l = i.split(" - ")
    finalList.append(l[1])

for i in finalList:
    print(i)
