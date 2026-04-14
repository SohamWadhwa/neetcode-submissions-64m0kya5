# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        st = []
        ptr = root
        while ptr != None or st:
            while ptr:
                st.append(ptr)
                ptr = ptr.left
            
            ptr = st.pop()
            k -= 1
            if k == 0:
                return ptr.val
            
            ptr = ptr.right