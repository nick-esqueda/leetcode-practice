# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

from collections import deque

def lefty_nodes(root):
  if not root:
    return []
  
  q = deque([root])
  lefties = []
  while q:
    for i in range(len(q)):
      print(q)
      cur = q.popleft()
      if i == 0:
        lefties.append(cur.val)
      if cur.left:
        q.append(cur.left)
      if cur.right:
        q.append(cur.right)
  
  return lefties
    
    