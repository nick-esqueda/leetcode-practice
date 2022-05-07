# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         """
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
          
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
              3
            9   20
           1 4    10
              5
             2 6
        
        
        sta = []
        depth = 5
        curr = 2
        len = 0
        while...
          increment depth
          newSta = []
          for the length of sta...
            pop the node (curr)
            put the children on newSta if there are any
            
          sta = newSta
          
        return 5
        """
        
        if not root: return 0
        
        sta = [root]
        d = 0
        while sta:
          d += 1
          newSta = []
          for _ in range(len(sta)):
            curr = sta.pop()
            print(curr.val)
            if curr.right: newSta.append(curr.right)
            if curr.left: newSta.append(curr.left)
              
          sta = newSta
          
        return d