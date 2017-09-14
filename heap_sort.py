def heapify(arr):
    if len(arr) == 1:
        return arr
    for i in xrange(len(arr)/2 - 1, -1, -1):
        try:
            if (arr[i] > arr[2*i + 1]):
                arr[i], arr[2*i + 1] = arr[2*i + 1], arr[i]
            if (arr[i] > arr[2*i + 2]):
                arr[i], arr[2*i + 2] = arr[2*i + 2], arr[i]
        except:
            pass
    arr[i], arr[len(arr)-1] = arr[len(arr)-1], arr[i]
    return arr

arr = [190, 19, -4, 10, 11, -8, 2, -200, 13]
l = len(arr)-1
final = []
while arr != []:
    heap = heapify(arr)
    final.extend(heap[l:])
    arr = heap[:l]
    l-=1
for i in final:
    print i,