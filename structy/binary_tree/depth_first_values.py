# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def depth_first_values(root, vals=[]):
  if not root:
    return vals
  vals.append(root.val)
  depth_first_values(root.left, vals)
  depth_first_values(root.right, vals)
  return vals
