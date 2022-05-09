# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        if node is null, return
        if p is less than or equal to root and q is greater than or equal to root, return node
        """
        
        if not root:
          return
        
        if p.val <= root.val <= q.val:
          return root
        elif q.val <= root.val <= p.val:
          return root
        
        elif p.val <= root.val and q.val <= root.val:
          return self.lowestCommonAncestor(root.left, p, q)
        
        elif p.val >= root.val and q.val >= root.val:
          return self.lowestCommonAncestor(root.right, p, q)
        