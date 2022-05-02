# find k largest numbers in the array

from heapq import *
def top_k_number(arr,k):
    
    minheap = []
    for i in range(k):
        heappush(minheap, arr[i])
    
    for i in range(k,len(arr)):
        if arr[i] > minheap[0]:
            heappop(minheap)
            heappush(minheap,arr[i])
    
    return minheap
    
print(top_k_number([1,2,3,4,5,6,7],3))
