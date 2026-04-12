# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        
        l = 0
        if root.left:
            l = self.maxDepth(root.left)
        r = 0
        if root.right:
            r = self.maxDepth(root.right)

        return 1 + max(l, r)