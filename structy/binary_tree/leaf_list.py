# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def leaf_list(root):
  leaves = []
  def get_leaves(root):
    if root is None:
      return
    if root.left is None and root.right is None:
      leaves.append(root.val)
      return
    get_leaves(root.left)
    get_leaves(root.right)

  get_leaves(root)
  return leaves
