def insertion_sort(ar):
    for i in range(1,len(ar)):
        j = i
        while j > 0 and ar[j] < ar[j-1]:
            ar[j], ar[j-1] = ar[j-1], ar[j]
            j=j-1
    for i in ar:
        print i,


N = int(raw_input())
arr = map(int, raw_input().split(" "))
insertion_sort(arr)
