# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = deque([root])

        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if node.val == subRoot.val and self.check(node, subRoot):
                    return True
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return False
    
    def check(self, p, q):
        if not p or not q:
            return p == q
        
        return p.val == q.val and self.check(p.left, q.left) and self.check(p.right, q.right)
