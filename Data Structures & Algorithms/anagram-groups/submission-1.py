class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs.sort()
        vis = [False] * len(strs)
        res = []
        for i in range(len(strs)):
            if vis[i]:
                continue
            row = [strs[i]]
            vis[i] = True
            for j in range(i + 1, len(strs)):
                if not vis[j] and self.isAnagram(strs[i], strs[j]):
                    row.append(strs[j])
                    vis[j] = True
            res.append(row)
        return res
    
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