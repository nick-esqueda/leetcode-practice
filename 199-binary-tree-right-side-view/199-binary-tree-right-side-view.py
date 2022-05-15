# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
      """
      declare res list
      declare q
      while q...
        declare list for current level
        for len(q)...
          pop from q
          push that val to current level
          push left and right to q (IN THAT ORDER)
        push the last val in the level to the res list
      return res list
      """
      if not root: return root
      
      res = []
      q = [root]
      while q:
        level = []
        for i in range(len(q)):
          curr = q.pop(0)
          level.append(curr.val)
          if curr.left: q.append(curr.left)
          if curr.right: q.append(curr.right)
        res.append(level[-1])
      return res
          
        
      
      
      
