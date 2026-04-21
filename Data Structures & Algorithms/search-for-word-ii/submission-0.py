class Trie:

    def __init__(self):
        self.children = {}
        self.end= False

    def insert(self, word: str) -> None:
        curr = self
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Trie()
            curr = curr.children[ch]
        
        curr.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()

        for word in words:
            root.insert(word)

        n, m = len(board), len(board[0])
        res, vis = set(), set()
        def dfs(r, c, node, curr_word):
            if r < 0 or c < 0 or r >= n or c >= m or (r, c) in vis or board[r][c] not in node.children:
                return 
            
            vis.add((r, c))
            node = node.children[board[r][c]]
            curr_word.append(board[r][c])
            if node.end:
                res.add("".join(curr_word))
            
            dfs(r + 1, c, node, curr_word)
            dfs(r - 1, c, node, curr_word)
            dfs(r, c + 1, node, curr_word)
            dfs(r, c - 1, node, curr_word)
            vis.remove((r, c))
            curr_word.pop()
        
        for r in range(n):
            for c in range(m):
                dfs(r, c, root, [])
        
        return list(res)