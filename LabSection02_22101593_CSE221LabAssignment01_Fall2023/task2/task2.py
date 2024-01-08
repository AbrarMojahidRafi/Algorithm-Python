inputFileOpenning = open("./input2_textCase1.txt", "r")
inputFile = inputFileOpenning.readlines()

dumnyArr = inputFile[1].split(" ") 
arr = [0]*len(dumnyArr)
for i in range(len(arr)):
  arr[i] = int(dumnyArr[i])
# print(arr)   # ------> [3, 2, 1, 4, 5] 

for i in range(len(arr)-1):
  flag = False
  for j in range(len(arr)-i-1):
    if arr[j] > arr[j+1]:
      arr[j], arr[j+1] = arr[j+1], arr[j]
      flag = True 
  if (flag == False):
    # print("inner loop works for the O(n) time complexity!")
    break 

outputFileCreating = open("output2.txt", "a")
outputFileCreating.writelines(f"{arr}")
outputFileCreating.close()

