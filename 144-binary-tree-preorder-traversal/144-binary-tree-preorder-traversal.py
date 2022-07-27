# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        pre = []
        sta = []
        cur = root
        while sta or cur:
            if cur:
                pre.append(cur.val)
                sta.append(cur)
                cur = cur.left
            else:
                cur = sta.pop()
                cur = cur.right
        return pre
        
    
    def preorderTraversal_RECURSIVE(self, root: Optional[TreeNode]) -> List[int]:
        pre = []
        def dfs(root):
            if not root:
                return
            pre.append(root.val)
            dfs(root.left)
            dfs(root.right)
    
        dfs(root)
        return pre