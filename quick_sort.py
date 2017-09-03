#Quicksort Algorithm
#5
#9 8 7 6 5
def partition(alist,first,last):
   pivotvalue = alist[first]
   i = first+1
   j = last
   while 1:
       while i <= j and alist[i] <= pivotvalue:
           i += 1
       while alist[j] >= pivotvalue and j >= i:
           j -= 1
       if j < i:
           break
       else:
           temp = alist[i]
           alist[i] = alist[j]
           alist[j] = temp
   temp = alist[first]
   alist[first] = alist[j]
   alist[j] = temp
   return j
   
def quick_sort(alist, first, last):
   if first < last:
       splitpoint = partition(alist, first, last)
       quick_sort(alist, first, splitpoint-1)
       quick_sort(alist, splitpoint+1, last)

m = input()
ar = [int(i) for i in raw_input().split()]
quick_sort(ar, 0, len(ar)-1)
for i in ar:
    print i,