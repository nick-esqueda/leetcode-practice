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
