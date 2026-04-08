class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        i = 0
        max_length = 0

        for j in range(len(s)):
            if s[j] in chars and chars[s[j]] >= i:
                i = chars[s[j]] + 1

            chars[s[j]] = j
            max_length = max(max_length, j - i + 1)

        return max_length