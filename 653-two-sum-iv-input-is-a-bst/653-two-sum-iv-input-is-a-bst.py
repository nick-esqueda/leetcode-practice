# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """
        declare hashset
        
        DFS:
          if not node, return false
          if findTarget(left) == True, return true
          if curr.val is inside the hashset, return true
          if it's not inside set, put k - curr.val inside set
          if findTarget(right) == True, return true
          return false (there's no stack frame that returned true)
          
        call DFS with root, and return the outcome of the call
        """
        def dfs(root, comps):
          if not root:return False
          
          if dfs(root.left, comps) is True: return True
          
          if root.val in comps: return True
          else: comps.add(k - root.val)
          
          if dfs(root.right, comps) is True: return True
          
          return False
        
        return dfs(root, set())