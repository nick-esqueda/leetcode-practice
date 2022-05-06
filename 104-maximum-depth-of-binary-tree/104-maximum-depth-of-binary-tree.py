# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        """
        
        if not root: return 0
        
        d = 0
        q = [root]
        while q:
          d += 1
          l = len(q)
          
          for _ in range(l):
            curr = q.pop(0)
            if curr.left: q.append(curr.left)
            if curr.right: q.append(curr.right)
          
        return d
          
