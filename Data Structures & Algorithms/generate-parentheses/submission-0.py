class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(left, right, path):
            if left > right:
                return
            if left == 0 and right == 0:
                res.append("".join(path))
                return
            
            if left > 0:
                path.append("(")
                dfs(left - 1, right, path)
                path.pop()
            if left < right:
                path.append(")")
                dfs(left, right - 1, path)
                path.pop()
        dfs(n, n, [])
        return res

            