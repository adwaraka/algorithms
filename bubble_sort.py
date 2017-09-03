#5
#5 4 9 0 2
#0 2 4 5 9
def bubble_sort(ar):
    for j in reversed(xrange(0,len(ar))):
		for i in xrange(j):
			if (ar[i] > ar[i+1]):
				ar[i],ar[i+1] = ar[i+1],ar[i]
    for i in ar:
        print i,


N = int(raw_input())
arr = map(int, raw_input().split(" "))
bubble_sort(arr)