#to detect a rotation inside an otherwise sorted array
def rotation_search(arr, low, high):
    if (low < high):
        if arr[low] < arr[high]:
            mid = (low + high)//2
            if arr[low] < arr[mid]:
                return rotation_search(arr, mid, high)
            elif arr[mid] < arr[high]:
                return rotation_search(arr, low, mid)
        else:
            for i in xrange(low, high):
                if arr[i] < arr[i+1]:
                    i+=1
                else:
                    return i+1
    else:
        return -1


arr = ["alexander", "ethan", "fred", "matt", "obara", "yaxley", "arvind", "bob"]
alpha_num_arr = []
for i in arr:
    i = list(i)
    first_alpha_number = ord(i[0]) - ord('a')
    alpha_num_arr.append(first_alpha_number)

print alpha_num_arr
val = rotation_search(alpha_num_arr, 0, len(alpha_num_arr)-1)
print val
