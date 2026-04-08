class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1
        for ch in t:
            idx = ord(ch) - ord('a')
            count[idx] -= 1
            if count[idx] < 0:
                return False
        
        return True