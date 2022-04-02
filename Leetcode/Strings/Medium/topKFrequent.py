'''
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.
'''

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        
        first_K = count.most_common(k)
        
        res = []
        for i,j in first_K:
            res.append(i)
                   
        return res
