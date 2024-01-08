# [2, 6, 9, 15, 54, 68, 100, 125, 128, 324]

def ternarySearch(arr, first, last, findValue):
  left = first
  right = last - 1
  while (left <= right):
    mid1 = (left - right) // 3
    mid2 = right - mid1
    if arr[mid1] == findValue:
      return True
    elif arr[mid2] == findValue:
      return True
    
    if arr[mid2] < findValue:
      left = mid2 + 1
    elif arr[mid1] < findValue < arr[mid2]:
      left = mid1 + 1
      right = mid2 - 1
    elif arr[mid1] > findValue:
      right = mid1 - 1
  return False


arr = [2, 6, 9, 15, 54, 68, 100, 125, 128, 324]
print(ternarySearch(arr, 0, len(arr), 101))
