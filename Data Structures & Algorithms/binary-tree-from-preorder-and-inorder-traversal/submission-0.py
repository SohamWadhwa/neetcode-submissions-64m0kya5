# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inMap = {val: i for i, val in enumerate(inorder)}
        idx = 0

        def dfs(start, end):
            nonlocal idx
            if start > end:
                return None

            root_val = preorder[idx]
            idx += 1

            root = TreeNode(root_val)
            mid = inMap[root_val]

            root.left = dfs(start, mid - 1)
            root.right = dfs(mid + 1, end)

            return root

        return dfs(0, len(inorder) - 1)