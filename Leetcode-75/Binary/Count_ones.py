#Count 1's


# Example 1:

# Input: n = 00000000000000000000000000001011
# Output: 3
# Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

class Solution:
    def hammingWeight(self, n: int) -> int:
        
        count = Counter(bin(n)[2:])
        return count["1"]
      
