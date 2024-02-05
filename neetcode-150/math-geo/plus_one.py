class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
      # Need Type Conversions
        s = [str(i) for i in digits]
        res = int("".join(s))
        res += 1
        result = []
        for i in str(res):
            result.append(int(i))
        return result

