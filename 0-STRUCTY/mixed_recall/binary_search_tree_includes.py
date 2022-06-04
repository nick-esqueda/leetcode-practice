# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def binary_search_tree_includes(root, target):
  if not root:
    return False
  
  if root.val == target:
    return True
  
  if target < root.val:
    return binary_search_tree_includes(root.left, target)
  elif target > root.val:
    return binary_search_tree_includes(root.right, target)
      
  
  
  
