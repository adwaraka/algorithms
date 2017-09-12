#5
#2
#0 2 4 5 9
def binary_search(arr, low, high, n):
    if (low <= high):
        mid = (low + high)/2
        if arr[mid] == n:
            return mid
        elif (arr[mid] > n):
            return binary_search(arr, low, mid-1, n)
        elif (arr[mid] < n):
            return binary_search(arr, mid+1, high, n)
    else:
        return -1
		
N = int(raw_input())
n = int(raw_input())
arr = map(int, raw_input().split(" "))
val = binary_search(arr, 0, len(arr), n)
print val