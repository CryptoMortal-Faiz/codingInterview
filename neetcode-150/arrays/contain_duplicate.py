class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        if len(set(nums)) == len(nums):
            return False
        return True
    
    # Using Dictionary
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        nums_dict = {}
        for i in nums:
            if i in nums_dict:
                return True
            else:
                nums_dict[i] = 1
