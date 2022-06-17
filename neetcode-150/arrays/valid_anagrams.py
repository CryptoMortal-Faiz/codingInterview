class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = 0
        if len(set(s)) != len(set(t)):
            return False
        for i in s:
            if i in t:
                count += 1
        
        return len(s) == count
