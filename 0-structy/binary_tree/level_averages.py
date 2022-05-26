from collections import deque

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def _level_averages(root, levels, lvl=0):
  if root is None:
    return
  
  if len(levels) == lvl:
    levels.append([root.val])
  else:
    levels[lvl].append(root.val)
    
  _level_averages(root.left, levels, lvl + 1)
  _level_averages(root.right, levels, lvl + 1)

def level_averages(root):
  levels = []
  _level_averages(root, levels)
  return list(map(lambda lvl: sum(lvl) / len(lvl), levels))
    
    
def level_averages(root):
  if root is None:
    return []
  
  levels = []
  q = deque([root])
  while q:
    len_q = len(q)
    level_sum = 0
    for _ in range(len_q):
      curr = q.popleft()
      level_sum += curr.val
      if curr.left:
        q.append(curr.left)
      if curr.right:
        q.append(curr.right)
    levels.append(level_sum / len_q)
    
  return levels

    
    
    
    
    
