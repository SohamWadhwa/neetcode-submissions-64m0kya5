# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def solve(root, level):
            if not root:
                return None
            
            if len(res) < level:
                res.append(root.val)
            
            solve(root.right, level + 1)
            solve(root.left, level + 1)
        
        solve(root, 1)
        return res