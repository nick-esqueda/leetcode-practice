# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

from collections import deque

def _all_tree_paths(root):
  if root is None:
    return []
  if root.left is None and root.right is None:
    return [[root.val]]
  
  child_paths = _all_tree_paths(root.left) + _all_tree_paths(root.right)
  for path in child_paths:
    path.append(root.val)
    
  return child_paths


def all_tree_paths(root):
  all_paths = _all_tree_paths(root)
  return list(map(lambda path: path[::-1], all_paths))
    