# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    def serialize(self, root: Optional[TreeNode]) -> str:
        arr = []
        def dfs(root):
            nonlocal arr
            if not root:
                arr.append("N")
                return
                
            arr.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(arr)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = data.split(",")

        i = 0
        def dfs():
            nonlocal i
            if arr[i] == 'N':
                i += 1
                return None
            node = TreeNode(int(arr[i]))
            i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()
