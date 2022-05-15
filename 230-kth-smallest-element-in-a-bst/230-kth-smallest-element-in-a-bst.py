# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
#   RECURSIVE:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         """
#         if you traverse in order, then you will get the nodes in order of value
#         collect all nums in order, and return the val at the k - 1 idx
        
#         """
#         nums = []
#         def in_order_trav(root):
#           if not root:
#             return
          
#           in_order_trav(root.left)
#           nums.append(root.val)
#           in_order_trav(root.right)
          
#           return
          
#         in_order_trav(root)
#         return nums[k - 1]

# ITERATIVE
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
      """
      declare var for k (starting at 0 and incrementing for every node being processed)
      start with a stack (empty at first) and a curr node
      while we have a curr and a stack...
        while there is a curr...
          push curr to the stack
          update curr to curr.left
        (once you exit this loop ^, you are as far left as possible without going right yet)
        pop the top of stack and set as curr
        increment k var
        return curr's val if k var == parameter k
        if not, set curr as curr.right
      """
      curr_k = 0
      sta = []
      curr = root
      while sta or curr:
        while curr:
          sta.append(curr)
          curr = curr.left
        curr = sta.pop()
        curr_k += 1
        if curr_k == k:
          return curr.val
        curr = curr.right