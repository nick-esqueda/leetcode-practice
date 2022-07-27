# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder = []
        sta = []
        cur = root
        while sta or cur:
            if cur:
                sta.append(cur)
                cur = cur.left
            else:
                cur = sta.pop()
                inorder.append(cur.val)
                cur = cur.right
        return inorder
            
        
    def inorderTraversal_RECURSIVE(self, root: Optional[TreeNode]) -> List[int]:
        inorder = []
        def dfs(root):
            if root is None:
                return None
            dfs(root.left)
            inorder.append(root.val)
            dfs(root.right)
            return
        
        dfs(root)
        return inorder