# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def flip_tree(root):
  """
  at every level, root.right should be assigned to root.left and vice versa
  should this be done from the bottom up?
  """
  if not root:
    return
  
  old_left = root.left
  root.left = root.right
  root.right = old_left
  
  flip_tree(root.left)
  flip_tree(root.right)
  return root


def flip_tree(root):
  if not root:
    return
  
  new_left = flip_tree(root.left)
  new_right = flip_tree(root.right)
  root.left = new_right
  root.right = new_left
  return root
