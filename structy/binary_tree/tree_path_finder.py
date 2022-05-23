# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

from collections import deque

def path_finder(root, target):
  if not root:
    return
  
  q = deque([ [root] ])
  while q:
    curr_path = q.popleft()
    curr_node = curr_path[-1]
    
    if curr_node.val == target:
      return [node.val for node in curr_path]
    
    if curr_node.left:
      q.append([*curr_path, curr_node.left])
    if curr_node.right:
      q.append([*curr_path, curr_node.right])


def path_finder(root, target):
  if not root:
    return None
  
  if root.val == target:
    return [root.val]
  
  left = path_finder(root.left, target)
  right = path_finder(root.right, target)

  if left:
    return [root.val] + left
  elif right:
    return [root.val] + right
  else:
    return None
  
