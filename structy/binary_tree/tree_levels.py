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


def _tree_levels(root, levels, curr_level=0):
  """
  pass in an array to store sub arrays where each index corresponds to the level
  keep track of the curr level by passing in a level param (+1 on each child call)
  if the outer array at the current index doesn't exist yet, append a new array
    with curr.val inside (should work because you're going down level by level)
  if an array at the curr level/idx exists, append curr.val to that sub array
  go down left and right, passing in level + 1
  """
  if root is None:
    return
  
  try:
    levels[curr_level].append(root.val)
  except:
    levels.append([root.val])
    
  _tree_levels(root.left, levels, curr_level + 1)
  _tree_levels(root.right, levels, curr_level + 1)
  
  
def tree_levels(root):
  levels = []
  _tree_levels(root, levels)
  return levels
  