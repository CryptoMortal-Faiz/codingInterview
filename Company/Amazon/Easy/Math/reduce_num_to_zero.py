# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

class Solution:
    def numberOfSteps(self, num: int) -> int:
        print(bin(num))
        binary = bin(num)[2:]
        print(binary)
        ones = binary.count("1")
        total = len(binary)
        return ones + total - 1
