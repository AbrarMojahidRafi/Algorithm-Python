# [2, 6, 9, 15, 54, 68, 100, 125, 128, 324]

def binarySearch(arr, first, last, findValue):
    left = first
    right = last
    while (left < right):
        mid = (left + right) // 2
        if arr[mid] == findValue:
            return True
        elif arr[mid] < findValue:
            left = mid + 1
        elif arr[mid] > findValue:
            right = mid - 1
    return False


arr = [2, 6, 9, 15, 54, 68, 100, 125, 128, 324]
print(binarySearch(arr, 0, len(arr)-1, 9))
