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

import heapq
from heapq import *
 
# Function to find the k'th largest element in a list using min-heap
def find_kth_largest(ints, k):
 
    # base case
    if not ints or len(ints) < k:
        exit(-1)
 
    # build a min-heap from the first `k` elements in the list
    minheap = []
    for i in range(k):
        heappush(minheap,ints[i])
 
    # do for remaining list elements
    for i in range(k, len(ints)):
        # if the current element is more than the root of the heap
        if ints[i] > minheap[0]:
            # replace root with the current element
            heapq.heapreplace(minheap, ints[i])
    
 
    # return the root of min-heap
    return minheap[0]
