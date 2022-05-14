# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        declare result arr
        declare q
        while q...
          declare arr to represent each level
          for the length of the q...
            pop front of q
            push curr.val to the level's arr
            push right and left to q
          push level arr to result arr
        return result arr
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
          res.append(level)
        return res