class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        left, right = 0, 0
        count = Counter([ch for ch in s])
        n = len(s)
        res = []
        myset = set()
        while right < n:
            if s[right] not in myset:
                myset.add(s[right])
            count[s[right]] -= 1
            right += 1

            validSubstr = True
            for ch in myset:
                if count[ch] != 0:
                    validSubstr = False
                    break
            
            if validSubstr:
                res.append(right - left)
                left = right
                myset.clear()
            
        return res
                