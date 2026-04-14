# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxVal):
            if not root:
                return 0
            
            count = 1 if root.val >= maxVal else 0
            count += dfs(root.left, max(maxVal, root.val))
            count += dfs(root.right, max(maxVal, root.val))

            return count
        return dfs(root, root.val)