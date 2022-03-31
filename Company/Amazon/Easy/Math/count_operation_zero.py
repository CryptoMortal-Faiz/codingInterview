# https://leetcode.com/problems/count-operations-to-obtain-zero/

# Count toatal operation until to reach 0 (Zero)

class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        res = 0
    
        while num1 and num2:
            print(num1,num2)
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            res += 1
    
        return res
