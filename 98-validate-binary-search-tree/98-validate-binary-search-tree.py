# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        from the bottom, if each node's left is lesser and right is greater, that node is a BST
        if the left and right nodes are BSTs, and this node is a BST, everything is a BST
        """
        values = []
        
        def isValid(root):
          if not root:
            return True

          left = isValid(root.left)
          
          values.append(root.val)
          if values[-1] != max(values) or len(set(values)) != len(values):
            return False
          
          right = isValid(root.right)

          return left and right
        
        return isValid(root)