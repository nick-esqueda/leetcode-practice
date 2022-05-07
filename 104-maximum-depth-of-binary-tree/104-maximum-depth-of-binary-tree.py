# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         """
#         BFT
#         """
#         if not root: return 0
        
#         d = 0
#         q = [root]
#         while q:
#           d += 1
#           l = len(q)
          
#           for _ in range(l):
#             curr = q.pop(0)
#             if curr.left: q.append(curr.left)
#             if curr.right: q.append(curr.right)
          
#         return d
          
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         """
#         DFT
#               3
#             9   20
#            1 4    10
#               5
#              2 6
        
        
#         sta = []
#         depth = 5
#         curr = 2
#         len = 0
#         while...
        
          
#         return x
#         """
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
      """
      if the root is none, return 0
      otherwise...
      take the max of the left tree and the right tree
      return the max + 1 (for this frame) to the caller
      """
      
      if not root:
        return 0
      
      return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1