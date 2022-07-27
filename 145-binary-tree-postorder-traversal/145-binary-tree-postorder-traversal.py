# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        """
        if not root:
            return None
        
        post = []
        sta = [root]
        while sta:
            cur = sta.pop()
            post.append(cur.val)
            if cur.left:
                sta.append(cur.left)
            if cur.right:
                sta.append(cur.right)
        
        return post[::-1]
    
    
    def postorderTraversal_RECURSIVE(self, root: Optional[TreeNode]) -> List[int]:
        post = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            post.append(root.val)
            
        dfs(root)
        return post