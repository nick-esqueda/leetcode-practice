# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_value_count(root, target):
  """
  count 0 or 1
  if root.val == target, count = 1, else 0,
  sum that in the return with calls to left and right
  """
  if not root:
    return 0
  count = 1 if root.val == target else 0
  return count + tree_value_count(root.left, target) + tree_value_count(root.right, target)
