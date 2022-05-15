# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        if you traverse in order, then you will get the nodes in order of value
        count how many iterations (or length of collected values), and return the val that is at the kth node
        """
        nums = []
        def in_order_trav(root):
          if not root:
            return
          
          in_order_trav(root.left)
          nums.append(root.val)
          in_order_trav(root.right)
          
          return
          
        in_order_trav(root)
        print(nums)
        return nums[k - 1]