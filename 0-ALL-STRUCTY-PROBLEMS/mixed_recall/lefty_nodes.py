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
    

def lefty_nodes(root, lefties=[], cur_lvl=0):
  if not root:
    return []
  
  if cur_lvl == len(lefties):
    lefties.append(root.val)
  
  lefty_nodes(root.left, lefties, cur_lvl + 1)
  lefty_nodes(root.right, lefties, cur_lvl + 1)
  return lefties
  
  
  
  