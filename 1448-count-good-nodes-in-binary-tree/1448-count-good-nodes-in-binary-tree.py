# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
      """
      use a q to store and iterate through paths (arrays as paths)
      if no root, return 0
      declare count = 0
      q = [[root]]
      while q:
        pop the front path
        curr = last node in the path
        if curr[-1] is the max in that path, increment count
        push the left neighbor to a new list with the rest of curr path, and push that list to the q
        ^ do the same for right
      return count
      """
      if not root: return 0
      
      count = 0
      q = [[root]]
      while q:
        path = q.pop(0)
        curr = path[-1]
        
        path_values = [node.val for node in path]
        if max(path_values) == path_values[-1]:
          count += 1
          
        if curr.left:
          q.append([*path, curr.left])
        if curr.right:
          q.append([*path, curr.right])
          
      return count
        