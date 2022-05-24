# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

from collections import deque

def tree_levels(root):
  if root is None:
    return []
  
  levels = []
  
  q = deque([root])
  while q:
    level = []
    
    for i in range(len(q)):
      curr = q.popleft()
      level.append(curr.val)
      
      if curr.left:
        q.append(curr.left)
      if curr.right:
        q.append(curr.right)
        
    levels.append(level)
    
  return levels
