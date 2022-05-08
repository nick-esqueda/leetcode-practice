# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def isBalanced(self, root: Optional[TreeNode]) -> bool:
    """
    abs(left subtree height - right subtree height) <= 1
    null nodes have height of 0 and True for isBalanced
    
    
    inner func:
      get the height and isBalanced of left and right subtrees 
      subtract those heights, and if <= 1, isBalanced = T
      return (max(heightL, heightR) + 1, isBalanced) to the caller
    
    return result of calling func, and take index 1 (isBalanced)
    """
    
    def dft(node):
      if not node:
        return (0, True)
      
      left, right = dft(node.left), dft(node.right)
      isBalanced = abs(left[0] - right[0]) <= 1 and left[1] and right[1]
      
      return (max(left[0], right[0]) + 1, isBalanced)
    
    return dft(root)[1]

    