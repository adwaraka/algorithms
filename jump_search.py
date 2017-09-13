#jump search
def jump_search(arr, n, step_size):
    low, high = 0, step_size
    while low < len(arr):
        if arr[high] < n:
            low = high + 1
            high = min(low + step_size, len(arr)-1)
        else:
            for i in xrange(low, high+1):
                if n == arr[i]:
                    return True, i+1
            return False, -1
    return False, -1

n = 10
arr = [0,2,4,5,9,10,18,19,20,25]
val, index = jump_search(arr, n, 3)
print val, index