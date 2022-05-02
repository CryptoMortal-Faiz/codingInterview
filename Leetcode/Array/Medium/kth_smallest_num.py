# find kth smallest number in the array

from heapq import *
def k_smallest_number(arr,k):
    
    maxheap = []
    for i in range(k):
        heappush(maxheap, -arr[i])
    
    for i in range(k,len(arr)):
        if -arr[i] > maxheap[0]:
            heappop(maxheap)
            heappush(maxheap,-arr[i])
    
    return -maxheap[0]
    
print(k_smallest_number([1, 5, 12, 2, 11, 5], 4))
