# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        """
        left = []
        def left_pre(root):
            if root is None:
                left.append('n')
                return
            left.append(root.val)
            left_pre(root.left)
            left_pre(root.right)
        
        right = []
        def right_pre(root):
            if root is None:
                right.append('n')
                return
            right.append(root.val)
            right_pre(root.right)
            right_pre(root.left)
        
        left_pre(root.left)
        right_pre(root.right)
        return left == right