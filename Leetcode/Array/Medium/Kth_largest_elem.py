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
