# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, cur_sum):
            if not root:
                return False
            if not root.left and not root.right:
                return targetSum == cur_sum + root.val
            
            if (dfs(root.left, cur_sum + root.val) or
                dfs(root.right, cur_sum + root.val)):
                return True
            
            return False
        
        return dfs(root, 0)
        