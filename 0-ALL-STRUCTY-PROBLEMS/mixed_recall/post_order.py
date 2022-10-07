# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def post_order(root):
  vals = []
  get_vals(root, vals)
  return vals

def get_vals(root, vals):
  if not root:
    return

  get_vals(root.left, vals)
  get_vals(root.right, vals)
  vals.append(root.val)
