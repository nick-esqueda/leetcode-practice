# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        while loop through both trees (have 2 different stacks)
        if the values at any point are not equal, return false
        """
        
        staP = [p]
        staQ = [q]
        
        while (staP and staQ):
          currP = staP.pop()
          currQ = staQ.pop()
          
          if currP is None and currQ is not None or currQ is None and currP is not None:
            return False
          if currP is None or currQ is None:
            continue
            
          
          if currP.val != currQ.val:
            return False
          
          staP.append(currP.left)
          staP.append(currP.right)
          
          staQ.append(currQ.left)
          staQ.append(currQ.right)
        
        return len(staP) == len(staQ)