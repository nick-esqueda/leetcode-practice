# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_sum(root):
  if not root:
    return 0
  return root.val + tree_sum(root.left) + tree_sum(root.right)
