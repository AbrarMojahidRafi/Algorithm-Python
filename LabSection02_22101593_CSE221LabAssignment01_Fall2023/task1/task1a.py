def even_odd(num):
  if int(num)%2 == 0:
    return "Even"
  else:
    return "Odd"


file = open("./input1a.txt", "r")

line = file.readlines()

f = open("output1a.txt", "a")

T = line[0]

for i in range(int(T)):
  returnValue = even_odd(line[i+1])
  f.writelines(f"{int(line[i+1])} is an {returnValue} number.")
  f.writelines("\n")

f.close()

