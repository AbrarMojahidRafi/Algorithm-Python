with open("./input6.txt", "r") as inputFileOpening:
  inputFile = inputFileOpening.readlines()

R, H = map(int, inputFile[0].split(" "))

grid = []
for i in inputFile[1::]:  # i = '..D\n', 'D..\n', '.D.\n', '##.'
  eachRow = i.strip("\n")
  grid.append(eachRow)
  
# grid = ['..D', 'D..', '.D.', '##.']

############################

def dfs(grid, r, c, visitedList):
    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == '#' or visitedList[r][c]:
        return 0
      
    visitedList[r][c] = True
    diamonds = 0
    if grid[r][c] == 'D':
        diamonds = 1
    diamonds += dfs(grid, r - 1, c, visitedList)
    diamonds += dfs(grid, r + 1, c, visitedList)
    diamonds += dfs(grid, r, c - 1, visitedList)
    diamonds += dfs(grid, r, c + 1, visitedList)

    return diamonds
  
def findMaximumAmountOfDiamonds(grid):
  rows = len(grid)
  columns = len(grid[0])
  for r in range(rows):
    for c in range(columns):
      if grid[r][c] == '.':
        visitedList = []
        for i in range(rows):
          visitedList.append([False]*columns)
        maxNumOfDiamonds = dfs(grid, r, c, visitedList)
  return maxNumOfDiamonds

###################### 

with open("output6.txt", "w") as outputFile:
  outputFile.write(f"{findMaximumAmountOfDiamonds(grid)}")