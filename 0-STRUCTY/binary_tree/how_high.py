# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def how_high(node):
  if not node:
    return -1
  return 1 + max(how_high(node.left), how_high(node.right))
