class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def isValid(x, y, board):
            d1 = y - 1
            d2 = y + 1
            for r in range(x-1, -1, -1):
                if board[r][y] == 'Q':
                    return False
                if 0 <= d1 and board[r][d1] == 'Q':
                    return False
                if d2 < n and board[r][d2] == "Q":
                    return False
                d1 -= 1
                d2 += 1
            return True
        
        def dfs(r, board):
            if r == n:
                res.append(["".join(board[i]) for i in range(n)])
                return
            
            for c in range(n):
                if isValid(r, c, board):
                    board[r][c] = 'Q'
                    dfs(r + 1, board)
                    board[r][c] = '.'
        
        dfs(0, [['.'] * n for _ in range(n)])
        return res