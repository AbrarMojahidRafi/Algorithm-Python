inputFileOpen = open("./input2b.txt", "r")

# inputFile = ['4\n', '1 3 5 7\n', '4\n', '2 2 4 8']
inputFile = inputFileOpen.readlines()

# making list1
l1 = inputFile[1].split(" ")    # l1 = ['1', '3', '5', '7\n']

list1 = []        # list1 = [1, 3, 5, 7]
for i in l1:
    list1.append(int(i))

# making list2
l2 = inputFile[3].split(" ")

list2 = []        # list2 = [2, 2, 4, 8]
for i in l2:
    list2.append(int(i))

# O(n)
def OrderOfN(list1, list2):
  newL = []
  p1 = p2 = 0
  while p1 < len(list1) and p2 < len(list2):
    if list1[p1] > list2[p2]: 
      newL.append(list2[p2])
      p2 += 1 
    else: 
      newL.append(list1[p1])
      p1 += 1
  
  if p1 < len(list1): 
    newL.extend(list1[p1::])
  
  if p2 < len(list2): 
    newL.extend(list2[p2::])
  return newL
  
sortedList = OrderOfN(list1, list2)

# Generating the output
s = ""
for i in sortedList:
    s = s + str(i) + " "

outputFileCreating = open("output2b.txt", "a")
outputFileCreating.writelines(s)
outputFileCreating.close()
