'''
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
'''

class Solution:
  ## Approach 1 
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Remove duplicates
        list(set(nums))
        nums.sort(reverse=True)
        return nums[k-1]
    
    
    ### Apraoch 2 - Heap
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
      
## Implementing Heap

# find kth largest number in the array

from heapq import *
def kth_largest_number(arr,k):
    
    minheap = []
    for i in range(k):
        heappush(minheap, arr[i])
    
    for i in range(k,len(arr)):
        if arr[i] > minheap[0]:
            heappush(minheap,arr[i])
    
    return minheap[k-1]
    
print(kth_largest_number([1,2,3,4,5,6,9,10,13], 7))
