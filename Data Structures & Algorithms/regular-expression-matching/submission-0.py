class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        cache = {}

        def solve(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            if j == m:
                return i == n

            first_match = i < n and (s[i] == p[j] or p[j] == '.')

            if j + 1 < m and p[j + 1] == '*':
                ans = solve(i, j + 2) or (first_match and solve(i + 1, j))
            else:
                ans = first_match and solve(i + 1, j + 1)

            cache[(i, j)] = ans
            return ans

        return solve(0, 0)