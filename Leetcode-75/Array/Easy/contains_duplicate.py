# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Hashmap
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

# Using set and comparing sizes                
class Solution: 
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False
        else:
            return True
