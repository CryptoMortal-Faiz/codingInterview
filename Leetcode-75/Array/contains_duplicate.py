# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        occurence = dict()
        initial = 1
        if len(nums) == 1:
            return False
        for i in nums:
            if i in occurence.keys():
                return True
            else:
                occurence[i] = initial
