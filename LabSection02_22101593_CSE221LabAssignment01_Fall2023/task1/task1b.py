def add(num1, num2):
  return num1 + num2

def sub(num1, num2):
  return num1 - num2

def mul(num1, num2):
  return num1 * num2

def divi(num1, num2):
  return (num1 / num2)


file = open("./input1b.txt", "r")

line = file.readlines()

f = open("output1b.txt", "a")

T = line[0]

for i in range(int(T)):
  calculate = line[i+1].split(" ")
  result = None
  operator = None
  if calculate[2] == "+":
    result = add(int(calculate[1]), int(calculate[3]))
    operator = calculate[2]
  elif calculate[2] == "-":
    result = sub(int(calculate[1]), int(calculate[3]))
    operator = calculate[2]
  elif calculate[2] == "*":
    result = mul(int(calculate[1]), int(calculate[3]))
    operator = calculate[2]
  elif calculate[2] == "/":
    result = divi(int(calculate[1]), int(calculate[3]))
    operator = calculate[2]
  f.writelines(f"The result of {int(calculate[1])} + {int(calculate[3])} is {result}")
  f.writelines("\n")

f.close()

