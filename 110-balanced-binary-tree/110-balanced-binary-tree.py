# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def isBalanced(self, root: Optional[TreeNode]) -> bool:
    """
    on each frame, need to get the depth of the left subtree and the right subtree
    if the difference in depths is > 1 or the left tree or right tree aren't balanced, that frame's tree is not balanced
    return true if both the left and the right subtree are balanced
    
    TO GET DEPTH:
    if not node: return 0
      
    """

    def dft(root):
      if not root: 
        return (0, True)

      left = dft(root.left)
      right = dft(root.right)
      
      isBalanced = abs(left[0] - right[0]) <= 1 and left[1] and right[1]

      return (max(left[0], right[0]) + 1, isBalanced)

    return dft(root)[1]