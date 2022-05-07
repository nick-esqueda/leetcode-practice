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
          
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        DFT
              3
            9   20
           1 4    10
              5
             2 6
        
        
        sta = [(1, 3),(4, 3)]
        maxDepth = 3
        curr = 
        node = 
        currDepth = 
        
        while sta...
          pop top of stack (curr)
          node, depth = curr
          
          if depth > maxDepth, replace it
          
          if node.left, push it to the stack with the currDepth + 1
          if node.right, push it to the stack with the currDepth + 1
          
        return maxDepth
        """
        
        if not root:
          return 0
        
        maxDepth = 1
        sta = [(root, 1)]
        while sta:
          curr = sta.pop()
          (node, depth) = curr
          
          if depth > maxDepth:
            maxDepth = depth
            
          if node.left:
            sta.append((node.left, depth + 1))
          if node.right:
            sta.append((node.right, depth + 1))
            
        return maxDepth
        
        
        
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#       """
#       RECURSIVE

#       if the root is none, return 0
#       otherwise...
#       take the max of the left tree and the right tree
#       return the max + 1 (for this frame) to the caller
#       """
      
#       if not root:
#         return 0
      
#       return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1